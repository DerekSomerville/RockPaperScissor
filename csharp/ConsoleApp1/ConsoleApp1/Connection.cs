using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Globalization;
using System.Linq;
using System.Web;

namespace StonkTracker.Engine
{
    public class Connection
    {
        private static string connStr = "Server=GA1;Database=Stonks;Trusted_Connection=True";

        public static DataSet GetEntries(DateTime date)
        {
            using (SqlConnection conn = new SqlConnection())
            {
                conn.ConnectionString = connStr;

                DataSet ds = new DataSet("Entries");
                conn.Open();

                SqlCommand command = new SqlCommand("[dbo].[loadEntries]", conn);
                command.Parameters.Add("@Date", SqlDbType.Date).Value = date;
                command.CommandType = CommandType.StoredProcedure;

                SqlDataAdapter da = new SqlDataAdapter
                { SelectCommand = command };
                da.Fill(ds);
                conn.Close();
                TearDown(da);
                return ds;
            }
        }

        public static void SaveEntries(List<Entry> entries)
        {
            DateTime todaysDate = DateTime.Today;
            foreach (Entry entry in entries)
            {
                SaveEntry(entry, todaysDate);
            }
        }

        private static void SaveEntry(Entry entry, DateTime date)
        {
            using (SqlConnection sqlConn = new SqlConnection(connStr))
            {
                using (SqlCommand sqlComm = new SqlCommand())
                {
                    sqlComm.Connection = sqlConn;
                    sqlComm.CommandType = System.Data.CommandType.StoredProcedure;
                    sqlComm.CommandText = "[dbo].[saveEntries]";
                    sqlComm.Parameters.Add("@CompanyName", SqlDbType.VarChar).Value = entry.CompanyName;
                    sqlComm.Parameters.Add("@Symbol", SqlDbType.VarChar).Value = entry.Symbol;
                    sqlComm.Parameters.Add("@Price", SqlDbType.VarChar).Value = entry.Price;
                    sqlComm.Parameters.Add("@ChangeValue", SqlDbType.VarChar).Value = entry.ChangeValue;
                    sqlComm.Parameters.Add("@ChangePercentage", SqlDbType.VarChar).Value = entry.ChangePercentage;
                    sqlComm.Parameters.Add("@Desc", SqlDbType.VarChar).Value = entry.Desc;
                    sqlComm.Parameters.Add("@Date", SqlDbType.Date).Value = date;

                    sqlConn.Open();
                    sqlComm.ExecuteNonQuery();
                }
            }
        }

        private static void TearDown(SqlDataAdapter da = null)
        {
            if (da != null) { da.Dispose(); }
        }



    }
}
