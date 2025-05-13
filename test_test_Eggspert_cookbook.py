from unittest import TestCase
from Eggspert_cookbook import get_recipes_from_folder, read_recipe_from_file, search_by_tag, print_titles, print_tags


class TestEggspertCookbook(TestCase):
    def test_get_recipes_from_folder(self):
        recipes = get_recipes_from_folder()
        self.assertIsInstance(recipes, list)

    def test_search_by_tag(self):
        recipes = get_recipes_from_folder()
        results = search_by_tag(recipes, "classic")
        self.assertIsInstance(results, list)

    def test_print_titles(self):
        # you can call the function and check manually if it prints titles
        print_titles(get_recipes_from_folder())

    def test_print_tags(self):
        print_tags(get_recipes_from_folder())




