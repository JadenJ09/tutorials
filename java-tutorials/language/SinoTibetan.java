class SinoTibetan extends Language {
    SinoTibetan(String languageName, int speakers) {
      super(languageName, speakers, "Asia", "subject-object-verb");
      if (languageName.contains("Chinese")) {
        this.wordOrder = "subject-verb-object";
      }
    }
  
    @Override
    public void getInfo() {
  
      System.out.println(this.name + " is spoken by " + this.numSpeakers + " people mainly in " + this.regionsSpoken + ".");
      System.out.println("The language follows the word order: " + this.wordOrder);
  
    }
    
  }