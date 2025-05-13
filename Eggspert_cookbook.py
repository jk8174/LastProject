# Shakila Jafari
# May 4, 2025
import json    # Using json format to read the recipe files
import os

RECIPE_PATH = "./recipes/"   # sets a variable with the path to my recipes folder
print("Welcome to the Eggspert cookbook! We will provide you with the best egg recipes. You are just one click away!")


def get_recipes_from_folder():   # A function to get the recipes from the folder
    cookbook = []
    filenames = os.listdir(RECIPE_PATH)
    for name in filenames:
        recipe = read_recipe_from_file(name)
        cookbook.append(recipe)
    return cookbook


def read_recipe_from_file(filename):   # A function to read the recipes from the file
    """
    Gets a recipe from a file
    :return: a dictionary containing the recipe
    """
    with open(RECIPE_PATH + filename, 'r') as file:
        data = file.read()
        return json.loads(data)


def search_by_tag(cookbook, tag):  # searching by tag
    matched = []
    for recipe in cookbook:
        tags = recipe.get("tags", [])
        if tag in tags:
            matched.append(recipe)
    return matched


def print_recipe(recipe, multiplier=1):   # Printing the recipe
    print(f"\nRecipe: {recipe.get('title', 'Untitled')}\n")

    print("Ingredients:")   # Printing the ingredients
    ingredients = recipe.get("ingredients", {})
    for item, quantity in ingredients.items():   # A loop that gets the ingredients name and quantity
        try:
            scaled_quantity = float(quantity) * multiplier   # Multiplies the quantity/ double it if the user wants
            print(f" - {scaled_quantity} {item}")
        except (ValueError, TypeError):
            print(f" - {item} ({quantity})")  # fallback

    print("\nInstructions:")
    instructions = recipe.get("instructions", [])

    if isinstance(instructions, str):
        # You mentioned slashes are stored as /n — not newlines
        steps = [step.strip() for step in instructions.split('/n') if step.strip()]
    else:
        steps = instructions  # assume it's already a list

    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")


def print_titles(recipes):   # prints the recipe titles
    for i, recipe in enumerate(recipes):
     print(f"{i + 1}. {recipe.get('title', 'Untitled')}")


def print_tags(recipes):   # Prints the recipes that the tags are in it
    # TODO make a set. Loop through each recipe. add all tags to the set. print each item in set
    tags_set = set()
    for recipe in recipes:
        for tag in recipe.get("tags", []):
            tags_set.add(tag)
    for tag in tags_set:
        print(tag)


def main():
    recipes = get_recipes_from_folder()
    cont = True
    while cont:
        choice = ""
        while choice not in ["tag", "list", "quit"]:
            choice = input("Type tag to search by tag or list to see every recipe, or quit to leave:")

            if choice == "tag":
                print("Tag search selected.")
                tag = input("Enter a tag to search: ")
                found = search_by_tag(recipes, tag)
                if found:
                    for i, recipe in enumerate(found):
                        print(f"{i + 1}. {recipe['title']}")
                    try:
                        index = int(input("Enter the number of the recipe to view: ")) - 1
                        multiplier = int(input("Enter a multiplier (e.g. 2 to double): "))
                        print_recipe(found[index], multiplier)
                    except (IndexError, ValueError):
                        print("Wrong selection or multiplier.")
                else:
                    print("No recipe found with that tag :(")
            elif choice == "list":
                print("Recipe list:")
                print_titles(recipes)
                try:
                    index = int(input("Enter the number of the recipe to view: "))-1
                    multiplier = int(input("Enter a multiplier (e.g. 2 to double): "))
                    print_recipe(recipes[index], multiplier)
                except (IndexError, ValueError):
                    print("Invalid selection or multiplier.")
            elif choice == "quit":
                cont = False
                print("Goodbye!")
            else:
                print("Please enter a valid response:)")


if __name__ == "__main__":
    main()

"""
recipes from text files
search based on: tags
    program is aware of tags
user can add recipes by putting txt files in a folder
ability to double recipe
    program is also aware of measurements
"""
