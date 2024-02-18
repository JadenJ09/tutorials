class CheckingAccount extends BankAccount {
    public CheckingAccount(double balance) {
      super(balance);
    }
  
    @Override
    public void printBalance() {
      System.out.println("Your checking account balance is $" + balance);
    }
  
    public void checkBalances() {
      // calls method from CheckingAccount
      printBalance();
      // calls method from BankAccount
      super.printBalance();
    }
  
    public static void main(String[] args) {
      CheckingAccount myCheckings = new CheckingAccount(5000);
      myCheckings.checkBalances();
    }
  }
  