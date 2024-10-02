shoppinglist = []

def add_item(item):
    shoppinglist.append(item)
    print(f"'{item}' wurde zur Einkauflsite hinzugefügt.")

item = input("Bitte gib ein Artikel ein, der zur Einkaufsliste hinzugeügt werden soll:")
add_item(item)

def show_shoppinglist():
    if shoppinglist == ['']:
        print("Deine Einkaufsliste ist leer")
    else:
        print("Deine Einkaufsliste:")
        for index, item in enumerate(shoppinglist, start=1):
            print(f"{item}")

show_shoppinglist()