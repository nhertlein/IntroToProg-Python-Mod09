# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A module for testing
# ChangeLog (Who,When,What):
# NHertlein,2021.03.15,Initial Release

# Github: https://github.com/nhertlein/IntroToProg-Python-Mod09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Person as P  # Update to import Person class
    from DataClasses import Employee as Emp  # Include Employee class
    from ProcessingClasses import FileProcessor as FP  # Import FileProcessor class
    from IOClasses import EmployeeIO as Eio  # Import EmployeeIO class
else:
    raise Exception("Did you tell him they are the Lords chips?")

# Test Person class from DataClasses module
objP1 = P("Nacho", "Libre")
objP2 = P("Steven", "Esqueleto")
objP3 = P("Sister", "Encarnación")
lstTable = [objP1, objP2, objP3]
for row in lstTable:
    print(row.to_string(), type(row))  # Check person objects

# Test Employee class from DataClass module adding employee number (use existing data, not re-enter)
objE1 = Emp(1, objP1.first_name, objP1.last_name)
objE2 = Emp(2, objP2.first_name, objP2.last_name)
objE3 = Emp(3, objP3.first_name, objP3.last_name)
lstEmployees = [objE1, objE2, objE3]
for row in lstEmployees:
    print(row.to_string(), type(row))  # Check employee objects

#  Test FileProcessor class from ProcessingClasses module
FP.save_data_to_file("EmployeeData.txt", lstEmployees)  # Save data
lstFileData = FP.read_data_from_file("EmployeeData.txt")  # Read data back in
lstEmployees.clear()  # Clear list
for line in lstFileData:  # Repopulate list
    lstEmployees.append(Emp(line[0], line[1], line[2].strip()))
for row in lstEmployees:  # Print list
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()  # check menu print
Eio.print_current_list_items(lstEmployees)  #
print(Eio.input_employee_data())
print(Eio.input_menu_options())