public class Bicycle {

    // Instance variables
    int gear;
    int speed;

    // Constructor
    public Bicycle(int gear, int speed) {
        this.gear = gear;
        this.speed = speed;
    }

    // Method to increase speed
    public void speedUp(int increment) {
        speed += increment;
    }

    public static void main(String[] args) {
        // Creating an object using the constructor
        Bicycle myBike = new Bicycle(3, 10);

        // Calling a method on the object
        myBike.speedUp(5);
        
        System.out.println("Gear: " + myBike.gear + " Speed: " + myBike.speed);
    }
}
