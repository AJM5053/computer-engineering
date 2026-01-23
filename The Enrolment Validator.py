# A dictionary for module prerequisites
module_prerequisites = {
    "CIS1702": [],
    "CIS1000": ["CIS1702"],
    "CIS1001": ["CIS1702"],
    "CIS2000": ["CIS1000", "CIS1702"],
    "MTH1001": [],
    "CIS2005": ["CIS1000", "MTH1001"]
}

# A dictionary for student data
student_database = {
    "s12345": {
        "Name": "Alice",
        "Completed": ["CIS1702", "MTH1001"]
    },
    "s67890": {
        "Name": "Bob",
        "Completed": ["CIS1702", "CIS1001"]
    },
    "s54321": {
        "Name": "Charlie",
        "Completed": ["MTH1001"]
    }
}

# A fucntion for checking if a student can enrol in a module
def can_enrol(student_id, module_code):
    
    if student_id not in student_database:
        print("Error: that ID doesn't exist")
        return False
    
    if module_code not in module_prerequisites:
        print("Error: that module doesn't exist")
        return False
    
    prerequisites = module_prerequisites[module_code]
    completed_modules = student_database[student_id]["Completed"]

    completed_set = set(completed_modules)

    for required_module in prerequisites:
        if required_module not in completed_set:
            print(f"Missing prerequisite module: {required_module}")
            return False
    return True

# Test cases
print(can_enrol("s12345", "CIS1000"))
print(can_enrol("s13579", "CIS1702"))
print(can_enrol("s54321", "CIS1000"))

# A function to enrol a student in a module
def enrol_student(student_id, module_code):
    if student_id not in student_database:
        return "Error: that ID doesn't exist"
    
    if module_code not in module_prerequisites:
        return "Error: that module doesn't exist"
    
    completed_list = student_database[student_id]["Completed"]

    if module_code in completed_list:
        print("This student already has that module")

    else:
        if can_enrol(student_id, module_code):
            completed_list.append(module_code)
            print(f"Sucessfully enrolled {student_id} in {module_code}")
        else:
            print("Enrollment failed")

# Further tests
print()
enrol_student("s54321", "CIS1000")
enrol_student("s12345", "CIS1000")
print(student_database["s12345"]["Completed"])
enrol_student("s12345", "CIS1000")
enrol_student("s12345", "CIS2000")