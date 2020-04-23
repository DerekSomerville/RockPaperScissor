using System;
using System.Collections.Generic;
using System.Data;
using System.Globalization;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.Web.UI.WebControls;

namespace StonkTracker
{
    public partial class _Default : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            PopulateGrid();
        }

        private void PopulateGrid()
        {
            DateTime selector;
            if (DateTime.Now.Hour > 17 && DateTime.Now.Minute > 2) { selector = DateTime.Today.Date; }
            else { selector = DateTime.Today.AddDays(-1).Date; }
            DataSet ds = Connection.GetEntries(selector);

            if (ds.Tables[0].Rows.Count == 0)
            {
                StonkDataTable.Visible = false;
                NoStockDataMsg.Visible = true;
            }
            else
            {
                StonkDataTable.Visible = true;
                NoStockDataMsg.Visible = false;
            }

            HtmlTableRow tableRow;
            foreach (DataRow row in ds.Tables[0].Rows)
            {
                tableRow = new HtmlTableRow();

                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<DateTime>("Date").ToShortDateString() });
                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<string>("CompanyName") });
                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<string>("Symbol") });
                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<string>("Price") });
                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<string>("ChangeValue") });
                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<string>("ChangePercentage") });
                tableRow.Cells.Add(new HtmlTableCell { InnerText = row.Field<string>("Desc") });

                StonkDataTable.Rows.Add(tableRow);
            }
        }
    }
}
