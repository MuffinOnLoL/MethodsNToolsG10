import mysql.connector



#Connects SQL webserver through XAMPP to access database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "MethodsNTools_G10"
)


#Use cursor to navigate SQL table
mycursor = mydb.cursor()


#SELECT query to concatenate SQL table into list of tuples to be accessed throughout program (fetchall)
mycursor.execute("SELECT * FROM accounts")
userExist = mycursor.fetchall()



#intialize User class using init method
class User:
    def _init_(self, customerID, firstName, lastName, userName, passWd, shippingInfo, paymentInfo):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.passWd = passWd
        self.shippingInfo = shippingInfo
        self.paymentInfo = paymentInfo



    #create logIn function to validate info with SQL table and move on to next menu using SELECT
    def logIn(self):
        mycursor.execute("SELECT * FROM accounts")
        userExist = mycursor.fetchall()
        while True:
            self.userName = str(input("\nPLease enter your username: "))

            for i in userExist:
                if (i[3] != self.userName):
                    continue
                
                else:
                    while True:

                        self.passWd = str(input("\nPlease enter your password: "))


                        for i in userExist:
                            if (i[4] != self.passWd):
                                continue

                            else:
                                print("\nSuccessfully logged in!")
                                return

                        print("\nERROR: That password is incorrect. Please try again.\n")
            print("\nERROR: That username does not exist. Please try again.\n")
        


    #create Register function to initialize new row in SQL table using INSERT
    #A bunch of nested loops to prevent empty input
    def Register(self):
        while True:
            self.userName = str(input("\nPlease enter a username: "))

            for i in userExist:
                if (i[3] == self.userName):
                    print("\nERROR: That username already exists. Please enter a different one.")
                    break

                elif self.userName == "":
                    print("\nERROR: You must enter a username. Please try again\n")
                    break

                else:
                    while True:

                        self.passWd = str(input("\nPlease enter a password: "))

                        for i in userExist:
                            if (i[4] == self.passWd):
                                print("\nERROR: That password already exists. Please enter a different one.")
                                break

                            elif self.passWd == "":
                                print("\nERROR: You must enter a password. Please try again\n")
                                break

                            else:
                                while True:
                                    self.firstName = str(input("\nWhat is your first name? "))

                                    if self.firstName == "":
                                        print("\nERROR: You must enter a name. Please try again\n")
                                
                                    else:
                                        while True:
                                            self.lastName = str(input("\nWhat is your last name? "))

                                            if self.lastName == "":
                                                print("\nERROR: You must enter a name. Please try again\n")

                                            else:
                                                while True:
                                                    self.shippingInfo = str(input("\nWhat is your shipping address? "))

                                                    if self.shippingInfo == "":
                                                        print("\nERROR: You must enter an address. Please try again\n")

                                                    else:
                                                        while True:
                                                            self.paymentInfo = str(input("\nWhat is your six-digit payment number? "))

                                                            if self.paymentInfo == "":
                                                                print("\nERROR: You must enter a payment number. Please try again\n")

                                                            else:
                                                            
                                                                #Final instructions, ensures ID number is new and unique
                                                                ind = len(userExist)

                                                                self.customerID = str(userExist[ind - 1][0] + 1)

                                                                #String concatenated insert query
                                                                sql = "INSERT INTO accounts (customerID, firstName, lastName, userName, passWd, shippingInfo, paymentInfo) VALUES ('" + self.customerID + "', '" + self.firstName + "', '" + self.lastName + "', '" + self.userName + "', '" + self.passWd + "', '" + self.shippingInfo + "', '" + self.paymentInfo + "')"


                                                                mycursor.execute(sql)

                                                                mydb.commit()

                                                                print("\n\nAccount successfully created!\n")

                                                                return
    
    #Function to edit accounts shipping info column using UPDATE
    def editShippingInfo(self):
        newShip = str(input("\nWhat would you like your new address to be? "))

        for i in userExist:
            if i[5] == newShip:
                print("\nNo changes needed. Returning to menu.\n")

            else:
                sql = "UPDATE accounts SET shippingInfo='" + newShip + "' WHERE userName='" + self.userName + "'"

                mycursor.execute(sql)
                mydb.commit()

                print("\nSuccessfully changed your shipping information!\n")
                
                return

                

    #Function to edit accounts payment info column using UPDATE
    def editPaymentInfo(self):
        newPay = int(input("\nWhat would you like your new six-digit payment number to be? "))

        for i in userExist:
            if i[6] == newPay:
                print("\nNo changes needed. Returning to menu.\n")

            else:
                sql = "UPDATE accounts SET shippingInfo='" + str(newPay) + "' WHERE userName='" + self.userName + "'"

                mycursor.execute(sql)
                mydb.commit()

                print("\nSuccessfully changed your payment information!\n")

                return



    def viewAccountInfo(self):
        mycursor.execute("SELECT * FROM accounts WHERE userName='" + self.userName + "'")

        viewAcc = mycursor.fetchall()

        for i in viewAcc:
            print("\nCustomer ID: " + str(i[0]))
            print("First Name: " + str(i[1]))
            print("Last Name: " + str(i[2]))
            print("Username: " + str(i[3]))
            print("Password: " + str(i[4]))
            print("Shipping Info: " + str(i[5]))
            print("Payment Info: " + str(i[6]) + "\n")
            return


    #Function to delete account information from SQL table using DELETE
    #Spits user back to main menu instead of exiting
    def deleteAccount(self):
        while True:

            #double confirmation message to prevent unnecessary deleting

            userConf_1 = str(input("\nAre you sure you want to delete your account? (y/n) "))
        
            if userConf_1 == 'n':
                print("\nPhew! That was close!\n")
                return
        
            elif userConf_1 == 'y':
                while True:

                    userConf_2 = str(input("\nARE YOU SURE? (y/n) "))

                    if userConf_2 == 'n':
                        print("\nPhew! That was close!\n")
                        return

                    elif (userConf_2 == 'y'):

                        accDel = "DELETE FROM accounts WHERE userName = '" + self.userName +"'"

                        mycursor.execute(accDel)

                        mydb.commit()

                        print("\n\nGood-bye! We're sad to see you go!\n")
                        return

                    else:
                        print("\nERROR: That is not a valid selection. Please try again\n")

            else:
                print("\nERROR: That is not a valid selection. Please try again\n")

#^^^^ Prevention of invalid selection. Loops to ease frustration

         

            

#Initializing some classes that will be updated

class shoppingCart:

    def _init_(self, item, quantity, userName):
        self.item = item
        self.quantity = quantity
        self.userName = userName


    def addToCart(self):
        self.userName = str(input("\nPlease enter your username: "))
        self.item = str(input("\nItem Name: "))
        self.quantity = str(input("\nAmount Wanted: "))
        sql = "INSERT INTO cart (ItemName, ItemQuantity, CustomerID) VALUES ('" + self.item + "', '" + self.quantity + "', '" + self.userName + "')"      
        mycursor.execute(sql)

        mydb.commit()


    def removeFromCart(self):
        self.userName = str(input("\nPlease enter your username: "))
        sql = "DELETE FROM cart WHERE CustomerID = " + "'" + self.userName + "'"

        mycursor.execute(sql)
        mydb.commit()

    def viewCart(self):

        self.userName = str(input("\nPlease enter your username: "))
        sql = "SELECT ItemName, ItemQuantity FROM cart WHERE customerID = " + "'" + self.userName + "'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("\n" + "Qty: " + str(x[1]) + "\t" + str(x[0]))



class orderHistory:
    def _init_(self, userName, purchased, shippingInfo, paymentInfo):
        self.userName = userName
        self.purchased = purchased
        self.shippingInfo = shippingInfo
        self.paymentInfo = paymentInfo


    #Displays the user's purchasing history as well as related information
    def viewOrderHistory(self):
        sql = "SELECT * from orders"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print("\nUsername\tItem Purchased\t\tShipping Information\t\tPayment Information\n")
        for x in myresult:
            print(str(x[0]) + "\t\t" + str(x[1]) + "\t\t\t" + str(x[2]) + "\t\t\t" + str(x[3]))


    #Adds a purchased order to the given user's ordering history for later view
    def addToOrderHistory(self):
        self.userName = str(input("\nPlease enter your username: "))
        self.purchased = str(input("\nItem Purchased: "))
        self.shippingInfo = str(input("\nShipping Information: "))
        self.paymentInfo = str(input("\nPayment Information: "))
        sql = "INSERT INTO orders (userName, PastPurchases, ShippingInfo, PaymentInfo) VALUES ('" + self.userName + "', '" + self.purchased + "', '" + self.shippingInfo + "', '" + self.paymentInfo + "')"
        mycursor.execute(sql)
        mydb.commit()
        print("\nSuccessfully added purchase to history!\n")

    def removeFromOrderHistory(self):
        self.userName = str(input("\nPlease enter your username: "))
        mycursor.execute("DELETE FROM orders WHERE userName='" + self.userName + "'")
        mydb.commit()


class inventory:
    def _init_(self, item, price, stock):
        self.item = item
        self.price = price
        self.stock = stock


    def addToInventory(self):
        self.item = str(input("\nItem Name: "))
        self.price = str(input("\nList Price: "))
        self.stock = str(input("\nStock Available: "))
        sql = "INSERT INTO inventory (Name, Price, Amount) VALUES ('" + self.item + "', '" + self.price + "', '" + self.stock + "')"
        mycursor.execute(sql)

    def removeFromInventory(self):
        self.item = str(input("\nItem you want to purchase: "))
        sql = "SELECT * FROM inventory"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        itemFound = False
        for row in records:
            if (row[0] == self.item):
                stockString = row[2]

                stockInt = int(stockString)
                stockInt = stockInt - 1
                stockString = str(stockInt)

                sql = "UPDATE inventory SET Amount='" + stockString + "' WHERE Name='" + self.item + "'"
                mycursor.execute(sql)
                mydb.commit()

                itemFound = True

        if (itemFound == False):
            print("\nItem does not exist.")

            #print("Name = ", row[0], )
            #print("Price = ", row[1])
            #print("Amount  = ", row[2], "\n")

    def viewInventory(self):

        sql = "SELECT * FROM inventory"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print("\n")
        for x in myresult:
            print("Qty: " + str(x[2]) + "\t" + str(x[0]) + "\t$" + str(x[1]))

        return



#Main function that initializes class instances


def main():
    u = User()
    c = shoppingCart()
    t = inventory()
    o = orderHistory()

    print("\nWelcome to the E-Commerce Store!")
    print("Version 1.0.0 by Group 10\n")

    print("\nPlease login or create an account to get started.")

    while True:
        print("\n\n0. Exit the program\n")
        print("1. Log in to an existing account\n")
        print("2. Create an account\n")

        menuSel = int(input("\nPlease make a selection: "))

        if menuSel == 0:
            raise SystemExit(0)
            #exit program

        elif menuSel == 1:

            #calls login, if returned then move to next menu, create account illusion
            
            u.logIn()

            loggedIn = True

            while loggedIn:
                print("\n\n0. Exit the program\n")
                print("1. Browse our inventory\n")
                print("2. View your cart\n")
                print("3. View order history\n")
                print("4. View or edit account information\n")
                print("5. Delete your account\n")
                print("6. Logout\n")

                menuSel = int(input("\nPlease make a selection: "))

                if menuSel == 0:
                    raise SystemExit(0)

                elif menuSel == 1:
                    inventoryMenu = True
                    t.viewInventory()
                    while inventoryMenu:

                        print("\n1. Add to cart")
                        print("2. Refresh inventory")
                        print("3. Return to Main Menu")

                        inventorySel = int(input("\nPlease make a selection: "))

                        if inventorySel == 1:
                            c.addToCart()
                            t.removeFromInventory()
                            print("\nItem was successfully added!\n")

                        elif inventorySel == 2:
                            t.viewInventory()
                        elif inventorySel == 3:
                            inventoryMenu = False

                        elif inventorySel == '':
                            print("\nERROR: That was not a correct selection.")
                        else:
                            print("\nERROR: That was not a correct selection.")


                elif menuSel == 2:
                    cartMenu = True
                    c.viewCart()
                    while cartMenu:
                        print("\n1. Check out.")
                        print("2. Remove an item from the cart.")
                        print("3. Return to Main Menu.")

                        cartSel = int(input("\nPlease make a selection: "))

                        if cartSel == 1:
                            o.addToOrderHistory()
                            c.removeFromCart()

                            print("\nThank you for shopping with us!")
                            break

                        elif cartSel == 2:
                            c.removeFromCart()
                            c.viewCart()

                        elif cartSel == 3:
                            cartMenu = False
                        elif cartSel == 4:
                            c.addToCart()
                            c.viewCart()
                        else:
                            print("\nERROR: That was not a correct selection.")

                elif menuSel == 3:
                    o.viewOrderHistory()


                #Decided to include editing of account info in one branch of menu, keep logged menu simple
                elif menuSel == 4:
                    while True:
                        u.viewAccountInfo()
                        print("\n1. Edit shipping information\n")
                        print("2. Edit payment information\n")
                        print("3. Return to menu\n")
                        
                        menuSel = int(input("\nPlease make a selection: "))

                        if menuSel == 1:
                            u.editShippingInfo()
                            

                        elif menuSel == 2:
                            u.editPaymentInfo()

                        elif menuSel == 3:
                            break

                        else:
                            print("\nERROR: That is not a valid selection. Please try again.\n")
                    

                #Return to main menu once deleted, hope they return
                elif menuSel == 5:
                    u.deleteAccount()
                    c.removeFromCart()
                    o.removeFromOrderHistory()

                    break


                elif menuSel == 6:
                    break


                else:
                    print("\nERROR: That is not a valid selection. Please try again.\n")

            

        elif menuSel == 2: 

            u.Register()
            


        else:
            print("\nERROR: That is not a valid selection. Please try again.\n")
    

#^^^^ Plenty of incorrect menuing prevention. CLI programs NEED protective user input


if __name__ == "__main__":
    main()

#Call main
