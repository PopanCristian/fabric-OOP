import pandas as pd

class Stock:
    def __init__(self, stock_file):
        self.stock_file = stock_file
        self.stock_df = pd.read_csv(stock_file)

    def display_stock(self):
        print("\nCurrent stock:\n")
        print(self.stock_df)

    def verify_product_details(self, product_name, ingredients_list):
        """
        Verify if the stock have ingredients to create a product
        """
        for ingredient_dict, quantity_needed in ingredients_list:
            current_stock = self.stock_df.loc[self.stock_df['Product'] == ingredient_dict, 'Quantity'].values
            if len(current_stock) == 0 or current_stock[0] < quantity_needed:
                return False
        return True

    def decrease_stock(self, ingredient, quantity):
        """
        Scade cantitatea de ingredient din stoc.
        """
        if ingredient in self.stock_df['Product'].values:
            self.stock_df.loc[self.stock_df['Product'] == ingredient, 'Quantity'] -= quantity
            self.stock_df.to_csv(self.stock_file, index=False)
        else:
            print(f"Ingredientul {ingredient} nu există în stoc!")

    def add_product_in_stock(self, product_name, quantity):
        """
        Adaugă un produs finit în stoc.
        """
        if product_name in self.stock_df['Product'].values:
            self.stock_df.loc[self.stock_df['Product'] == product_name, 'Quantity'] += quantity
        else:
            new_row = {'Product': product_name, 'Quantity': quantity}
            self.stock_df = pd.concat([self.stock_df, pd.DataFrame([new_row])], ignore_index=True)
        self.stock_df.to_csv(self.stock_file, index=False)

    def add_ingredient_in_stock(self, ingredient, quantity):
        """
        Adaugă materii prime în stoc.
        """
        if ingredient in self.stock_df['Product'].values:
            self.stock_df.loc[self.stock_df['Product'] == ingredient, 'Quantity'] += quantity
        else:
            new_row = {'Product': ingredient, 'Quantity': quantity}
            self.stock_df = pd.concat([self.stock_df, pd.DataFrame([new_row])], ignore_index=True)
        self.stock_df.to_csv(self.stock_file, index=False)

