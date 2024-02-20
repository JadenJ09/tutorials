import java.util.Arrays;
public class Combining {
    public static void main(String[] args) {
        int[][] imageData = {
            {100, 90, 255, 80, 70, 255, 60, 50},
            {255, 10, 5, 255, 10, 5, 255, 255},
            {255, 255, 255, 0, 255, 255, 255, 75},
            {255, 60, 30, 0, 30, 60, 255, 255}
        };
        
        // Initialize a new 2D array with 4 rows and 6 columns
        int[][] newImage = new int[4][6];
        
        // Copying the data, excluding the right 2 columns
        for (int i = 0; i < newImage.length; i++) { // Loop through each row
            for (int j = 0; j < newImage[i].length; j++) { // Loop through each column in the row
                newImage[i][j] = imageData[i][j];
            }
        }
        
        System.out.println("Cropped Image: " + Arrays.deepToString(newImage));
        
        // Decreasing the brightness by 50 units
        for (int i = 0; i < newImage.length; i++) {
            for (int j = 0; j < newImage[i].length; j++) {
                newImage[i][j] = newImage[i][j] - 50;
                if (newImage[i][j] < 0) { // Ensure pixel value doesn't go below 0
                    newImage[i][j] = 0;
                }
            }
        }
        
        System.out.println("Adjusted Brightness: " + Arrays.deepToString(newImage));
    }
}