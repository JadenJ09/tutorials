public class DNA {
  
    /*  
    Write a DNA.java program that determines whether there is a protein in a strand of DNA.
    
    A protein has the following qualities:
    1. It begins with a “start codon”: ATG.
    2. It ends with a “stop codon”: TGA.
    3. In between, each additional codon is a sequence of three nucleotides.
    */
    
      public static void main (String[] args) {
        String dna1 = "ATGCGATACGCTTGA";
        String dna2 = "ATGCGATACGTGA";
        String dna3 = "ATTAATATGTACTGA";
        String[] dna = {dna1, dna2, dna3};
    
        // Loop should start from 0 and go till dna.length to cover all elements
        for (int i = 0; i < dna.length; i++) {
          System.out.println("");
          System.out.println("Length of DNA strand " + (i+1) + ": " + dna[i].length());
    
          int start = dna[i].indexOf("ATG");
          System.out.println("Start: " + start);
    
          int stop = dna[i].indexOf("TGA");
          System.out.println("Stop: " + stop);
    
          if (start != -1 && stop != -1 && (stop - start) % 3 == 0) {
            System.out.println("Condition 1, 2, and 3 are satisfied.");
            String protein = dna[i].substring(start, stop + 3); // Corrected to use dna[i]
            System.out.println("Protein: " + protein);
          } else {
            System.out.println("No protein.");
          }
        }
      }
    }