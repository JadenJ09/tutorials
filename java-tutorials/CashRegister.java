import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class CashRegister {
    private Queue<Item> conveyorBelt = new ArrayDeque<Item>(); // a private attribute with a type of Queue<Item>
    private List<String> discountCatalog = new LinkedList<>(); // a private attribute with a type of List<String>

    public void addDiscountedItem(String itemName) {
        discountCatalog.add(itemName);
    } // a public method which adds the name of the item to the discount catalog

    public void placeDivider() {
        conveyorBelt.add(new Item("", 0)); // Divider
    } // a public method which adds a divider to the conveyor belt

    public void loadItems(Stack<Item> cart) {
        while (!cart.isEmpty()) {
            conveyorBelt.add(cart.pop());
        }
    } // a public method which loads items from the cart to the conveyor belt

    public void serveClient() {
        double total = 0;
        while (!conveyorBelt.isEmpty() && !conveyorBelt.peek().isDivider()) {
            Item item = conveyorBelt.poll();
            double price = item.getPrice();
            if (discountCatalog.contains(item.getName())) {
                price /= 2; // 50% discount
                System.out.println(item.getName() + ": € " + price + " (50% off)"); // print item name, price and discount
            } else {
                System.out.println(item.getName() + ": € " + price);
            }
            total += price; // increase total by each item's price
        }
        if (!conveyorBelt.isEmpty() && conveyorBelt.peek().isDivider()) {
            conveyorBelt.poll(); // Remove divider
        }
        System.out.println("Total: € " + total); // print total price
        System.out.println();
    }
}
