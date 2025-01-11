import csv
import ast

# Citim ingredientele pentru produsul dorit
import csv

def get_ingredients_for_product(product_name, products_file_path):
    with open(products_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].strip().lower() == product_name.strip().lower():
                # Separăm ingredientele prin virgulă și le transformăm într-o listă
                ingredients = row['Ingredients'].split(',')
                # Curățăm fiecare ingredient de eventuale spații suplimentare
                ingredients = [ingredient.strip() for ingredient in ingredients]
                return ingredients
    return None
