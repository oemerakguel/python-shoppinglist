shoppinglist = []
item = None

def add_item(item):
        shoppinglist.append(item)
        print(f"'{item}' wurde zur Einkauflsite hinzugefügt.")
    

def show_shoppinglist():
    if shoppinglist == ['']:
        print("Deine Einkaufsliste ist leer")
    else:
        print("Deine Einkaufsliste:")
        for index, item in enumerate(shoppinglist, start=1):

            print(f"{item}")

def main():
    while True:
        print("-----Einkaufsliste-----")
        print("1. Artikel zur Einkaufslsite hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")

        choice = input("Was möchten Sie tun ? ")

        if choice == "1":
            item = input("Bitte gib ein Artikel ein, der zur Einkaufsliste hinzugeügt werden soll:")
            add_item(item)
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen")
            exit()
        elif not choice == "1" or choice == "2" or choice == "3":
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")

if __name__ == "__main__":
    main()