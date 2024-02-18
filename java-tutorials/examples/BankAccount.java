class BankAccount {
    protected double balance;
  
    public BankAccount(double balanceIn){
      balance = balanceIn;
    }
  
    public void printBalance() {
      System.out.println("Your account balance is $" + balance);
    }
  }