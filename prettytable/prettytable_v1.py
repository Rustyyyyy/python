import sys
from prettytable import PrettyTable #importing a table module

def main():
    print("\n\tPayroll department system\n")

    print("Enter your")
    first_Name = input("first name: ")   
    last_name = input("last name: ") 

    print("\nHour worked")
    hourWordked = int(input("hr: ")) 

    if hourWordked != 0:  total_Wage = hourWordked * 45
    else : print("\nenter appropriate value\n"); sys.exit()

    print("\nThe total wage is: {}\n".format(total_Wage))
    
    tablevalue = PrettyTable(['first Name','last name','wage','Hour worked'])
    tablevalue.add_row([first_Name, last_name, total_Wage, hourWordked])
    print(tablevalue)

if __name__ == "__main__":  main()
    