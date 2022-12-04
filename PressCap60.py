
import pyautogui
import time
import random

var_i = True
while var_i==True:
    pyautogui.press('capslock') #Simulate press escape ke
    localtime = time.localtime() #Capture local time for logging
    result = time.strftime("%I:%M:%S %p", localtime) #Format the time to a readable value
    print('Successfully Updated Running_Production_Air_Tool_Query at ' + str(result)) #print out time
    time.sleep(60) #do nothing for 60 seconds
print("Program End")