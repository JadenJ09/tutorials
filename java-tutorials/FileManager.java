import java.io.*;

public class FileManager {

    public static String readFile(String fname) {
        StringBuilder contentBuilder = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(fname))) {
            String currentLine;
            while ((currentLine = br.readLine()) != null) {
                contentBuilder.append(currentLine).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return contentBuilder.toString();
    }
    
    public static void main(String[] args) {
        String fileContent = FileManager.readFile("example.txt");
        System.out.println(fileContent);
    }
}
