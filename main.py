# dinner_decider.py
print("👩‍🍳 Welcome to the Recipe Recommender! 🍴")

# Cookbook: recipes mapped to their required ingredients
cookbook = {
    "Paneer Butter Masala": ["paneer", "tomato", "onion", "butter"],
    "Matar Paneer": ["paneer", "tomato", "onion", "peas"],
    "Palak Paneer": ["paneer", "spinach", "onion", "garlic"],
    "Veg Pulao": ["rice", "peas", "carrot", "onion"],
    "Aloo Paratha": ["potato", "wheat flour", "onion", "spices"],
    "Tomato Soup": ["tomato", "onion", "garlic"],
    "Curd Rice": ["rice", "curd", "mustard seeds", "curry leaves"],
}

# Step 1: Ask user for ingredients
user_input = input("Enter ingredients you have (comma separated): ")
user_ingredients = {item.strip().lower() for item in user_input.split(",")}

# Step 2: Find matching recipes
possible_recipes = []

for recipe, ingredients in cookbook.items():
    required = set(ingredients)
    if required.issubset(user_ingredients):  # All ingredients available
        possible_recipes.append(f"{recipe} ✅ (You have everything!)")
    elif required & user_ingredients:  # Partial match
        missing = required - user_ingredients
        possible_recipes.append(f"{recipe} (You still need: {', '.join(missing)})")

# Step 3: Show results
print("\nBased on your ingredients, you can make:\n")

if possible_recipes:
    for r in possible_recipes:
        print("-", r)
else:
    print("😔 Sorry, no recipes match your current ingredients. Maybe order some Vadapav? 😉")
