#1. Write a python program using Function to which will do the following: # time of last access - read , write, last modification - content is modified and last inode (index node - specific identifier, metadata)change - time of file creation
#a. The function will create a text file with the current timestamp #  format YYYY-MM-DD hh:mm:ss - year, month, day, hour, minute, second, and fractional seconds.
#b. The file content should have the content of the current timestamp.

def timestamp():
    # f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\timestamp.txt","x")
    # f.close()
    f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\timestamp.txt", "w")
    f.write("import datetime\nct = datetime.datetime.now()\nprint('current time: ', ct)\nts = ct.timestamp()\nprint('timestamp: -', ts)\nts_int = int(ts)\nts_format = datetime.datetime.utcfromtimestamp(ts_int)")
    f.close()
    f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\timestamp.txt", "a")
    f.write("\nprint(ts_format)")
    f.close()
    f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\timestamp.txt", "r")
    print(f.read())
    f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\timestamp.txt")
    f.close()

timestamp()