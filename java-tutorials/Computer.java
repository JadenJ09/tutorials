public class Computer{
    public int brightness;
    public int volume;
    
    public void setBrightness(int inputBrightness){
      this.brightness = inputBrightness;
    }
  
    public void setVolume(int inputVolume){
      this.volume = inputVolume;
    }
  
    public void resetSettings(){
      this.setBrightness(0);
      this.setVolume(0);
    }

    public static void main(String[] args){
      Computer myComputer = new Computer();
      myComputer.setBrightness(100);
      myComputer.setVolume(50);
      System.out.println("Brightness: " + myComputer.brightness);
      System.out.println("Volume: " + myComputer.volume);
      myComputer.resetSettings();
      System.out.println("Reset Settings: ");
      System.out.println("Brightness: " + myComputer.brightness);
      System.out.println("Volume: " + myComputer.volume);
    }
  }
  