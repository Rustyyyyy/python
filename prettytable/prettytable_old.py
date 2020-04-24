import sys
from prettytable import PrettyTable #importing a table module
def max():
    print("\nPayroll department system\n")
    print("Enter your ")
    f_name = input("first name:") #for first name   
    l_name = input("last name:") #for last name
    print("\n")
    print("Hour worked:")
    num = int(input("hr: ")) #num for the input of worked hour
    print("\n")
    wrk = num * 45
    print("The total wage is: " + str(wrk) +"\n")
    
    t = PrettyTable(['first Name','last name','wage','Hour worked'])
    t.add_row([f_name, l_name, wrk, num])
    print(t)

if __name__ == "__main__":
    max();