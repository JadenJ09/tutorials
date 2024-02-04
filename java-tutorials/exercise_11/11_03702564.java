
import java.util.Stack;

class recursiveFunctions { 
    // Homework 11.1: A recursive function to calculate the powers of 3
    public static int powerOfThree(int n) {
        if (n == 0) {
            return 1;
        } else {
            return 3 * powerOfThree(n - 1);
        }
    }

    // Homework 11.2: A recursive function to count the occurrences of a number in a stack
    public static int countOccurrences(Stack<Integer> s, int n) {
        if (s.isEmpty()) {
            return 0;
        } else {
            int top = s.pop(); // Remove the top element from the stack
            int count = countOccurrences(s, n); // Recursively count the occurrences of n in the stack
            if (top == n) {
                count++;
            }
            s.push(top); // Restore the stack to its original state
            return count;
        }
    }

    // Homework 11.3: A recursive function to check if there is a range of numbers that sum to a given number
    public static boolean func(int x, int y, int z) {
        if (x > y) {
            return func(y, x, z); // Ensure x is always less than or equal to y
        }
        return sumInRange(x, y) == z;
    }

    private static int sumInRange(int x, int y) {
        if (x == y) {
            return x;
        } else {
            return x + sumInRange(x + 1, y); // Sum the range from x to y
        }
    }

    public static void main(String[] args) {
        // Running Homework 11.1
        System.out.println("Power of Three (3): " + powerOfThree(3)); // 27

        // Running Homework 11.2
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(2);
        System.out.println("Count Occurrences of 2: " + countOccurrences(stack, 2)); // 2

        // Running Homework 11.3
        System.out.println("func(3,6,18): " + func(3, 6, 18)); // true
        System.out.println("func(6,3,18): " + func(6, 3, 18)); // true
        System.out.println("func(6,6,6): " + func(6, 6, 6)); // true
    }
}
