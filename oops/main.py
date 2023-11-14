from item import Item


item = Item("GX", 500, 3)
item.apply_increment(0.2)
item.apply_discount()

print(item.price)

