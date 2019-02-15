inventario = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventario):
    item_total = 0
    print('Inventory:')
    for k, v in inventario.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inv, itens):
    for i in itens:
        if i in inv:
            inv[i] += 1
        else:
            inv.setdefault(i, 1)
    return inv

novoInventario = addToInventory(inventario, dragonLoot)
displayInventory(novoInventario)

    
