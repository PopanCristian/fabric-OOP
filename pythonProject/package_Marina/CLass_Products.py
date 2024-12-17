
import os.path
import csv
from itertools import product
import pandas as pd

#trebuie sa creez o functie LISTA SEPRATA DE CLASA IN MAIN prin care trebuie sa sterg produsul atat din lista creata cat si din csv

# try to have access at the csv file with the list of products and their ingredients, gram weight and price
class Product:
    products = []
    def __init__(self, produs, ingrediente, pret):
        self.produs = produs
        self.ingrediente = ingrediente
        self.pret = pret
    @staticmethod
    def file_products(name_file):
        if not os.path.isfile(name_file):
            print(f"The file {name_file} does not exist.")
            return
        with open(name_file, mode='r') as f:
            reader = csv.DictReader(f)  # Citește fișierul ca un dicționar !!! nu mai incearca cu pd
            for row in reader:
                produs = row['Denumire']
                ingrediente = row['Ingrediente']
                pret = row['Pret']
                product_instance = Product(produs, ingrediente, pret)
                Product.products.append(product_instance)

  # initiate the terms used in csv like produs, gramaj, ingrediente, pret
    def __str__(self):
         return f"Produs(nume='{self.produs}, ingrediente='{self.ingrediente}', pret='{self.pret}')"

# show the list of registrated products
    @classmethod
    def show_list_of_products(cls):
        if not cls.products:
            print("There are no registered products")
        else:
            print("List of products:")
            for another_product in cls.products:
                print(another_product)


#delete a product base its name
    @classmethod
    def delete_product(cls, product_name):
        found_product = False
        for product in cls.products:
            if product.produs == product_name:
                cls.products.remove(product)
                product_name = True
                print(f" The product '{product_name}' has been deleted.")
                break
        if not found_product:
            print(f"The product '{product_name}' was not found.")





if __name__ == '__main__':
    name_file = 'products.csv'
    file = pd.read_csv(name_file)
    Product.file_products(name_file)
    Product.show_list_of_products()
    product_deleted = input("Enter the product you want to delete (in romanian): ")
    Product.delete_product(product_deleted)
    print("\nUpdated list of products:")
    Product.show_list_of_products()


