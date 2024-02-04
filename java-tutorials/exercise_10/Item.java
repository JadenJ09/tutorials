public class Item {
    private String name; // a private attribute
    private double price; // a private attribute

    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    } // a public constructor

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public boolean isDivider() {
        return name.isEmpty();
    } // a public method which returns a boolean value as true if the name of the item is empty and false otherwise
}
