import json

def main():
    
    user_choice = ""
    while user_choice != "4":
        print_menu()
        user_choice = input("Val: ")
        if user_choice == "1":
            show_result()
        elif user_choice == "2":
            add_player()
        elif user_choice == "3":
            remove_player()
        elif user_choice == "4":
            print("Hejdå")
            continue
        else: 
            print("Nu skrev du in något knasigt")

def print_menu():
    print("="*40)
    print("Meny")
    print("="*40)
    print("Val:")
    print("1) Visa resultat")
    print("2) Registrera nytt resultat")
    print("3) Radera resultat")
    print("4) Avsluta")

def show_result():
    '''
    Skapar listor med sorterade resultat och printar dessa listor bereoende på vilken sortering användaren vill ha
    '''
    try:
        my_file = open("points.json", "r")

        #skapar lista med alla spelare och poäng (originalordning)
        points = json.loads(my_file.read())
        
        print("\nHur vill du sortera?")
        print("1) Namn")
        print("2) Varv 1")
        print("3) Varv 2")      
        print("4) Varv 3")
        print("5) Totalt")
        print("6) Orignal")
    
        while True:
            sortering_val = input("Val (1-6): ")
            if sortering_val.isdigit():
                if int(sortering_val) in range(1,7):
                    break
                else:
                    print("Du måste skriva ett val mellan 1-6")
            else:
                print("Du måste skriva in en siffra")

        if sortering_val != "6":
            print("\nVill du sortera fallande eller stigande? ")
            print("1) Fallande ")
            print("2) Stigande ")
            while True:
                reverse_val = input("Val (1 eller 2): ")
                if reverse_val.isdigit():
                    if int(reverse_val) in range(1,3):
                        break
                    else:
                        print("Du måste skriva in 1 eller 2")
                else:
                    print("Du måste skriva in en siffra")
        
        #skapar sorterade listor på given key
        sort_by_name = sorted(points, key=lambda k: k["namn"]) 
        sort_by_varv1 = sorted(points, key=lambda k: k["varv1"])
        sort_by_varv2 = sorted(points, key=lambda k: k["varv2"])
        sort_by_varv3 = sorted(points, key=lambda k: k["varv3"])
        sort_by_totalen = sorted(points, key=lambda k: k["totalen"])
        #skapar listor fast reversed
        sort_by_name_reversed = sorted(points, key=lambda k: k["namn"], reverse = True) 
        sort_by_varv1_reversed = sorted(points, key=lambda k: k["varv1"], reverse = True)
        sort_by_varv2_reversed = sorted(points, key=lambda k: k["varv2"], reverse = True)
        sort_by_varv3_reversed = sorted(points, key=lambda k: k["varv3"], reverse = True)
        sort_by_totalen_reversed = sorted(points, key=lambda k: k["totalen"], reverse = True)

        if sortering_val == "6":
            print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
            for player in points:
                print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        elif sortering_val == "1":
            if reverse_val == "2":
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_name:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
            else:
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_name_reversed:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        elif sortering_val == "2":
            if reverse_val == "2":
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_varv1:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
            else:
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_varv1_reversed:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        elif sortering_val == "3":
            if reverse_val == "2":
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_varv2:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
            else:
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_varv2_reversed:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        elif sortering_val == "4":
            if reverse_val == "2":
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_varv3:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
            else:
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_varv3_reversed:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        elif sortering_val == "5":
            if reverse_val == "2":
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_totalen:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
            else:
                print("\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
                for player in sort_by_totalen_reversed:
                    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["totalen"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        my_file.close()

    except FileNotFoundError:
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Filen finns inte, prova igen så ska det nog gå!")

    except (json.decoder.JSONDecodeError, TypeError):
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Nu var något knasigt med strukturen i filen, prova igen")
    #Helgarderar mig nedan :)
    except:
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Oj! Något katastrofalt har hänt.... prova igen, funkar det inte då... då är det kört......")

def add_player():
    try:
        my_file = open("points.json", "r")
        players = json.loads(my_file.read())
        new_player = ({
            "namn": input("\nNamn: ").capitalize(), #alla namn måste ha första bokstaven stor, annars funkar inte sortering på namn
            "varv1": int(input("Varv 1: ")),
            "varv2": int(input("Varv 2: ")),
            "varv3": int(input("Varv 3: ")),
        })

        #lägger till totalpoängen i lexikonet
        new_player["totalen"] = new_player["varv1"] + new_player["varv2"] + new_player["varv3"] 
        #lägger till det nya lexikonet i listan med tillsammans med alla andra spelare
        players.append(new_player)
        my_file.close()

        #skriver över den gamla listan, med den nya uppdaterade
        my_file = open("points.json", "w")
        my_file.write(json.dumps(players, indent = 4))
        my_file.close()

    except ValueError:
        #kollar så att man skriver in siffror (man kan inte ha bokstäver eller andra tecken som resultat)
        print("Du måste skriva in siffror i 'Varv' inputen")
    except FileNotFoundError:
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Filen hittades inte! Men prova igen så ska det nog gå bättre.")
    except (json.decoder.JSONDecodeError, TypeError):
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Nu var något knasigt med strukturen i filen, prova igen")
    #Helgarderar mig nedan :)
    except:
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Oj! Något katastrofalt har hänt.... prova igen, funkar det inte då... då är det kört......")


def remove_player():
    '''
    Tar bort spelare ur listan
    '''
    try:
        my_file = open("points.json", "r")
        players = json.loads(my_file.read())

        which_player = input("\nVilken spelare vill du ta bort? " ).lower()
        players_not_removed = []
        players_removed = 0
        #kollar om which_player finns i spelar-listan.
        for player in players:
            if which_player != player["namn"].lower():
                players_not_removed.append(player)
            else:
                print("{} har tagits bort!".format(player["namn"]))
                players_removed += 1
        
        if players_removed == 0:
            print("Inga spelare med det namnet!")
        my_file.close()

        my_file = open("points.json", "w")
        my_file.write(json.dumps(players_not_removed, indent = 4))
        my_file.close()

    except FileNotFoundError:
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Filen hittades inte! Men prova igen så ska det nog gå bättre.")
    except (json.decoder.JSONDecodeError, TypeError):
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Nu var något knasigt med strukturen i filen, prova igen")
    #Helgarderar mig nedan :)
    except:
        my_file = open("points.json","w")
        my_file.write(json.dumps([]))
        my_file.close()
        print("Oj! Något katastrofalt har hänt.... prova igen, funkar det inte då... då är det kört......")

main()  