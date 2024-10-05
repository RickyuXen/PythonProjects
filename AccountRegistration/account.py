# project in progress, to register different accounts and store them in a database -> sql
import tkinter as tk
import mysql.connector

# mysql connector - connect database here
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="UserAccounts"
        )
    mycursor = db.cursor()
except:
    print("Issue connecting to db")

def closeWindow(window, prev_window):
    window.destroy()
    prev_window.deiconify()

def backToRoot(window):
    window.destroy()
    root.deiconify()

def on_closing():
    # This function is called when the user clicks the close (X) button
    root.destroy()

def createSmallWindow(prev_window, msgText):
    # creates small windows; mainly for text to appear to let user know about information
    smallWindow = tk.Toplevel(prev_window)
    smallWindow.title("Registration")
    smallWindow.geometry("250x100")

    labelMsg = tk.Label(smallWindow, text=msgText, font=('Arial', 10))
    labelMsg.pack(pady=20)

    backButton = tk.Button(smallWindow, text="Back", command=lambda: closeWindow(smallWindow, prev_window))
    backButton.pack()


def createAccount(new_window, textName, textPassword, textRePassword):
    # add account to sql database

    nameR = textName.get("1.0", "end-1c")
    passwordR = textPassword.get("1.0", "end-1c")
    rePasswordR = textRePassword.get("1.0", "end-1c")

    # replace all spaces in strings
    nameR.replace(" ", "")
    passwordR.replace(" ", "")
    rePasswordR.replace(" ", "")
    print("all spaces are ignored when entered.")

    # Ensure requirements: name minimum 4 length and password minimum 4 length -> do not allow spaces as well.
    if len(nameR) < 4 or len(passwordR) < 4:
        print("Name or password too short; requires minimum length of 4")
        createSmallWindow(new_window, "Name or password is currently too short.")
    else:
        try:
            # check that username does not exist within the database; if it does, do not proceed
            mycursor.execute("SELECT username, COUNT(*) FROM useraccounts.registeredaccounts WHERE username = %s GROUP BY username", (nameR,))
            results = mycursor.fetchall()
            row_count = mycursor.rowcount
            if row_count == 0:
                # check that password and repassword are the same
                if (passwordR == rePasswordR):
                    print("password and repassword are the same; account created")
                    createAccountSuccessful(nameR, passwordR)
                    createSmallWindow(new_window, "Successfully registered account!")
                    # closeWindow(new_window, root)
                else:
                    print("not the same passwords")
                    createSmallWindow(new_window, "Passwords do not match")
            else:
                print("Username already exists in db")
                createSmallWindow(new_window, "Username already exists")
        except:
            print("There was an issue")

    print(nameR, passwordR)
    print('IN PROGRESS')
    
def createAccountSuccessful(username, password):
    # add username and password to SQL database
    mycursor.execute("INSERT INTO RegisteredAccounts (username, passwd) VALUES (%s, %s)", (username, password))
    db.commit() # saves into database
    print("Successfully added to db")

def registerAccount():
    # show new page to register with more information to fill in.
    root.withdraw()
    new_window = tk.Toplevel(root)
    new_window.title("Registration")
    new_window.geometry("500x250")

    labelWelcome = tk.Label(new_window, text="Registration", font=('Arial', 18))
    labelWelcome.pack(pady=5)

    labelName = tk.Label(new_window, text="Username:")
    labelName.pack()
    textName = tk.Text(new_window, height=1, width=20)
    textName.pack()

    labelPass = tk.Label(new_window, text="Password:")
    labelPass.pack()
    textPassword = tk.Text(new_window, height=1, width=20)
    textPassword.pack()

    labelPassAgain = tk.Label(new_window, text="Re-enter Password:")
    labelPassAgain.pack()
    textRePassword = tk.Text(new_window, height=1, width=20)
    textRePassword.pack()


    # button to register
    buttonCreate = tk.Button(new_window, text="Create Account", command=lambda: createAccount(new_window, textName, textPassword, textRePassword))
    buttonCreate.pack(pady=5)

    # button to go back to login page
    buttonBack = tk.Button(new_window, text="Back", command=lambda: closeWindow(new_window, root))
    buttonBack.pack()

    # when user presses (X) on application, to properly close out the root page
    new_window.protocol("WM_DELETE_WINDOW", on_closing)
    
def loginButton(new_window):

    # get input values
    name = textName.get("1.0", "end-1c")
    password = textPassword.get("1.0", "end-1c")

    # if name / password in sql and match, login successful
    # check that username does exist within the database; if it does, do not proceed
    # Check size if < 4 throw exception
    
    mycursor.execute(f"SELECT username, passwd FROM useraccounts.registeredaccounts WHERE username = \"{name}\"")
    results = mycursor.fetchall()
    print(results)
        # check if username and password matches
    try:
        if(name == results[0][0]):
            if(password == results[0][1]):
                print("Login successful")
                # open up page that login was successful -> 
                createSmallWindow(new_window, "Successfully Logged In!")
            else:
                print("Credentials incorrect")
                createSmallWindow(new_window, "Credentials incorrect")
        else:
            print("Credentials incorrect")
            createSmallWindow(new_window, "Credentials incorrect")
    except:
        print("Results not found; empty query")
        createSmallWindow(new_window, "Credentials incorrect")

    print(name + ' ' + password)

if __name__ == "__main__":
    # root main page
    root = tk.Tk()
    root.geometry("500x250")
    root.title("Account Management")

    # label
    labelP = tk.Label(root, text="", font=('Arial', 14))
    label = tk.Label(root, text="Account Management", font=('Arial', 18))
    label.pack(pady=20)

    # Text box (input fields)
    labelName =  tk.Label(root, text="Username:")
    labelName.pack()
    textName = tk.Text(root, height=1, width=20)
    textName.pack()

    labelPass =  tk.Label(root, text="Password:")
    labelPass.pack()
    textPassword = tk.Text(root, height=1, width=20)
    textPassword.pack()

    # buttons to register/login
    buttonReg = tk.Button(root, text="Register Account", command=registerAccount)
    buttonReg.pack(pady=2)
    buttonLog = tk.Button(root, text="Login", command=lambda: loginButton(root))
    buttonLog.pack(pady=1)

    root.mainloop()
