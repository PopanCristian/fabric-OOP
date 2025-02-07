import pandas as pd
from package_cristi.class_stock import Stock

def read_csv_file(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame
    """
    return pd.read_csv(file_path)

def write_csv_file(df, file_path):
    """
    Writes a Pandas DataFrame to a CSV file
    """
    df.to_csv(file_path, index=False)


class Employee:
    def __init__(self, name, age, role, hire_date, salary):
        """
        Initializes an Employee object with basic employee information
        :param name:
        :param age:
        :param role:
        :param hire_date:
        :param salary:
        """
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary
        self.hire_date = hire_date


    def display_info(self):
        """
        Returns a formatted string with the employee's information
        :return: A string containing the employee's details
        """
        return (f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Hire Date: {self.hire_date},"
                f"Salary: {self.salary}")

class Operator(Employee):
    def __init__(self, name, age, hire_date, salary, products_processed):
        """
        Initializes and Operator object, which is a type of Employee
        :param name:
        :param age:
        :param hire_date:
        :param salary:
        :param products_processed:
        """
        super().__init__(name, age, "Operator", hire_date, salary)
        self.products_processed = products_processed

    def place_order(self, product_name, ingredients_list, stock, stock_keeper):

        #Verify if ingredients are sufficient using the stock class method
        if stock.verify_product_details(product_name, ingredients_list, stock):
            print(f"Producing {product_name} ...")

            #If stock has sufficient ingredients, decrease the stock for each ingredient used
            for ingredient, quantity in ingredients_list:
                stock.decrease_stock(ingredient, quantity) #Decrease the stock of raw materials

            #Add the finished product to the stock
            stock.add_product_in_stock(product_name, 1) #Assuming the quantity of finished product is 1
            self.products_processed += 1 #Update the processed products count
            print(f"{product_name} has been successfully produced. Total processed: {self.products_processed}")
        else:
            print(f"Not enough stock to produce {product_name}. Please inform the StockKeeper.")
            #If not enough stock, ask the StockKeeper to add ingredients
            stock_keeper.supply_ingredients(product_name, ingredients_list, stock)

class Manager(Employee):
    def __init__(self, name, age, hire_date, salary):
        """
        Initializes a Manager object, which is a type of Employee
        :param name:
        :param age:
        :param hire_date:
        :param salary:
        """
        super().__init__(name, age, "Manager", hire_date, salary)

    def add_employees(self, file_path):
        """
        Adds a new employee to the CSV file by asking for user input
        :param file_path:
        """
        #TODO coloanele competence level,specialization, products_processed trebuie eliminate( prea multe detalii de care nu ne folosim)
        #TODO cand se fac adaugarea unui nou angajat cand cerem detaliile despre angajat trebuie sa dam exemplu acolo unde trebuie, ex. data angajarii)
        while True:
            print("Enter the data for the new employee")
            print("-Name: In the format FirstName LastInitial, e.g. Andreea B.")
            print("-Age: A whole number, e.g. 22")
            print("-Role: Choose from Manager, Operator, StockKeeper")
            print("-Hire Date: In the format dd/mm/yyyy, e.g. 01/01/2023")
            print("-Salary: A numeric value, e.g. 3000")
            print("-Separate the values by commas, e.g. Andreea B., 22, Manager, 01/01/2023, 3000")
            
            data = input("Please enter employee details: ")
            employee_data = data.split(",") #Split the input string into a list base on commas

            if len(employee_data) != 5:
                print("Invalid number of information. Please enter exactly 5 pieces of information.")
                continue #If the input is invalid, ask for the input again

            name, age, role, hire_date, salary = [item.strip() for item in employee_data] #Remove any extra spaces and assign the
                                                                                                                            #values to respective variables
            new_employee = Employee(name, int(age), role, hire_date, int(salary)) #Create a new Employee object

            employees_df = pd.read_csv(file_path)
            #Prepare the new employee's data for adding to the DataFrame
            new_employee_data = {
                'Name': new_employee.name,
                'Age': new_employee.age,
                'Role': new_employee.role,
                'Hire Date': new_employee.hire_date,
                'Salary': new_employee.salary,
            }
            new_employee_df = pd.DataFrame([new_employee_data]) #Create a DataFrame from the new employee's data
            employees_df = pd.concat([employees_df, new_employee_df], ignore_index=True) #Append the new employee's data to the existing Dataframe
            write_csv_file(employees_df, file_path) #Write the updated DataFrame back to the CSV file
            print(f"Employee {new_employee.name} has been successfully added to the CSV file.")
            break

    def display_employees(self, file_path):
        """
        Display the list of employees from a CSV file
        :param file_path:
        """
        #Read employees from csv file
        employees_df = pd.read_csv(file_path)
        print(f"Employees list:")
        print(employees_df[['Name', 'Age', 'Role','Hire Date', 'Salary']])


    def remove_employees(self, file_path):
        """
        Removes an employee from the list based on their name
        :param file_path:
        """
        while True:
            employees_df = pd.read_csv(file_path)
            print(employees_df['Name'])
            name = input("Please enter the name of the employee you want to remove: ")


            if name not in employees_df['Name'].values: #Check if the employee exists in the DataFrame
                print(f"No employee found with the name: {name}")
            else:
                #Filter the employee with the specified name from DataFrame
                updated_employees = employees_df[employees_df['Name'] != name]

                #Check if the number of the rows in the original DataFrame is the same as the filtered one
                #If no rows were removed, it means no employee, with the give name was found
                if len(employees_df) == len(updated_employees):
                    print(f"No employee found with the name: {name}")
                else:
                    print(f"Employee {name} has been removed")
                    #Update the csv file with updated list of employees
                    write_csv_file(updated_employees, file_path) #update de csv file after remove
                break

class StockKeeper(Employee):
    def __init__(self, name, age, salary, hire_date, stock: Stock):
        """
        Initializes a StockKeeper object, which is a type of Employee
        :param name:
        :param age:
        :param salary:
        :param hire_date:
        :param stock:
        """

        super().__init__(name, age, "StockKeeper", salary, hire_date)
        self.stock = stock

    def supply_ingredients(self, ingredients_list):
        """
         If not enough stock exists for a product, supply the required ingredients by adding extra stock.
        :param ingredients_list:
        """
        #Loop through the ingredients and check if they are available
        for ingredient, required_quantity in ingredients_list:
            stock_df = pd.read_csv("package_cristi/stock.csv") #Read the current stock data

        #Check if the ingredient exists and if there is enough in stock
        current_stock = stock_df.loc[stock_df['Product'] == ingredient, 'Quantity'].values

        if len(current_stock) == 0 or current_stock[0] < required_quantity:
            #If stock is insufficient, calculate how much to add
            missing_quantity =  required_quantity - current_stock[0] if len(current_stock) > 0 else required_quantity
            extra_quantity = missing_quantity + (missing_quantity * 0.2) #Add 20% more

            print(f"Not enough stock for {ingredient}. Adding {int(extra_quantity)} units.")

            #Call the add_ingredient_in_stock method form the Stock class to add the missing ingredients
            self.stock.add_ingredient_in_stock(ingredient, int(extra_quantity))
        else:
            print(f"Stock for {ingredient} is sufficient.")


    def show_stock(self):
        """
        Calls the display_stock method from Stock to display the current stock.
        """
        self.stock.display_stock() #Call the display_stock method from Stock to display the stock

    def update_stock(self, material, quantity):
        """
        Updates the stock of a specific material
        :param material:
        :param quantity:
        """
        # Check if the material exist in stock
        if material in self.stock:
            # If quantity is positive, add to the existing stock
            if quantity > 0:
                self.stock[material] = self.stock[material] + quantity
                print(f"Stock updated: {material} +{quantity} units. New quantity: {self.stock[material]} units")
            # If quantity is negative, reduce the stock, but not below zero
            elif quantity < 0:
                if self.stock[material] + quantity >= 0:  # Ensure the stock doesn't go negative
                    self.stock[material] = self.stock[material] + quantity
                    print(
                        f"Stock updated: {material} -{abs(quantity)} units. New quantity: {self.stock[material]} units")
                else:
                    # If trying to reduce more than available, print an error message
                    print(f"Error: Not enough stock of {material} to reduce by {abs(quantity)} units.")
            else:
                # If the material does not exist in the stock, add it with the given quantity
                self.stock[material] = quantity

                print(f"New material {material} added to stock with {quantity} units.")

