import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "ECommerce_Group10"
)

print(mydb)

mycursor = mydb.cursor()


#class account:


#class shoppingCart:


##class orderHistory:
    ##def __init__(self, purchased, shippingInfo, paymentInfo):
        ##self.purchased = purchased
        #self.shippingInfo = shippingInfo
        #self.paymentInfo = paymentInfo

    ##def addToOrderHistory(self):




#class inventory:


def main():
    print("\nWelcome to the E-Commerce Store!")
    print("Version 1.0.0 by Group 10\n")

    print("\nPlease login or create an account to get started.")

    while True:
        print("\n0. Exit the program\n")
        print("1. Log in to an existing account\n")
        print("2. Create an account\n")

        menuSel = int(input("\nPlease make a selection: "))

        if menuSel == 0:
            raise SystemExit(0)

        elif menuSel == 1:
                
            mycursor.execute("SELECT userName FROM accounts")

            validUser = mycursor.fetchall()

            mycursor.execute("SELECT passWd FROM accounts")

            validPass = mycursor.fetchall()
            
            while True:

                currUser = str(input("\nEnter your username: "))

                for i in validUser:
                    if any(currUser in i for i in validUser):
                        while True:
                            currPass = str(input("\n Enter your password: "))

                            for i in validPass:
                                if any(currPass in i for i in validPass):
                                    loggedIn = True

                                    while loggedIn == True:
                                        print("\n\n0. Exit the program\n")
                                        print("1. Browse our inventory\n")
                                        print("2. View your cart\n")
                                        print("3. Edit your account information\n")
                                        print("4. Delete your account\n")

                                        menuSel = int(input("\nPlease make a selection: "))

                                        if menuSel == 0:
                                            raise SystemExit(0)

                                        #elif menuSel == 1:


                                        #elif menuSel == 2:

                                        #elif menuSel == 3:

                                        elif menuSel == 4:
                                            str(input("\nAre you sure you want to delete your account? (y/n) "))
                                            userConf = str(input("\nARE YOU SURE? (y/n) "))

                                            if (userConf == 'n'):
                                                continue

                                            elif (userConf == 'y'):

                                                accDel = "DELETE FROM accounts WHERE userName = '" + currUser +"'"

                                                mycursor.execute(accDel)

                                                mydb.commit()

                                                raise SystemExit(0)

                                                
                                                
        

                                            else:
                                                print("\nERROR: That is not a valid selection. Exiting to menu.\n")
                                                break
                                            
                                            
                                                

                                else:
                                    print("ERROR: That password is incorrect. Please try again.\n")
                                    break

                            

                    else:
                        print("ERROR: That username does not exist. Please try again.\n")   
                        break

                         
                break

        elif menuSel == 2: 

            mycursor.execute("SELECT userName FROM accounts")

            validUser = mycursor.fetchall()

            mycursor.execute("SELECT passWd FROM accounts")

            validPass = mycursor.fetchall()

            print("Welcome!")
            validNew = False
            while validNew == False:
                newUser = str(input("Please enter a username: "))

                if any(newUser in i for i in validUser):
                    print("ERROR: That username already exists. Please enter a different one.")
                    continue

                else:

                    newPass = str(input("Please enter a password: "))

                    if any(newPass in i for i in validPass):
                        print("ERROR: That password already exists. Please enter a different one.")
                        continue

                    else:
                        mycursor.execute("SELECT customerID FROM accounts")
                        IDind = mycursor.fetchall()
                        newID = "980" + str(len(IDind) + 1)

                        sql = "INSERT INTO accounts (customerID, userName, passWd) VALUES ('" + newID + "', '" + newUser + "', '" + newPass + "')"

                        mycursor.execute(sql)

                        mydb.commit()

                        break



    

        




                
            

            

                

                
                





if __name__ == "__main__":
    main()


