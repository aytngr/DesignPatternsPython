from nypizzastore import NYPizzaStore
from chigagopizzastore import ChigagoPizzaStore

ny_store = NYPizzaStore()
ch_store=ChigagoPizzaStore()

order1=ny_store.order_pizza("cheese")
order2=ch_store.order_pizza("veggie")

print(f"Order 1 : {order1.name}")
print(f"Order 2 : {order2.name}")