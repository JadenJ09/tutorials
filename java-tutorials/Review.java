import java.util.Arrays;

public class Review {
    public static void main(String[] args) {
        // Initialize a 4x3 2D array with the first exam scores and -1 for others
        double[][] scores = {
            {80.4, -1, -1},
            {96.2, -1, -1},
            {100.0, -1, -1},
            {78.9, -1, -1}
        };

        System.out.println("Initial scores: " + Arrays.deepToString(scores));

        // Updating scores for the second exam
        scores[0][1] = 89.7;
        scores[1][1] = 90.5;
        scores[2][1] = 93.6;
        scores[3][1] = 88.1;

        System.out.println("Updated scores with second exam: " + Arrays.deepToString(scores));
        
        // Initialize a new 4x2 2D array for two exams
        double[][] newScores = new double[4][2];
        
        // Copy scores of the first two exams into the new 2D array
        for (int i = 0; i < scores.length; i++) {
            for (int j = 0; j < 2; j++) { // Only copying first two exams
                newScores[i][j] = scores[i][j];
            }
        }

        System.out.println("Scores after copying to newScores: " + Arrays.deepToString(newScores));
        
        // Add 2 points to any exam score less than 90 in newScores
        for (int i = 0; i < newScores.length; i++) {
            for (int j = 0; j < newScores[i].length; j++) {
                if (newScores[i][j] < 90) {
                    newScores[i][j] += 2; // Add 2 points
                }
            }
        }

        System.out.println("Final newScores after extra credit: " + Arrays.deepToString(newScores));
    }
}
