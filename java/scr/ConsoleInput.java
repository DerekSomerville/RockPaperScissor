import java.util.Scanner;

public class ConsoleInput implements Input{
    private Scanner userInput = new Scanner(System.in);
    public String getInputString(){
        String result = userInput.nextLine();
        return result;
    }
    public int getInputInt(){
        int result = userInput.nextInt();
        return result;
    }
}
