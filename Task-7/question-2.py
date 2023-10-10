#2. Write another python function to read from a text file. The function will take the name of the text file and display
# the content of the file into the console.

def func1():
        #f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\text2.txt","x")
        #f.close()
        f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\text2.txt","w")
        f.write("Am Nabela, Learning Python\n")
        f.close()
        f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\text2.txt", "a")
        f.write("in Guvi")
        f.close()
        f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\text2.txt", "r")
        f.read()
        f = open(r"C:\Users\Nabela\OneDrive\Guvi - Automation testing\Python\Task\Task-7\text2.txt")
        f.close()
func1()