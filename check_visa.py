# Display resolution: 1920 x 1080
# Scale: 100%
# Browser: Chrome (bookmark bar is hidden)

import numpy as np
import webbrowser
import pyautogui
import easygui
import time
import cv2
import sys
import os
from colorthief import ColorThief
from datetime import datetime
from turtle import color

# title = "USA Visitor Visa Appointment Bot"
# msg = "Do you want to schedule the script or run it now?"
# choices = ["Schedule","Run it now!"]
# reply = easygui.buttonbox(msg, title, choices=choices)

# if reply == "Schedule":
#     msg = "Schedule Script\n\nWrite everything as a double digit.\nFor ex.\n7 -> 07"
#     fieldNames = ["Hour", "Minute", "Second"]
#     fieldNames_defs = ["", "00", "00"]
#     fieldValues = easygui.multenterbox(msg, title, fieldNames, fieldNames_defs)
#     if fieldValues is None:
#         sys.exit(0)
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     # current_time format = 07:08:50
#     while (current_time[:2] != str(fieldValues[0])) or (current_time[3:5] != str(fieldValues[1])) or (current_time[6:] != str(fieldValues[2])):
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         # print(current_time)
# else:
#     pass    

# message for telegram group
message = "Slot Open Now"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Program Files//Google//Chrome//Application//chrome.exe"))

webbrowser.get('chrome').open(
    "https://ais.usvisa-info.com/en-ca/niv/users/sign_in")
time.sleep(5)
pyautogui.press('pagedown')
# click on "I have read..."
pyautogui.click(404, 684, duration = 0.9)
# click on Sign in button
pyautogui.click(441, 766, duration = 0.5)
# wait to load the page
time.sleep(6)
# click on Continue button
pyautogui.click(1461, 346, duration = 0.5)
# wait
time.sleep(1)
# click on "Reschedule Appointment"
pyautogui.click(624, 535, duration = 0.9)
# click on "Reschedule Appointment" button
pyautogui.click(678, 674, duration = 0.5)
# wait
time.sleep(1)
time.sleep(5)
# click on center of "Date of Appointment" input box
pyautogui.click(691, 686, duration = 0.5)

# wait to load calendar
time.sleep(2)
try:
    month_color = pyautogui.locateOnScreen(
        'Images/month_back_button.png', confidence=0.9)

    if month_color is None:
        print("Calendar not detected")
except pyautogui.ImageNotFoundException:
    print("Calendar not detected")

month_back_button_count = 0

while (month_color != None) and (month_back_button_count != 50):
    # calendar screenshot resolution
    # 488 775
    #         1020 949
    image = pyautogui.screenshot(region=(488, 775, 532, 174))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(".//Images//Appointment.png", image)
    time.sleep(1)
    color_thief = ColorThief(".//Images//Appointment.png")

    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    # build a color palette
    palette = color_thief.get_palette(color_count=6)
    Px = palette[1][0]
    Py = palette[1][1]
    Pz = palette[1][2]
    if (Px >= 60 and Px <= 70) and (Py >= 120 and Py <= 130) and (Pz >= 162 and Pz <= 172):
        x, y = 508, 798
        flag1 = 0
        for j in range(0, 5):
            for i in range(0, 7):
                pyautogui.click(x, y)
                x += 35
            if flag1 != 4:
                y += 30
                x = 508
                flag1 += 1

        # check left calendar
        try:
            month_color = pyautogui.locateOnScreen(
                './Images/month_back_button.png', confidence=0.9)
            if month_color is None:
                pyautogui.click(712, 751)
                # down time slot
                pyautogui.click(700, 798, duration=0.5)
                # up time slot
                pyautogui.click(704, 716, duration=0.5)
                
                image = pyautogui.screenshot(region=(496, 625, 168, 149))
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("C://Users//arshit//Desktop//visa script v2//Images//Final_Appointment.png", image)

                # send message in telegram group 
                telegram_send_cmd = 'telegram-send --config group1.conf --image "C://Users//arshit//Desktop//visa script v2//Images//Final_Appointment.png" --caption "Slot opened at"'
                os.system(telegram_send_cmd)

                # click on green "Reschedule" button
                pyautogui.click(1675, 873, duration=0.5)
                break
        except pyautogui.ImageNotFoundException:

            pyautogui.click(712, 751)
            # down time slot
            pyautogui.click(700, 798, duration=0.5)
            # up time slot
            pyautogui.click(704, 716, duration=0.5)
            
            image = pyautogui.screenshot(region=(496, 625, 168, 149))
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            cv2.imwrite("C://Users//arshit//Desktop//visa script v2//Images//Final_Appointment.png", image)

            # send message in telegram group 
            telegram_send_cmd = 'telegram-send --config group1.conf --image "C://Users//arshit//Desktop//visa script v2//Images//Final_Appointment.png" --caption "Slot opened at"'
            os.system(telegram_send_cmd)

            # click on green "Reschedule" button
            pyautogui.click(1675, 873, duration=0.5)
            break

        # check right calendar
        x, y = 777, 797
        flag2 = 0
        for j in range(0, 5):
            for i in range(0, 7):
                pyautogui.click(x, y)
                x += 35
            if flag2 != 4:
                y += 30
                x = 777
                flag2 += 1

        try:
            month_color = pyautogui.locateOnScreen(
                './Images/month_back_button.png', confidence=0.9)
            if month_color is None:
                break
        except pyautogui.ImageNotFoundException:
            break
    
    else:
        time.sleep(0.5)
        # click on Next month button in the calendar
        pyautogui.click(1003, 725)
    month_back_button_count += 1 

# pyautogui.hotkey('ctrl', 'w')

# config bot
# telegram-send --config

# telegram cmd
# telegram-send --config user1.conf --config user2.conf "z"

# config group
# telegram-send --config group1.conf --configure-group

# send msg in grp
# telegram-send --config group1.conf "message"

# appointment dominant rgb color
# (48, 76, 98)
# (63, 121, 166)
# (67, 124, 168)