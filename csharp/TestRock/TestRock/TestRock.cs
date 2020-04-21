using Microsoft.VisualStudio.TestTools.UnitTesting;


namespace TestRock
{
    [TestClass]
    public class TestRock
    {
        [TestMethod]
        public void testGenerateGamesRequest()
        {
            Rock rock = new Rock();
            rock.setConfig(new ConfigFromStubb());
            string result = rock.generateGamesListRequest();
            Assert.AreEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result);
        }
    }
}
