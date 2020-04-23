using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace StonkTracker.Engine
{
    public class Entry
    {
        public string CompanyName { get; set; }
        public string Symbol { get; set; }
        public string ChangeValue { get; set; }
        public string ChangePercentage { get; set; }
        public string Price { get; set; }
        public string Desc { get; set; }

        public Entry(string companyName, string symbol, string price, string changeValue, string changePercentage)
        {
            CompanyName = companyName;
            Symbol = symbol;
            Price = price;
            ChangeValue = changeValue;
            ChangePercentage = changePercentage;
        }
    }
}

