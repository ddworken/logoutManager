#!/bin/python
from os.path import isfile #used to check the location of the file containing the lid state
from os import system #used to lock the screen
from time import sleep #used to sleep 1 second between loops

sleepCommand = "gnome-screensaver-command -l" #modify this if needed
delay = 1 #the number of seconds to sleep between loops. Increase this if you want your computer not to lock if the screen is only closed for x seconds

if isfile("/proc/acpi/button/lid/LID/state"):
    filename = "/proc/acpi/button/lid/LID/state"
else:
    if isfile("/proc/acpi/button/lid/LID0/state"):
        filename = "/proc/acpi/button/lid/LID/state"
    else:
        print "Could not find the lid state. "
        exit()

while True:
    with open(filename) as f:
        state = f.read().splitlines()[0]
    if "open" in state: #if the lid is open
        lastLoopWasClosed = False
    else: #if the lid is closed
        if not lastLoopWasClosed: #don't lock the computer if we already locked it
            system(sleepCommand)
            lastLoopWasClosed = True
    sleep(delay)
