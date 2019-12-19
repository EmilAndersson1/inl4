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
    try:
        #öppnar filen
        my_file = open("points.json", "r")
        #konverterar JSON
        points = json.loads(my_file.read())

        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Namn", "Varv 1", "Varv 2", "Varv 3", "Totalt", "Genomsnitt"))
        for player in points:
            print("{:<8} {:<8} {:<8} {:<8} {:<8} {:.1f}".format(player["namn"], player["varv1"], player["varv2"], player["varv3"], player["varv1"] + player["varv2"] + player["varv3"], (player["varv1"] + player["varv2"] + player["varv3"])/3 ))
        
        my_file.close()
    except FileNotFoundError:
        print("Filen finns inte, synd.")


def add_player():
    my_file = open("points.json", "r")
    players = json.loads(my_file.read())
    try:
        new_player = ({
            "namn": input("Namn: "),
            "varv1": int(input("Varv 1: ")),
            "varv2": int(input("Varv 2: ")),
            "varv3": int(input("Varv 3: "))
        })
        players.append(new_player)
        my_file.close()
    except ValueError:
        print("Du måste skriva in siffror i 'Varv' inputen")
    

    my_file = open("points.json", "w")
    my_file.write(json.dumps(players))
    my_file.close()


def remove_player():

    my_file = open("points.json", "r")
    players = json.loads(my_file.read())

    which_player = input("Vilken spelare vill du ta bort?" ).lower()

    for player in players:
        if which_player in player["namn"].lower():
            print("{} har tagits bort!".format(player["namn"]))
            players.remove(player)
    my_file.close()

    my_file = open("points.json", "w")
    my_file.write(json.dumps(players))
    my_file.close()



main()  