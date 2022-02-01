import pymongo
import random
import datetime

client = pymongo.MongoClient("mongodb+srv://pythonCode:Python@cluster0.gee6w.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["database"]
col = db["userAccess"]

while True:
 print("👋 Welcome. Type (L) to login, (C) to create an account or o (Q) to quit.")
 val = input("Selected option: ").upper()

 if val == "Q":
    print("Goodbye.")
    break

 elif val == "C":
     print("\nAccount creation process started.")
     
     while True:
         print("\nPlease insert your new username.")
     
         user = str(input("Username: "))

         q = {"username": user}
         
         if col.find_one(q):
             print("\nAn account with that username already exists.\nPlease try a new one.")
         else:
             print("\nPlease input your password.")
             passw = str(input("Password: "))
         
             print("\nPlease input your current balance.")
     
             try:
                 bal = int(input("Balance: "))
             except ValueError:
                 print("Did not insert a number. Account creation cancelled.")
                 break

             print("\nCreating account...")
    
             id = random.randint(1000, 2000)
             newUser = {"_id": id, "username": user, "password": passw, "balance": bal}
             x = col.insert_one(newUser)

             print("\nUser created under these credentials:")
             print("Username:", user)
             print("Password:", passw)
             print("Account ID:", x.inserted_id,"\n")
             break

 elif val == "L":
     while True:
      print("Please enter your credentials. Type (Q) to quit.")
      userL = str(input("Username: "))
      if userL.upper() == "Q": break

      print("\nSearching...")

      q = {"username": userL}
      find = col.find_one(q)

      if find:
          login = True
      else:
          login = False

      if login:
         print("We need to validate your identity.")
         print("Please enter your password.")
         passw = str(input("Password: "))
         print("\nValidating...")

         q = {"password": passw}
         find = col.find_one(q)

         if find:
             validated = True
         else: 
             validated = False

         if validated:
             d = datetime.datetime.now()
             d1 = d.strftime("%p")
             date = "Morning" if d1 == "AM" else "Evening"
             print(f"Good {date}.\nWelcome back, {userL}")
             
             while True:
                 print("\nWhat would you like to manage?")
                 print("(D) Deposit money. (S) Substract money. (I) Get information about your account. (Q) Quit.")
                 val = str(input("Selected option: ")).upper()

                 if val == "Q":
                     print("Quiting...")
                     break 
                
                     

                 elif val == "D":
                      while True:
                         print("\nHow much would you like to deposit?")
                     
                         try:
                           inp = int(input("Amount: "))
                     
                         except ValueError:
                             print("\nPlease type a valid number.")

                         else:
                             print("\nDepositing amount...")

                             q = col.find_one({"username": userL}, {"balance": 1})
                             qi = int(q["balance"])
                             qn = {"$set": {"balance": qi + inp}}

                             x = col.update_one(q, qn)
                             print("Successfully added to your balance $", inp)
                             break

                 elif val == "S":
                     while True:
                         print("\nHow much would you like to substract?")

                         try:
                             inp = int(input("Amount: "))
                         except ValueError:
                             print("\nPlease type a valid number")

                         else:
                             print("\nSubstracting amount...")

                             q = col.find_one({"username": userL}, {"balance": 1})
                             qi = int(q["balance"])
                             qn = {"$set": {"balance": qi - inp}}

                             x = col.update_one(q, qn)
                             print("Successfully substracted from your balance $", inp)
                             break

                 elif val == "I":
                     print("Displaying your current information.\n")

                     q = col.find_one({"username": userL}, {"balance": 1})
                     qi = int(q["balance"])

                     print(f"Username: {userL}")
                     print(f"Balance: {qi}")
                        

         else:
             print("Wrong password. Try again.")
    
      else:
         print("No account found by this username. Try again.")
