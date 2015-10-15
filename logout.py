#!/bin/python
from os.path import isfile
from os import system
from time import sleep

sleepCommand = "gnome-screensaver-command -l"
delay = 1

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
    if "open" in state:
        lastLoopWasClosed = False
    else:
        if not lastLoopWasClosed:
            system(sleepCommand)
            lastLoopWasClosed = True
    sleep(delay)
