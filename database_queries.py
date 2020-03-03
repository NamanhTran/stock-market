import mysql.connector

db = mysql.connector.connect(host = "",
                             user = "",
                            passwd = "",
                            database = "STOCK_TRADER")
                            
mycursor = db.cursor()

username = /*Needs to get username from the html, not sure how to implement*/

/*selects the rows in STOCK where the userID matches the username, will return the stockid, how many shares and its price*/
mycursor.execute("SELECT stockID, quantity, market_value 
                 FROM STOCK
                 WHERE userID = "%s"
                 ORDER BY stockID ASC", username)
                 
