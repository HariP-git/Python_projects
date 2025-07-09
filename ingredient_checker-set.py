recipe_ingredients={"mango","milk","ice","sugar"}

user_input=input("enter ingredinets you have :")
user_ingredients = set(user_input.split(","))

extra_ingredients=user_ingredients-recipe_ingredients
missing_ingredients=recipe_ingredients-user_ingredients

print("-----ingredient check----")
if missing_ingredients:
    print(f"you are missing:{','.join(missing_ingredients)}")

else:
    print("you have all ingredients")

if extra_ingredients:
    print(f"you are missing:{','.join(extra_ingredients)}")

else:
    print("you have all ingredients")

