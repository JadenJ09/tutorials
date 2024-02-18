public class Dog{
    public String name;
    public int age;
  
    public Dog(String input_name, int input_age){
      name = input_name;
      age = input_age;
    }
      
    public void speak() {
      System.out.println("Arf Arf! My name is " + name + " and I am a good dog!");
    }

    public static void main (String[] args) {
      Dog dog1 = new Dog("Rover", 5);
      Dog dog2 = new Dog("Spot", 3);
      Dog dog3 = new Dog("Spike", 7);
      Dog[] dogs = {dog1, dog2, dog3};
  
      for (int i = 0; i < dogs.length; i++) {
        dogs[i].speak();
      }
    }
  }
  