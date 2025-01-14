
import ast

import csv

def get_ingredients_for_product(product_name, products_file_path):
    with open(products_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].strip().lower() == product_name.strip().lower():
                ingredients = ast.literal_eval(row['Ingredients']) # from string to list of dicts
                return ingredients
    return None
