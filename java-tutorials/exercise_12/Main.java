import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        MyDynamicIntArray arr1 = new MyDynamicIntArray(4);
        arr1.add(1);
        arr1.add(2);
        arr1.add(3);
        System.out.println(arr1.size());


        MyDynamicIntArray arr2 = new MyDynamicIntArray(2);
        arr2.add(10);
        arr2.add(11);
        System.out.println(arr2.size());


        arr1.merge(arr2);
        for (int i = 0; i < arr1.size(); i++) {
            System.out.print(arr1.get(i) + " ");
        }
    }
}