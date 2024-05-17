import json

def load_recipes(filename):
    with open(filename, 'r') as file:
        recipes = json.load(file)
    return recipes

def generate_recipe(ingredients, recipes):
    # Simple rule-based approach: Find a recipe that matches the ingredients
    for recipe in recipes:
        if all(ingredient in recipe['ingredients'] for ingredient in ingredients):
            return recipe
    return None

def main():
    print("Welcome to Recipe Generator!")

    # Load recipes
    recipes = load_recipes('recipes.json')

    # Get user input for ingredients
    ingredients = input("Enter ingredients (comma-separated with minimum five ingredients): ").strip().lower().split(',')

    # Generate recipe
    recipe = generate_recipe(ingredients, recipes)

    if recipe:
        print("\nHere's a recipe for you:")
        print(f"Title: {recipe['title']}")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient}")
        print("Instructions:")
        print(recipe['instructions'])
    else:
        print("Sorry, no recipe found with those ingredients.")

if __name__ == "__main__":
    main()
