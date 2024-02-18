public class Continents {
  
    public static void main(String[] args) {
      // This program prints out a major city in a continent based on the continent's number.
      
      int continent = 4; // Continent number
  
      switch (continent) {
        case 1:
          System.out.println("North America: Mexico City, Mexico");
          break; // Exits the switch statement
  
        case 2:
          System.out.println("South America: Sao Paulo, Brazil");
          break; // Exits the switch statement
  
        case 3:
          System.out.println("Europe: Moscow, Russia");
          break; // Exits the switch statement
  
        case 4:
          System.out.println("Africa: Lagos, Nigeria");
          break; // This is the expected case based on the value of continent
  
        case 5:
          System.out.println("Asia: Shanghai, China");
          break; // Exits the switch statement
  
        case 6:
          System.out.println("Australia: Sydney, Australia");
          break; // Exits the switch statement
  
        case 7:
          System.out.println("Antarctica: McMurdo Station, US");
          break; // Exits the switch statement
  
        default:
          System.out.println("Undefined continent!");
          break; // Exits the switch statement
      }
    }
  }
  