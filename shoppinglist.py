shoppinglist = []

def add_item(item):
    shoppinglist.append(item)
    print(f"'{item}' wurde zur Einkauflsite hinzugefügt.")

item = input("Bitte gib ein Artikel ein, der zur Einkaufsliste hinzugeügt werden soll:")
add_item(item)

print(shoppinglist)