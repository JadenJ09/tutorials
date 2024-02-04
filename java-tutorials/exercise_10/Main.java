import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        CashRegister cashRegister = new CashRegister(); // create a new instance of CashRegister class
        cashRegister.addDiscountedItem("Coffee"); // add "Coffee" to the discount catalog

        Stack<Item> cart1 = new Stack<>(); // create a new instance of Stack<Item> class as cart1
        cart1.push(new Item("Milk", 1.0)); // add "Milk" to the cart1
        cart1.push(new Item("Bread", 2.5)); // add "Bread" to the cart1

        Stack<Item> cart2 = new Stack<>(); // create a new instance of Stack<Item> class as cart2
        cart2.push(new Item("Oranges", 2.0)); // add "Oranges" to the cart2
        cart2.push(new Item("Coffee", 4.0)); // add "Coffee" to the cart2

        cashRegister.loadItems(cart1); // load items from the cart1 to the conveyor belt
        cashRegister.placeDivider(); // place a divider on the conveyor belt
        cashRegister.loadItems(cart2); // load items from the cart2 to the conveyor belt

        cashRegister.serveClient(); // call serveClient() method
        cashRegister.serveClient(); // call serveClient() method again
    }
}
