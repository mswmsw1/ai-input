
import tkinter as tk
#Name of the main form
Form1 = tk.Tk()
# importing "array" for array creations
import array as arr
import AI_File_Handle
import Animation
import RPi.GPIO as GPIO

# Size and title
Form1.geometry("800x600")
Form1.title("Setup")

SaveStr = tk.StringVar()
myPath = tk.StringVar()
E1 = tk.StringVar()
E1.set("-40")
E2 = tk.StringVar()
E2.set("125")

Ckb0 = tk.IntVar()
Ckb1 = tk.IntVar()
Ckb2 = tk.IntVar()
Ckb3 = tk.IntVar()
Ckb4 = tk.IntVar()
Ckb5 = tk.IntVar()
Ckb6 = tk.IntVar()
Ckb7 = tk.IntVar()

global En
En = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0])


# Activate via save button
def set_defaults():
    min = E1.get()
    max = E2.get()
    print(Ckb0, ' Ckb0')
    En[0] = Ckb0.get()
    En[1] = Ckb1.get()
    En[2] = Ckb2.get()
    En[3] = Ckb3.get()
    En[4] = Ckb4.get()
    En[5] = Ckb5.get()
    En[6] = Ckb6.get()
    En[7] = Ckb7.get()
    
    print(En[0], En[1], En[2], En[3], En[4], En[5], En[6], En[7], 'Enables')

 # Pass vars to file handle to save
    AI_File_Handle.FileWrite(min, max, En[0], En[1], En[2], En[3], En[4], En[5], En[6], En[7])
## End save defaults ##

# Enable channels you want to use
C1 = tk.Checkbutton(Form1, text = "Enable Ch 0", variable = Ckb0).grid(row = 2, column = 1)
C2 = tk.Checkbutton(Form1, text = "Enable Ch 1", variable = Ckb1).grid(row = 3, column = 1)
tk.Checkbutton(Form1, text = "Enable Ch 2", variable = Ckb2).grid(row = 4, column = 1)
tk.Checkbutton(Form1, text = "Enable Ch 3", variable = Ckb3).grid(row = 5, column = 1)
tk.Checkbutton(Form1, text = "Enable Ch 4", variable = Ckb4).grid(row = 2, column = 2)
tk.Checkbutton(Form1, text = "Enable Ch 5", variable = Ckb5).grid(row = 3, column = 2)
tk.Checkbutton(Form1, text = "Enable Ch 6", variable = Ckb6).grid(row = 4, column = 2)
tk.Checkbutton(Form1, text = "Enable Ch 7", variable = Ckb7).grid(row = 5, column = 2)

tk.Entry(Form1, width=5, textvariable=E1).grid(row = 26, column = 1)
tk.Entry(Form1, width=5, textvariable=E2).grid(row = 26, column = 2)

#Label(t, text = "test").grid(row=20, column = 0)
B1 = tk.Button(Form1, text = "Save", bg = "grey", fg = "white", width = 10, 
       command = set_defaults).grid(row = 31, column = 2, pady = 6)

B2 = tk.Button(Form1, text = "Start", bg = "grey", fg = "white", width = 10, 
       command = Animation.animate()).grid(row = 31, column = 1, pady = 6)

# Open to read options file when the form opens and nothing is happening
#t.after_idle(AI_File_Handle.FileRead)

SaveStr = AI_File_Handle.FileRead()


print(SaveStr + ' Data to save')
# Process SaveStr
TextList = SaveStr.split(',')
#print(TextList)
min1 = TextList[0]
max1 = TextList[1]
ch0 = TextList[2]
ch1 = TextList[3]
ch2 = TextList[4]
ch3 = TextList[5]
ch4 = TextList[6]
ch5 = TextList[7]
ch6 = TextList[8]
ch7 = TextList[9]
myPath = TextList[10]
print(myPath)

En[0] = int(ch0)
En[1] = int(ch1)
En[2] = int(ch2)
En[3] = int(ch3)
En[4] = int(ch4)
En[5] = int(ch5)
En[6] = int(ch6)
En[7] = int(ch7)
    
Ckb0.set(En[0])
Ckb1.set(En[1])
Ckb2.set(En[2])
Ckb3.set(En[3])
Ckb4.set(En[4])
Ckb5.set(En[5])
Ckb6.set(En[6])
Ckb7.set(En[7])
#print(Ckb0,Ckb1,Ckb2)

print('Done GUI ')

Form1.mainloop()

GPIO.cleanup() 