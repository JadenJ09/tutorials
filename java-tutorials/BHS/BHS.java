import java . util . ArrayDeque ; 
import java . util . Queue ; 
import java . util . Stack ; 

public class BHS {
    private Stack<String> specialBaggageStorage = new Stack<>();
    private Stack<String> temporaryStorage = new Stack<>();
    private Queue<String> conveyorBelt = new ArrayDeque<>();

    public void checkInBaggage(String barcode) {
        conveyorBelt.add(barcode);
        System.out.println("Bag " + barcode + " is placed on the conveyor belt");
    }

    public void removeBaggage(String barcode) {
        String firstBaggage = conveyorBelt.poll();
        String currentHead = firstBaggage;
        boolean cycleCompleted = false;
        boolean found = false;

        while (!found && !cycleCompleted) {
            if (currentHead.equals(barcode)) {
                System.out.println("Bag " + barcode + " is removed from conveyor belt");
                found = true;
            } else {
                conveyorBelt.add(currentHead);
                System.out.println("Bag " + currentHead + " went all around the conveyor belt");
                currentHead = conveyorBelt.poll();

                if (currentHead.equals(firstBaggage)) {
                    conveyorBelt.add(currentHead);
                    cycleCompleted = true;
                }
            }
        }

        if (!found) {
            System.out.println("Bag " + barcode + " is lost");
        }
    }

    public void checkInSpecialBaggage(String barcode) {
        specialBaggageStorage.push(barcode);
        System.out.println("Bag " + barcode + " is stored in the storage room");
    }

    public void removeSpecialBaggage(String barcode) {
        boolean found = false;

        while (!found && !specialBaggageStorage.isEmpty()) {
            String currentHead = specialBaggageStorage.pop();

            if (currentHead.equals(barcode)) {
                System.out.println("Bag " + barcode + " is removed from storage room");
                found = true;
            } else {
                temporaryStorage.push(currentHead);
                System.out.println("Bag " + currentHead + " stored in the temporary storage room");
            }
        }

        if (!found) {
            System.out.println("Bag " + barcode + " is lost");
        }

        while (!temporaryStorage.isEmpty()) {
            String currentHead = temporaryStorage.pop();
            specialBaggageStorage.push(currentHead);
            System.out.println("Bag " + currentHead + " stored back in the storage room");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        BHS bhs = new BHS();

        bhs.checkInBaggage("001000");
        bhs.checkInBaggage("001001");
        bhs.checkInBaggage("001010");
        bhs.checkInBaggage("001011");

        bhs.checkInSpecialBaggage("101000");
        bhs.checkInSpecialBaggage("101001");
        bhs.checkInSpecialBaggage("101010");
        bhs.checkInSpecialBaggage("101011");

        bhs.removeBaggage("001010");
        bhs.removeBaggage("001111");

        bhs.removeSpecialBaggage("101010");
        bhs.removeSpecialBaggage("101111");
    }
}
