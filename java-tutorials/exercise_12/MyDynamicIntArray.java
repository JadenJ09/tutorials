import java . util . Arrays ;

public class MyDynamicIntArray { // do not use reallocate method

    private int[] a;
    private int size;

    public MyDynamicIntArray(int initialCapacity) {
        a = new int[initialCapacity];
        size = 0;
    }

    public void add(int value) {
        if (size == a.length) { // more space needed
            reallocate(a.length * 2); // double the size
        }
        a[size++] = value; // add the value and increment the size
    }

    private void reallocate(int newCapacity) { // split the add method for clarification
        int[] b = new int[newCapacity];
        System.arraycopy(a, 0, b, 0, size);
        a = b;
    }

    public void merge(MyDynamicIntArray other) {
        int newSize = size + other.size;
        // Find the new capacity which is the smallest power of 2 >= newSize
        int newCapacity = findNextPowerOfTwo(newSize);
        
        if (newCapacity > a.length) {
            reallocate(newCapacity);
        }
        
        int[] result = new int[newCapacity];
        int j = 0; // Index for the original array 'a'
        int k = 0; // Index for the 'other' array
        int i = 0; // Index for the new 'result' array

        while (j < size || k < other.size) {
            if (j < size) {
                result[i++] = a[j++];
            }
            if (k < other.size) {
                result[i++] = other.a[k++];
            }
        }

        a = result;
        size = newSize;
    }

    private int findNextPowerOfTwo(int value) {
        int power = 1;
        while (power < value) {
            power *= 2;
        }
        return power;
    }

    // Additional methods (size, get) for completeness
    public int size() {
        return size;
    }

    public int get(int i) {
        if (i >= size || i < 0) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Size: " + size);
        }
        return a[i];
    }
}