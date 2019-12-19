def main():
    
    user_choice = ""
    while user_choice != "3":
        print_menu()
        user_choice = input("Val: ")
        if user_choice == "1":
            pass
        elif user_choice == "2":
            pass
        elif user_choice == "3":
            print("Hejdå")
            continue
        else: 
            print("Nu skrev du in något knasigt")

def print_menu():
    print("="*40)
    print("Meny")
    print("="*40)
    print("Val:")
    print("1) Bingo")
    print("2) Stats")
    print("3) Avsluta")
