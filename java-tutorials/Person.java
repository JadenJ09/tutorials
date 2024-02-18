public class Person {
    private String firstName;

    public void setFirstName(String fname) {
        this.firstName = fname;
    }

    public String getFirstName() {
        return firstName;
    }
    
    public static void main(String[] args) {
        Person person = new Person();
        person.setFirstName("John");
        System.out.println("The person's first name is: " + person.getFirstName());
    }
}
