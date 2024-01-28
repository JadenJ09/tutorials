### Supermarket's Cash

Implement a system simulating a supermarket. In the supermarket, customers can buy items identified
by their names. The customers place their items in a shopping cart, piling them up. This means that
only the item on top of the cart is accessible. Once the item on top is removed, the next one becomes
accessible, and so on. The cash register is equipped with a conveyor belt, on which the clients place
the items from their carts to pay for them. After emptying their cart, clients put a divider on the
conveyor belt to avoid mixing up their items with those of the client behind them. The cashier serves a
client by scanning all items until the divider is reached, and then issues the bill with the total amount.
At the cash register, there is also a catalog of items on a 50% discount. The discount is applied when
the item is scanned.

Shopping cart: Stack sequence
Conveyor belt: Queue sequence

The shopping cart, the conveyor belt, and the catalog of discounted items are sequences. The text of
the assignment does not specify which class you should use to implement them. For each sequence,
choose whether to implement it as a Stack , Queue, or LinkedList. For each of these, you are only
allowed to use the methods described in the section “Data Structures for Sequences” above.