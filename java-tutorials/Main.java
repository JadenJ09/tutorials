import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        CashRegister cashRegister = new CashRegister();
        cashRegister.addDiscountedItem("Coffee");

        Stack<Item> cart1 = new Stack<>();
        cart1.push(new Item("Milk", 1.0));
        cart1.push(new Item("Bread", 2.5));

        Stack<Item> cart2 = new Stack<>();
        cart2.push(new Item("Oranges", 2.0));
        cart2.push(new Item("Coffee", 4.0));

        cashRegister.loadItems(cart1);
        cashRegister.placeDivider();
        cashRegister.loadItems(cart2);

        cashRegister.serveClient();
        cashRegister.serveClient();
    }
}
