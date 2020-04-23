using System;
using System.Collections.Generic;
using System.Web;
using System.Xml;
using System.IO;
using System.Text;
using HtmlAgilityPack;

namespace ConsoleApp1
{
    class LoadPrices
    {
        private string stockUrl = @"https://finance.yahoo.com/screener/predefined/day_gainers";
        private string localUrl = @"C:\Users\Derek\Downloads\Top Stock Gainers Today - Yahoo Finance.html";
        private Boolean inTest = false;
        private HtmlDocument localWebDocument = null;

        public void setInTest(Boolean inTest)
        {
            this.inTest = inTest;
        }

        private List<string> ScrapeToday()
        {
            List<string> priceEntries = new List<string>(); 
            try
            {
                
                HtmlNode stockTable = GetStockTable();
                foreach (HtmlNode node in stockTable.SelectNodes("tr"))
                {
                    priceEntries.Add(RipRow(node));
                }
                
            }
            catch (Exception ex)
            {
                Console.WriteLine("Help" + ex.Message);
            }
            return priceEntries;
        }

        public string RipRow(HtmlNode row)
        {
            
            string name = row.SelectSingleNode("td[@aria-label = 'Name']").InnerText.Trim();
            string symbol = row.SelectSingleNode("td[@aria-label = 'Symbol']").InnerText.Trim();
            string price = row.SelectSingleNode("td[@aria-label = 'Change']").InnerText.Trim();
            string changeValue = row.SelectSingleNode("td[@aria-label = '% Change']").InnerText.Trim();
            string changePercenatge = row.SelectSingleNode("td[@aria-label = 'Price (Intraday)']").InnerText.Trim();
            return name + "," + symbol + "," + price + "," + changeValue + "," + changePercenatge;
        }

        private HtmlDocument getHtmlDocumentFromWeb()
        {
            var webGet = new HtmlWeb();
            HtmlDocument webDocument = null;
            if (this.inTest)
            {
                Console.WriteLine("In Test");
                if (this.localWebDocument == null)
                {
                    Console.WriteLine("Set localWebDocument");
                    this.localWebDocument = webGet.Load(localUrl);
                } else
                {
                    Console.WriteLine("Use the localWebDocument");
                }
                webDocument = this.localWebDocument;
            }
            else
            {
                Console.WriteLine("Not in test, load from stockUrl");
                webDocument = webGet.Load(stockUrl);
            }
            return webDocument;
        }

        private HtmlNode GetStockTable()
        {

            HtmlDocument webDocument = getHtmlDocumentFromWeb();
            var stockTable = webDocument.DocumentNode.SelectSingleNode("//tbody");
            return stockTable;
        }

        private void displayStockTable(List<string> priceEntries)
        {
            foreach (string priceEntry in priceEntries)
            {
                Console.WriteLine(priceEntry);
            }
        }

        
        static void Main(string[] args)
        {
            Console.WriteLine("Start Load");
            long lastWatchTime;
            long initialWatchTime;
            var watch = new System.Diagnostics.Stopwatch();
            LoadPrices loadPrices = new LoadPrices();
            watch.Start();
            List<string> priceEntries = loadPrices.ScrapeToday();
            watch.Stop();

            Console.WriteLine($"Initial Load from web Execution Time: {watch.ElapsedMilliseconds} ms");
            lastWatchTime = watch.ElapsedMilliseconds;
            initialWatchTime = lastWatchTime;
            watch.Start();
            priceEntries = loadPrices.ScrapeToday();
            watch.Stop();
            Console.WriteLine($"Second Test Setup Execution Time: {watch.ElapsedMilliseconds - lastWatchTime} ms");
            lastWatchTime = watch.ElapsedMilliseconds;
            loadPrices.setInTest(true);
            watch.Start();
            priceEntries = loadPrices.ScrapeToday();
            watch.Stop();
            Console.WriteLine($"Initial Test Setup Execution Time: {watch.ElapsedMilliseconds - lastWatchTime} ms");
            Console.WriteLine($"Number of times faster: {initialWatchTime / (watch.ElapsedMilliseconds - lastWatchTime)}");
            lastWatchTime = watch.ElapsedMilliseconds;
            watch.Start();
            priceEntries = loadPrices.ScrapeToday();
            watch.Stop();
            Console.WriteLine($"Second Test Run Execution Time: {watch.ElapsedMilliseconds - lastWatchTime} ms");
            Console.WriteLine($"Number of times faster: {initialWatchTime / (watch.ElapsedMilliseconds - lastWatchTime)}");
            loadPrices.displayStockTable(priceEntries);
        }
    }
}
