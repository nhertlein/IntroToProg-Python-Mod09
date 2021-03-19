# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# NHertlein,2021.03.16,Modified code to complete assignment 9

# Github: https://github.com/nhertlein/IntroToProg-Python-Mod09
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":  # Only run if this is not an imported module
    from DataClasses import Employee as Emp  # Include Employee class
    from ProcessingClasses import FileProcessor as FP  # Import FileProcessor class
    from IOClasses import EmployeeIO as Eio  # Import EmployeeIO class
else:
    raise Exception("Chancho, I need borrow some sweats [and not try to import this module!]")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Define variables
lstFileData = None
lstEmployees = []  # Empty list of employee [luchador] objects
strOption = ""
objEmp = None

# Load data from file into a list of employee objects when script starts
lstFileData = FP.read_data_from_file("EmployeeData.txt")
for line in lstFileData:
    lstEmployees.append(Emp(line[0], line[1], line[2].strip()))

# Main loop
while True:
    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    strOption = Eio.input_menu_options()
    if strOption == "1":
        # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstEmployees)
        continue
    elif strOption == "2":
        # Let user add data to the list of employee objects
        objEmp = Eio.input_employee_data()
        lstEmployees.append(objEmp)
        continue
    elif strOption == "3":
        # let user save current data to file
        FP.save_data_to_file("EmployeeData.txt", lstEmployees)
        continue
    elif strOption == "4":
        # Let user exit program
        print("Get that corn outta my face!")
        input("Press ENTER to exit")
        break

# Main Body of Script  ---------------------------------------------------- #
