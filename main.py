from package_andreea.classEmployee import *
from package_cristi.class_stock import *
from package_marina.CLass_Products import *
from some_functions_integration import *

if __name__ == "__main__":

    stock_file_path = 'package_cristi/stock.csv'
    employees_file_path = "package_andreea/employees.csv"
    products_file_path = "package_marina/products.csv"

    stock = Stock(stock_file_path)  # create an object for stock

    manager = Manager("Marina M", 25, "01/08/2000", 8000, "Resource Allocation", "Expert", 10)
    operator = Operator("Andreea B", 23, "01/08/2003", 3000, "IDK", "Expert", 0)
    stockKeeper = StockKeeper("Cristian P", 23, 2000, "01/08/2003", "Safety", "Expert", stock)

    while True:
        print("\n===== MENU =====")
        print("1. Angajeaza un nou personal")
        print("2. Exclude un angajat")
        print("3. Afiseaza angajatii")
        print("4. Produce un produs")
        print("5. Creeaza un produs nou")
        print("6. Elimina un produs")
        print("7. Afișeaza stocul")
        print("8. Adauga materii prime")
        print("0. Iesire")
        choice = input("Alege numarul unei optiuni: ")

        if choice == "1":#TODO DONE
            manager.add_employees(employees_file_path)

        elif choice == "2":#TODO DONE
            manager.remove_employees(employees_file_path)

        elif choice == "3":#TODO DONE
            manager.display_employees(employees_file_path)

        elif choice == "4":#TODO
            Product.file_products(products_file_path)
            Product.show_list_of_products()

            product_name = input("Introduceti numele produsului pe care doriti sa-l produceti: ").strip()
            ingredients_list = get_ingredients_for_product(product_name, products_file_path)
            print(f"Lista cu ingrediente pentru produsul : {product_name}     =>    {ingredients_list}")

            if not ingredients_list:
                print(f"Produsul '{product_name}' nu a fost gasit sau nu are ingrediente valide.")
                continue

            if stock.verify_product_details(product_name, ingredients_list):

                print(f"Materia primă este suficientă. Producem {product_name}...")
                for ingredient_dict in ingredients_list:
                    ingredient_name = list(ingredient_dict.keys())[0]
                    quantity_needed = list(ingredient_dict.values())[0]
                    stock.decrease_stock(ingredient_name, quantity_needed)
                stock.add_product_in_stock(product_name, 1)
                print(f"Produsul '{product_name}' a fost creat cu succes!")
            else:
                print(f"Materia prima este insuficientă pentru a produce {product_name}. Aprovizionam stocul...")
                stockKeeper.supply_ingredients(
                    [(list(ing.keys())[0], list(ing.values())[0]) for ing in ingredients_list])

                # Optiunea 4. Dam comanda de produse din fabrica: Se va face in display la produsele pe care fabrica le produce(Doar numele) ( (METODA PENTRU CLASA PRODUCT)
                    # Userul plaseaza o comanda pentru un produs :
                        #2 cazuri posibile: 4.1 Avem materia prima necesara, 4.2 Nu avem materie prima necesara



                    #4.1 Daca avem materie prima necesara vom produce produsul (METODA PENTRU CLASA OPERATOR), eliminand din stock materia prima consumata.
                    # Pentru clasa stock va fi:
                                                    # o metoda ce va verifica cantitatile necesare producerii produsului, va returna T/F verify_product_details(name_prod,list_ingredients,stock)
                                                    # o metoda ce va adauga un produs FINIT in stock cu cantitatea lui add_product_in_stock(name_product, quantity)


                    #4.2 Daca nu avem materia prima necesara magazinerul trebuie sa aprovizioneze stockul cu materia prima necesara + o valoare semnificativa (METODA PENTRU CLASA MAGAZINER)
                            # o metoda in clasa stock ce va adauga materie prima add_ingredient_in_stock(name_ingredient,quantity)


        elif choice == "5": # TODO: la reteta trebuie adaugata cantitatea fiecarui element
            # Optiunea 5. Creeam un produs nou. Avem input Denumirea si lista de dictionare ce reprezinta reteta produsului
            # Produsul va fi scris in fiserul csv corespunzator.
            Product.add_product(products_file_path)

        elif choice == "6":#TODO nu se gaseste produsul ca sa-l sterg
            Product.delete_product(products_file_path)
            # Optiunea 6. Elimina produs. (Pe langa ce are Marina de facut, in clasa package_cristi ai nevoie de o metoda ce
            # va avea ca parametrii denumirea produsului si va sterge din stock toata linia produsului.)

        elif choice == "7":#TODO DONE
            # Optiunea 7. Afisam stock. Metoda de display este in clasa stock dar este apelata prin magaziner.
            stockKeeper.show_stock()

        #Optiunea 8. Aceeasi metoda ca la 4.2 dar separat de momentul adaugarii.
        # # o metoda in clasa stock ce va adauga materie prima add_ingredient_in_stock(name_ingredient,quantity)
        elif choice == "8":
            pass
        elif choice == "0":
            break









