import os.path
import csv
from itertools import product
import pandas as pd

# try to have access at the csv file with the list of products and their ingredients, gram weight and price
class Product:
    products = []
    def __init__(self, product, ingredients, price):
        self.product = product
        self.ingredients = ingredients
        self.price = price
    @staticmethod
    def file_products(name_file):
        if not os.path.isfile(name_file):
            print(f"The file {name_file} does not exist.")
            return
        with open(name_file, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = row['Name']
                ingredients = (row['Ingredients'])
                price = (row['Price'])
                product_instance = Product(product, ingredients, price)
                Product.products.append(product_instance)

  # initiate the terms used in csv like denumire, ingrediente, pret
    def __str__(self):
         return f"Product(name='{self.product}, ingredients='{self.ingredients}', price='{self.price}')"

# show the list of registrated products
    @classmethod
    def show_list_of_products(cls):
        if not cls.products:
            print("There are no registered products")
        else:
            print("List of products:")
            for another_product in cls.products:
                print(another_product)


    @staticmethod
    def add_product(name_file):
        while True:
            answer = input().strip().lower() #delete white spaces and convert the input to lowercase
            # "Do you want to add a new product? (Yes/No): "
            if answer == 'no':
                break
            elif answer == 'yes': #we need to ask the user the details of the new product
                product = input("Write the name of the new product: ").strip()
                ingredients = input("Write the ingredients and quantities (e.g., Milk Powder:2, Sugar:3) separated by comma: ").strip()
                price = input("Write the price of the product: ").strip()

                ingredients_list = [] #we process the ingredients in the dictionary list
                try:
                    ingredients_types = ingredients.split(',') #'type' comes from the type of ingredient introduce by the user
                    for type in ingredients_types:
                        ingredient, quantity = type.split(':')
                        ingredients_list.append({ingredient.strip(): int(quantity.strip())})
                except ValueError:
                    print("Invalid ingredient format! Please use the format 'Ingredient:Quantity,Ingredient:Quantity'.")
                    continue
                try: #create the produced object and add to the class and CSV
                    price = float(price)
                    new_product = Product(product, ingredients_list, price)
                    Product.products.append(new_product)

                    with open(name_file, mode='a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            product,
                            str(ingredients_list).replace("'", '""'),
                            price
                        ])
                    print(f"The product {product} has been added successfully!")
                except ValueError:
                    print("Invalid price format! Please enter a valid number.")
            else:
                print("Invalid answer! Please introduce 'yes' or 'no'.")


#delete a product base its name
    @classmethod
    def delete_product(cls, name_file):
        while True:
            del_answer = input().strip().lower() #"Do you want to delete a product? Yes/No"
            if del_answer == 'no':
                break
            elif del_answer == 'yes':
                df = pd.read_csv(name_file)
                print(df['Name'])
                product_name = input("Introduce the product you want to delete: ").strip()
                updated_products = [p for p in Product.products if p.product.lower() != product_name.lower()] #filtered the list to keep the products that does not corespund to the given name
                if len(updated_products) == len(Product.products): #check if the product was founded
                    print(f"The product {product_name} was not foound.")
                    return
                Product.products = updated_products #update the list products
                with open(name_file, mode='w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Name', 'Ingredients', 'Price'])
                    for p in Product.products:
                        writer.writerow([p.product, p.ingredients, p.price])
                    print(f"The product '{product_name} has been successfully deleted!")
            else:
                print("Invalid answer! Please introduce 'yes' or 'no'.")
                break




if __name__ == '__main__':
    name_file = 'products.csv'
    file = pd.read_csv(name_file)
    Product.file_products(name_file) #show the existent products
    Product.show_list_of_products()
    Product.add_product(name_file)# add new product
    Product.delete_product(name_file) #delete a product
    #product_deleted = input("Enter the product you want to delete: ")
    # Product.delete_product(product_deleted)
    print("\nUpdated list of products:")
    Product.show_list_of_products()


