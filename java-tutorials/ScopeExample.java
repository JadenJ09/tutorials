public class ScopeExample{
    public static void main(String[] args){
    // public int sum = 0; // This line will cause an error because public is not allowed here. 
    // The reason is that public is an access modifier that is used to define the access level of the method. It is not allowed to use public access modifier inside a method.
      int sum = 0;
      int[] myArray = {1, 2, 3, 4};
      for(int i = 0; i < myArray.length; i++){
        
        sum += myArray[i];
      }
  
      System.out.println(sum);
    }
  }