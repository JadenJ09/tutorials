import java.util.ArrayList;

class Playlist {
  
  public static void main(String[] args) {
    ArrayList<String> desertIslandPlaylist = new ArrayList<String>();
    ArrayList<String> tempA = new ArrayList<String>();

    desertIslandPlaylist.add("3D");
    desertIslandPlaylist.add("4D");
    desertIslandPlaylist.add("5D");
    desertIslandPlaylist.add("6D");
    desertIslandPlaylist.add("7D");

    tempA.add("a");
    desertIslandPlaylist.set(0, "9D");
    desertIslandPlaylist.set(1, tempA.get(0));

    System.out.println(desertIslandPlaylist);
    System.out.println(desertIslandPlaylist.size());
    System.out.println(desertIslandPlaylist.indexOf("6D") + 1);
  }
  
}