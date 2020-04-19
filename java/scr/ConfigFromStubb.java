import java.util.ArrayList;
import java.util.List;

public class ConfigFromStubb implements Config{
    public List<String> getConfig(){
        List<String> propertyData = new ArrayList<String>();
        propertyData.add("Name:First,Second,Third");
        propertyData.add("Rock Paper Scissors:Rock,Scissors,Paper");
        propertyData.add("Star Wars:Darth Vadar,Emperor,Luke Skywalker");
        return propertyData;
    }
}
