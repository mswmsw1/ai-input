import os
import array as arr

# test
#myPath = tk.StringVar()

#to get the current working directory
def FileWrite(min,max,ch0,ch1,ch2,ch3,ch4,ch5,ch6,ch7):
    # Test print
    print("AI_File_Handle.FileWrite")
    # Get the path to the program
    myPath = os.getcwd()
    # Test print
   #print(myPath)
    
    # Move the values to local vars and make into strings.
    min1 = str(min)
    max1 = str(max)
    ch01 = str(ch0)
    ch11 = str(ch1)
    ch21 = str(ch2)
    ch31 = str(ch3)
    ch41 = str(ch4)
    ch51 = str(ch5)
    ch61 = str(ch6)
    ch71 = str(ch7)
    
    # Create a complete string to save to file
    SaveStr = min1 + "," + max1 + "," + ch01 + "," + ch11 + "," + ch21   \
        + "," + ch31 + "," + ch41 + "," + ch51 + "," + ch61 + "," + ch71 \
        + "," + myPath
    # Test string
    print(SaveStr + ' Write')

   # Open, write and close file
    Aifile = open(myPath + "/AI_log.txt", "w")
    Aifile.write(SaveStr)
    Aifile.close()
    
    return

#def FileRead(min,max,ch0,ch1,ch2,ch3,ch4,ch5,ch6,ch7,myPath):
def FileRead():
    a = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
    # Test print
    print("AI_File_Handle.FileRead") 
    
    # Get the path to the program
    myPath = os.getcwd()
    # Test print
    #print(myPath) 
    # Open file to read. Place in the SaveStr then close
    Aifile = open(myPath + "/AI_log.txt", "r")
    SaveStr = Aifile.readline()
    Aifile.close()
    # Remove after testing
    print('Data')
    print(SaveStr)
    
    # Process SaveStr
#    TextList = SaveStr.split(',')
    #print(TextList)
#    min1 = TextList[0]
#    max1 = TextList[1]
#    ch01 = TextList[2]
#    ch11 = TextList[3]
#    ch21 = TextList[4]
#    ch31 = TextList[5]
#    ch41 = TextList[6]
#    ch51 = TextList[7]
#    ch61 = TextList[8]
#    ch71 = TextList[9]
#    myPath = TextList[10]
    
    
#    ch0 = int(ch01)
#    ch1 = int(ch11)
#    ch2 = int(ch21)
#    ch3 = int(ch31)
#    ch4 = int(ch41)
#    ch5 = int(ch51)
#    ch6 = int(ch61)
#    ch7 = int(ch71)
    
   # print(SaveStr)
    
    return(SaveStr)
    