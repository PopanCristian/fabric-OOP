from package_andreea import *
if __name__ == "__main__":

        # Step 1 : by default creeam cate un angajat din fiecare tip
        # Step 2 : Se va deschide meniul cu optiuni.


                # Optiunea 1. Angajeaza un nou personal (METODA PENTRU CLASA MANAGER)
                    # Se va cere Name,Age,Role,Hire Date,Salary,Specialization,Competence Level,Products_Processed
                    # EX : Introduceti datele pentru noul angajat ( 1.cu , intre ele informatii
#                                                                   2. sa fie un numar exact de informatii necesare)
#                                                                   : Popan Cristian , 22, Operator etc
                    # Se creeaza obiectul dupa care se va scrie in csv


                # Optiunea 2. Exclude un angajat din fabric(il dam afara) (METODA PENTRU CLASA MANAGER): din fisierul csv se va sterge linia corespunzatoare angajatului

                # Optiunea 3. Display employees (METODA PENTRU CLASA MANAGER)

                # Optiunea 4. Dam comanda de produse din fabrica: Se va face in display la produsele pe care fabrica le produce(Doar numele) ( (METODA PENTRU CLASA PRODUCT)
                    # Userul plaseaza o comanda pentru un produs :
                        #2 cazuri posibile: 4.1 Avem materia prima necesara, 4.2 Nu avem materie prima necesara



                    #4.1 Daca avem materie prima necesara vom produce produsul (METODA PENTRU CLASA OPERATOR), eliminand din stock materia prima consumata.
                    # Pentru clasa stock va fi:
                                                    # o metoda ce va verifica cantitatile necesare producerii produsului, va returna T/F verify_product_details(name_prod,list_ingredients,stock)
                                                    # o metoda ce va adauga un produs FINIT in stock cu cantitatea lui add_product_in_stock(name_product, quantity)


                    #4.2 Daca nu avem materia prima necesara magazinerul trebuie sa aprovizioneze stockul cu materia prima necesara + o valoare semnificativa (METODA PENTRU CLASA MAGAZINER)
                            # o metoda in clasa stock ce va adauga materie prima add_ingredient_in_stock(name_ingredient,quantity)

                # Optiunea 5. Creeam un produs nou. Avem input Denumirea si lista de dictionare ce reprezinta reteta produsului
                    #Produsul va fi scris in fiserul csv corespunzator.

                #Optiunea 6. Elimina produs. (Pe langa ce are Marina de facut, in clasa package_cristi ai nevoie de o metoda ce
                    # va avea ca parametrii denumirea produsului si va sterge din stock toata linia produsului.)

                #Optiunea 7. Afisam stock. Metoda de display este in clasa stock dar este apelata prin magaziner.

                #Optiunea 8. Aceeasi metoda ca la 4.2 dar separat de momentul adaugarii.
                    # # o metoda in clasa stock ce va adauga materie prima add_ingredient_in_stock(name_ingredient,quantity)











