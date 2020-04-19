import java.util.ArrayList;
import java.util.Scanner;
//import java.util.io.*;
import java.util.Random;
import java.util.List;

class RockPaperScissor {

    private Input userInput;
    private Input computerInput;
    private Output userOutput;
    private Config config;
    private ErrorLevel errorLevel = ErrorLevel.WARNING;
    private ErrorLog errorLog;
    private String className = "RockPaperScissor";

    public void setErrorLevel(ErrorLevel errorLevel) {
        this.errorLevel = errorLevel;
    }

    public void setUserInput(Input inputType){
        userInput = inputType;
    }

    public void setUserOutput(Output outputType){
        userOutput = outputType;
    }

    public void setComputerInput(Input inputType){
        computerInput = inputType;
    }

    RockPaperScissor(){

        userInput = new ConsoleInput();
        userOutput = new ConsoleOutput();
        computerInput = new RandInput();
        config = new ConfigFromFile();
        errorLog = ErrorLog.getInstance();

    }

    private void writeError(String method, String message, ErrorLevel errorLevel){

        errorLog.writeMessage(className,method, message,errorLevel, this.errorLevel);
    }

    public static String generateRequest(String[] weapons){
        String display = "Please select";
        /*for (int i=0;i<weapons.length;i++){*/
        int i=0;
        for (String weapon: weapons){
            display += " " + i + " " + weapon;
            i++;
        };
        return display;
    }

    private int requestPlay(String[] weapons)
    {
        String request;
        request = generateRequest(weapons);
        userOutput.output(request);

        int userWeapon = userInput.getInputInt();
        if (userWeapon > 23){
            writeError("requestPlay","userWeapon greater than 3", ErrorLevel.ERROR );
        }

        return userWeapon;
    }



    public static String determineWinner(String[] weaponList, int userWeapon, int computerWeapon)
    {
        String winner;
        if (userWeapon == computerWeapon)
        {
            winner = "Draw both selected " + weaponList[computerWeapon];
        }
        else if ((userWeapon + 1) % 3 == computerWeapon)
        {
            winner = "You win and beat the computer's " + weaponList[computerWeapon];
        }
        else if ((computerWeapon + 1) % 3 == userWeapon)
        {
            winner = "Computer wins with " + weaponList[computerWeapon];
        }
        else {
            winner = "Please select 1. Rock, 2. Scissors or 3. Paper";
        }

        return winner;

    }

    private void displayWinner(String winner)
    {
        userOutput.output(winner);
    }

    public void playGame(String[] weaponList){
        int userWeapon;

        int computerWeapon;
        String winner;
        //Final declares
        userWeapon = requestPlay(weaponList);
        do{
            computerWeapon = computerInput.getInputInt();
            winner = determineWinner(weaponList, userWeapon, computerWeapon);
            displayWinner(winner);
            userWeapon = requestPlay(weaponList);
        } while (userWeapon< weaponList.length);

    }

    public void run(){
        //Final declares
        List<String> listOfGames = config.getConfig();
        String request = getGamesRequest(listOfGames);
        this.userOutput.output(request);
        int userGame = this.userInput.getInputInt();
        while (userGame < listOfGames.size())
        {
            String[] weaponlist = listOfGames.get(userGame).split(":")[1].split(",");
            playGame(weaponlist);
            this.userOutput.output(request);
            userGame = this.userInput.getInputInt();
        } ;
    }

    private String getGamesRequest(List<String> listOfGames){
        String request = "Please select";
        for (int counter = 1; counter < listOfGames.size(); counter++){
            request += " " + String.valueOf(counter) + " - " + listOfGames.get(counter).split(":")[0];
        }
        return request;
    }

    public static void main(String[ ] args) {
        RockPaperScissor rockPaperScissor = new RockPaperScissor();
        rockPaperScissor.run();
    }
}
