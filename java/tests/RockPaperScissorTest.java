import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.*;

public class RockPaperScissorTest {

    RockPaperScissor rock = new RockPaperScissor();
    TestOutput testOutput = new TestOutput();
    TestInput testInput = new TestInput();
    TestInput computerInput = new TestInput();


    final String[] weaponList = {"Rock","Scissors","Paper"};


    private ArrayList<String>  setUpTest(ArrayList<String> userInputs, ArrayList<String> computerInputs){
        testOutput.clear();
        testInput.setTestInputs(userInputs);
        computerInput.setTestInputs(computerInputs);
        rock.setUserOutput(testOutput);
        rock.setUserInput(testInput);
        rock.setComputerInput(computerInput);
        return testOutput.getTestOutputs();
    }

    @Test
    public void testGenerateRequest() {
        String result = rock.generateRequest(weaponList);
        assertEquals("Please select 0 Rock 1 Scissors 2 Paper", result);
    }


    @Test
    public void testDetermineWinner() {
        String result = rock.determineWinner(weaponList,0,0);
        assertEquals("Draw both selected Rock", result);
    }

    @Test
    public void testRockVsRock() {
        ArrayList<String> userInputs = new ArrayList<String>(2);
        userInputs.add("0");
        userInputs.add("4");
        ArrayList<String> computerInputs = new ArrayList<>(1);
        computerInputs.add("0");
        ArrayList<String> userOutput = setUpTest(userInputs,computerInputs);

        rock.run();
        String result = userOutput.remove(1);
        assertEquals("Draw both selected Rock", result);
    }
}