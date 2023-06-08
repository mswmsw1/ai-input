# Here the animation calls the import program to
# get a analog value to place on the graph.
# It must know what channel to ask for.
#
#1/usr/bin/env python
#Based on Python program to test 8 analogue inputs on Custard Pi 3
#www.sf-innovations.co.uk
#
#
#
import RPi.GPIO as GPIO
import time
import sys
#
c = 0
#
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(24, GPIO.OUT)   #pin 24 is chip enable
    GPIO.setup(23, GPIO.OUT)   #pin 23 is clock
    GPIO.setup(19, GPIO.OUT)   #pin 19 is data out
    GPIO.setup(21, GPIO.IN)    #pin 21 is data in
#set pins to default state
    GPIO.output(24, True)
    GPIO.output(23, False)
    GPIO.output(19, True)
    return()
#set address channels 0 to 7
#1st bit selects single/differential
#2nd bit channel address
#3rd bit channel address
#4th bit channel address
#5th bit 1 bit delay for data
#6th bit 1st null bit of data
#
def Read_One_AI(channel_No = 0):
#
    global c
#   
#Define byte to read a channel based on channel number
    if channel_No >= 0:
        # Create chanel word.
        if channel_No == 0:
            word= [1 ,1, 0, 0, 0, 1, 1] #set channel 0
        if channel_No == 1:
            word= [1 ,1, 0, 0, 1, 1, 1] #set channel 1
        if channel_No == 2:
            word= [1 ,1, 0, 1, 0, 1, 1] #set channel 2
        if channel_No == 3:
            word= [1 ,1, 0, 1, 1, 1, 1] #set channel 3
        if channel_No == 4:
            word= [1 ,1, 1, 0, 0, 1, 1] #set channel 4
        if channel_No  == 5:
            word= [1 ,1, 1, 0, 1, 1, 1] #set channel 5
        if channel_No == 6:
            word= [1 ,1, 1, 1, 0, 1, 1] #set channel 6
        if channel_No  == 7:
            word= [1 ,1, 1, 1, 1, 1, 1] #set channel 7
    
        if channel_No > 8: # Was not less than 0 maybe higher then 7
            print( ' Channel Nummer to high')
            GPIO.cleanup # Clean up if exit bad
            sys.exit()    
    # End if
#
        GPIO.output(24, False) #enable chip
        AIvalue=0                 #clear variable
#clock out 7 bits to select channel
        for x in range (0,7):
            GPIO.output(19, word[x])
            time.sleep(0.01)
            GPIO.output(23, True)
            time.sleep(0.01)
            GPIO.output(23, False)
    # End for
#clock in 11 bits of AI data 
        for x in range (0,12):
            GPIO.output(23,True) #set clock hi
            time.sleep(0.01)
            bit=GPIO.input(21) #read input
            time.sleep(0.01)   
            GPIO.output(23,False) #set clock lo
            
            AIbit=bit*2**(12-x-1) #work out value of this bit
            AIvalue = AIvalue + AIbit #add to previous total (12 bit)
    #End For
# print x, bit, value, anip
        GPIO.output(24, True) #disable chip
        volt = AIvalue * 2.5 / 4096 #use ref voltage of 2.5 to work out voltage
# 
    # Sensor range -40 to 125 deg C sensitivity 10 mv / deg C approx
    # convert to mv c = volt * 1000 then divide by 10 {sensitivty actuall 11.5}
    # the zero by subtracting -40 {degC}
    # which gives - You can simplify if you wish.

        c = round((volt * 1000 / 11.5) - 40 ,2)
# testing
#        print ("voltage ch", channel_No, ("%.2f" %round(volt,2)," mV", c, " degC")) #print to screen
#
    return c
    
#Read_One_AI(1)
##GPIO.cleanup()
#import sys
#sys.exit()
#TO TEST
#Note: we use the terminology Channel 0 to 7.
# On the PCB they are marked as Channel 1 to 8.
#Connect Channels 0 to 7 to 2.5V and voltage
#should be 2.5V printed to screen
#Connect two equal resistors in series from 2.5V to 0V.
#Connect mid point of resistors to Channels 0 to 7 in turn
#Voltage should be 1.25V printed to screen
