public class SomeClass {

    public int someAttribute;
    public int someOtherAttribute;

    public SomeClass(int initialValue){
        System.out.println("first constructor called");
        someAttribute = initialValue;
    }

    public SomeClass(int initialValue, int initialValueOther){
        System.out.println("second constructor called");
        someAttribute = initialValue;
        someOtherAttribute = initialValueOther;
        }

    public static void main(String[] args) {
        SomeClass someObject = new SomeClass(7);
        int x = someObject.someAttribute;
        System.out.println(x);
        int y = someObject.someOtherAttribute;
        System.out.println(y); // prints 0 because it was not initialized
        }

}

