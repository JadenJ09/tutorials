import java.util.ArrayList;

class PrimeDirective {
  
  // Check if a number is prime
  public boolean isPrime(int number) {
    if (number < 2) {
      return false;
    }
    for (int i = 2; i < number; i++) {
      if (number % i == 0) {
        return false;
      }
    }
    return true;
  }
  
  // Return an ArrayList of all primes found in an array
  public ArrayList<Integer> onlyPrimes(int[] numbers) {
    ArrayList<Integer> primes = new ArrayList<Integer>();
    for (int number : numbers) {
      if (isPrime(number)) {
        primes.add(number);
      }
    }
    return primes;
  }
  
  public static void main(String[] args) {
    PrimeDirective pd = new PrimeDirective();
    int[] numbers = {6, 29, 28, 33, 11, 100, 101, 43, 89};

    // Test the onlyPrimes method
    System.out.println("Prime numbers: " + pd.onlyPrimes(numbers));

    // // Iterate through the array of numbers: Working without the onlyPrimes method
    // for (int j = 0; j < numbers.length; j++) {
    //     // Print each number and whether it is prime
    //     System.out.println(numbers[j] + ": " + pd.isPrime(numbers[j]));
  }  
}
