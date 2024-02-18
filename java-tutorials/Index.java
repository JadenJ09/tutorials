

public class Index {

    public static void main (String[] args) {
        String line = "The Heav'ns and all the Constellations rung";

        int startIndex = line.indexOf("Constellations");

        // Add length of "Constellations" and 1 for the space to get the next word's start index
        int nextWordStart = startIndex + "Constellations".length() + 1;

        // Assuming you don't know the next word's length, find the next space
        int nextWordEnd = line.indexOf(" ", nextWordStart);
        if (nextWordEnd == -1) { // No more spaces, so we are at the last word
            nextWordEnd = line.length();
        }

        // Now extract the word
        String nextWord = line.substring(nextWordStart, nextWordEnd);
        System.out.println(nextWord); // This would print the word following "Constellations"

    }
}