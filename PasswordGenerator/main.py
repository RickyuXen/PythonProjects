import random
import string
import time
import tkinter as tk

# method to generate password
def generatePassword():
    global labelP

    if len(text.get("1.0", "end-1c"))<=1:
        labelP["text"] = "Please enter in the length of your password"
    length = text.get("1.0", "end-1c")
    
    intLength = int(length)
    letters = string.ascii_letters
    numbers = string.digits
    if(intLength == 0):
        labelP["text"] = "Cannot have 0 length"

    elif intCheck.get() == 1 and intCheck2.get() == 1:
        passwordValue = ''.join(random.choice(letters + numbers) for i in range(intLength))
        labelP["text"]= passwordValue

    elif intCheck.get() == 1:
        passwordValue = ''.join(random.choice(letters) for i in range(intLength))
        labelP["text"]= passwordValue

    elif intCheck2.get() == 1:
        passwordValue = ''.join(random.choice(numbers) for i in range(intLength))
        labelP["text"]= passwordValue

    else:
        labelP["text"]= "Please pick at least one of the checkboxes"

# create GUI
root = tk.Tk()

photo = tk.PhotoImage(file = "lock.png")
root.iconphoto(False, photo)

root.geometry("500x250")
root.title("Password Generator")

# label
labelP = tk.Label(root, text="", font=('Arial', 14))
label = tk.Label(root, text="Password Generator", font=('Arial', 18))
label.pack()

# checkboxes
intCheck = tk.IntVar()
intCheck2 = tk.IntVar()

check1 = tk.Checkbutton(root,text="Alphabets", variable=intCheck)
check1.pack()
check2 = tk.Checkbutton(root,text="Numbers", variable=intCheck2)
check2.pack()

check1.select()
check2.select()

# Text box
labelInfo=  tk.Label(root, text="Enter in length of password: ")
labelInfo.pack()
text = tk.Text(root, height=1, width=4)
text.pack()

# button
button = tk.Button(root, text="Generate", command=generatePassword,)
button.pack()

# label with password
labelP.pack()

root.mainloop()
