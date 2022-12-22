#!/user/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """ Returns True if the computer has a pending erboot. """
    return os.path.exits("/run/reboot-required")

def check_disk_usage(disk ,min_abs ,mi_percent):
    """Returns True if there is enough free disk space , false otherwise """
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free /du.total
    # Calculate how many free gigabytes
    gigabytes_free =du.free /2**30
    if percent_free <mi_percent or gigabytes_free < min_abs :
        return False
    return True

def main():
    if check_reboot():
        print("pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()
