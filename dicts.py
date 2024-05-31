def  create_inventory(item):
    inventario = dict()
    for i in item:
        if i not in inventario:
            inventario[i]=item.count(i)
    return(inventario)

def add_items(inventory, items):
    inventario2 =create_inventory(items)
    for i in inventory:
        if i in inventario2:
            inventory[i]= inventory[i] + inventario2[i]
            del inventario2[i]
    for i in inventario2:
        if i not in inventory:
            inventory[i]=inventario2[i]
    return inventory

def decrement_items(inventory, items):
    inventario2 = create_inventory(items)
    for i in inventory:
        if i in inventario2:
            if inventario2[i] > inventory[i]:
                inventory[1]=0
            else:
                inventory[i]= inventory[i] - inventario2[i]
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    lista = list()
    for material in inventory:
        if inventory[material] > 0:
            lista.append((material,inventory(material)))
    return lista
