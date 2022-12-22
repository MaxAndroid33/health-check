#!/user/bin/env python3
import os
import sys

def check_reboot():
    """ Returns True if the computer has a pending erboot. """
    
def main():
    if check_reboot():
        print("pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()