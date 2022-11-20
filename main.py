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

            loggedIn = False
            
            while loggedIn == False:

                currUser = str(input("\nEnter your username: "))

                for i in validUser:
                    if any(currUser in i for i in validUser):
                        while loggedIn == False:
                            currPass = str(input("\n Enter your password: "))

                            for i in validPass:
                                if any(currPass in i for i in validPass):
                                    loggedIn = True
                                    break

                                else:
                                    print("ERROR: That password is incorrect. Please try again.\n")
                                    break

                            

                    else:
                        print("ERROR: That username does not exist. Please try again.\n")   
                        break

                         
            break

    
    while True:
        print("\n\n0. Exit the program\n")
        print("1. Browse our inventory\n")
        print("2. View your cart\n")
        print("3. Edit your account information\n")
        print("4. Delete your account\n")

        menuSel = int(input("\nPlease make a selection: "))

        if menuSel == 0:
            raise SystemExit(0)


                
            

            

                

                
                





if __name__ == "__main__":
    main()


