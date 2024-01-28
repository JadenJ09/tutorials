import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class CashRegister {
    private Queue<Item> conveyorBelt = new ArrayDeque<Item>();
    private List<String> discountCatalog = new LinkedList<>();

    public void addDiscountedItem(String itemName) {
        discountCatalog.add(itemName);
    }

    public void placeDivider() {
        conveyorBelt.add(new Item("", 0)); // Divider
    }

    public void loadItems(Stack<Item> cart) {
        while (!cart.isEmpty()) {
            conveyorBelt.add(cart.pop());
        }
    }

    public void serveClient() {
        double total = 0;
        while (!conveyorBelt.isEmpty() && !conveyorBelt.peek().isDivider()) {
            Item item = conveyorBelt.poll();
            double price = item.getPrice();
            if (discountCatalog.contains(item.getName())) {
                price /= 2; // 50% discount
                System.out.println(item.getName() + ": " + price + " (50% off)");
            } else {
                System.out.println(item.getName() + ": " + price);
            }
            total += price;
        }
        if (!conveyorBelt.isEmpty() && conveyorBelt.peek().isDivider()) {
            conveyorBelt.poll(); // Remove divider
        }
        System.out.println("Total: " + total);
        System.out.println();
    }
}
