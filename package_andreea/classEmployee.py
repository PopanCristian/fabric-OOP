import pandas as pd

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
    def __init__(self, name, age, role, hire_date, salary, specialization, competence_level):
        """
        Initializes an Employee object with basic employee information
        :param name:
        :param age:
        :param role:
        :param hire_date:
        :param salary:
        :param specialization:
        :param competence_level:
        """
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary
        self.hire_date = hire_date
        self.specialization = specialization
        self.competence_level = competence_level


    def display_info(self):
        """
        Returns a formatted string with the employee's information
        :return: A string containing the employee's details
        """
        return (f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Hire Date: {self.hire_date},"
                f"Salary: {self.salary},Specialization: {self.specialization}, Competence Level: {self.competence_level}")


class Operator(Employee):
    def __init__(self, name, age, hire_date, salary, specialization, competence_level, products_processed):
        """
        Initializes and Operator object, which is a type of Employee
        :param name:
        :param age:
        :param hire_date:
        :param salary:
        :param specialization:
        :param competence_level:
        :param products_processed:
        """
        super().__init__(name, age, "Operator", hire_date, salary, specialization, competence_level)
        self.products_processed = products_processed


    def process_material(self, material, quantity, stock):
        """
        Processes a material by reducing the stock and increasing the number of products processed
        :param material:
        :param quantity:
        :param stock:
        """
        #Trebuie sa verific cantitatea necesara cu cantitatea din stock(csv ul lu cristi) din lista de ingrediente din csv ul marinei
        #dupa ce creez un produs, stockul scade si trb sa verificam daca stockul este suficient
        #Check if there is enough stock of the specified material
        if stock.get(material, 0) >= quantity:
            #if enough stock, reduce the quantity from the stock
            stock[material] = stock[material] - quantity
            #increase the number of the products processed by the operator
            self.products_processed = self.products_processed + quantity
            print(f"{self.name} processed {quantity} units of {material}. Total processed: {self.products_processed}")
        else:
            print(f"{self.name}: Not enough stock for {material}. Notify the Manager.")


class Manager(Employee):
    def __init__(self, name, age, hire_date, salary, specialization, competence_level, team_size):
        """
        Initializes a Manager object, which is a type of Employee
        :param name:
        :param age:
        :param hire_date:
        :param salary:
        :param specialization:
        :param competence_level:
        :param team_size:
        """
        super().__init__(name, age, "Manager", hire_date, salary, specialization, competence_level)
        self.team_size = team_size


    def display_employees(self, file_path):
        """
        Display the list of employees from a CSV file
        :param file_path:
        """
        #Read employees from csv file
        employees_df = pd.read_csv(file_path)
        print(f"Employees list:")
        print(employees_df[['Name', 'Age', 'Role','Hire Date', 'Salary', 'Specialization', 'Competence Level']])


    def remove_employees(self, employees, name, file_path):
        """
        Removes an employee from the list based on their name
        :param employees:
        :param name:
        :param file_path:
        :return: The updated DataFrame with the employee removed
        """
        #Filter the employee with the specified name from DataFrame
        updated_employees = employees[employees['Name'] != name]
        #Check if the number of the rows in the original DataFrame is the same as the filtered one
        #If no rows were removed, it means no employee, with the give name was found
        if len(employees) == len(updated_employees):
            print(f"No employee found with the name: {name}")
        else:
            print(f"Employee {name} has been removed")
            #Update the csv file with updated list of employees
            write_csv_file(updated_employees, file_path) #update de csv file after remove
        return updated_employees


class StockKeeper(Employee):
    def __init__(self, name, age, salary, hire_date, specialization, competence_level):
        """
        Initializes a StockKeeper object, which is a type of Employee
        :param name:
        :param age:
        :param salary:
        :param hire_date:
        :param specialization:
        :param competence_level:
        :param stock:
        """
        super().__init__(name, age, "StockKeeper", salary, hire_date, specialization, competence_level)

        self.stock = "path ul spre csv ul lui cristi"


    def display_stock(self):
        """
        Displays the stock managed by the stockKeeper
        """
        print(f"Stock managed by {self.name}:")
        #Loop through each material and quantity in the stock dictionary
        for material, quantity in self.stock.items(): # to-do iter_rows
            print(f"{material}: {quantity} units")


    def update_stock(self, material, quantity):
        """
        Updates the stock of a specific material
        :param material:
        :param quantity:
        """
        #Check if the material exist in stock
        if material in self.stock:
            #If quantity is positive, add to the existing stock
            if quantity > 0:
                self.stock[material] = self.stock[material] + quantity
                print(f"Stock updated: {material} +{quantity} units. New quantity: {self.stock[material]} units")
            #If quantity is negative, reduce the stock, but not below zero
            elif quantity < 0:
                if self.stock[material] + quantity >= 0: #Ensure the stock doesn't go negative
                    self.stock[material] =  self.stock[material] + quantity
                    print(f"Stock updated: {material} -{abs(quantity)} units. New quantity: {self.stock[material]} units")
                else:
                   #If trying to reduce more than available, print an error message
                    print(f"Error: Not enough stock of {material} to reduce by {abs(quantity)} units.")
            else:
                #If the material does not exist in the stock, add it with the given quantity
                self.stock[material] = quantity
                print(f"New material {material} added to stock with {quantity} units.")

if __name__ == "__main__":
    file_path = "employees.csv"
    employees_df = pd.read_csv(file_path)
    #print("Initial Employee List:")
    #print(employees_df[['Name','Role']].to_string(index=False)) #Display without index
    #manager = Manager("Bob J.",54,"10/10/2010",5500,"Performance Monitoring","Advanced",19)
    # employees_df = manager.remove_employees(employees_df, "Bob J.", file_path)
    manager1 = Manager("Eve Y.",59,"20/06/2005",3500,"Biscuit Production","Intermediate",31)
    employees_df = manager1.remove_employees(employees_df, "Charlie U.", file_path)
    #print(employees_df)
    manager1.display_employees(file_path)
    # stock = {"White chocolate":100, "Caramel":40}
    # operator = Operator("Alice Q.",29,"26/06/2023",3000,"Quality Control","Advanced",17)
    # operator.process_material("Caramel", 30, stock)
    # print(f"Noul stock este {stock}")
    # operator.process_material("Caramel", 20, stock)

