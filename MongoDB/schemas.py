def student_serializer(student) -> dict:
    return {
        "STID" : str(student["_id"]),
        "FName" : student["FName"],
        "LName" : student["LName"],
        "Father" : student["Father"],
        "Birth" : student["Birth"],
        "SerialID" : student["SerialID"],
        "BornCity" : student["BornCity"],
        "Address" : student["Address"],
        "PostalCode" : student["PostalCode"],
        "CPhone" : student["CPhone"],
        "HPhone" : student["HPhone"],
        "Department" : student["Department"],
        "Major" : student["Major"],
        "Married" : str(student["Married"]),
        "ID" : student["ID"]
    }

def list_serial_student(students) -> list:
    return [student_serializer(student) for student in students]


#---------------------------------------------------------------------------------------------


def lecturer_serializer(lecturer) -> dict:
    return {
        "LID" : str(lecturer["_id"]),
        "FName": lecturer["FName"],
        "LName": lecturer["LName"],
        "ID": lecturer["ID"],
        "Department": lecturer["Department"],
        "Major": lecturer["Major"],
        "Birth": lecturer["Birth"],
        "BornCity": lecturer["BornCity"],
        "Address": lecturer["Address"],
        "PostalCode": lecturer["PostalCode"],
        "CPhone": lecturer["CPhone"],
        "HPhone": lecturer["HPhone"]
    }

def list_serial_lecturer(lecturers) -> list:
    return [lecturer_serializer(lecturer) for lecturer in lecturers]


#---------------------------------------------------------------------------------------------


def course_serializer(course) -> dict:
    return {
        "CID": str(course["_id"]),
        "CName": course["CName"],
        "Department": course["Department"],
        "Credit": course["Credit"]
    }

def list_serial_course(courses) -> list:
    return [course_serializer(course) for course in courses]


#---------------------------------------------------------------------------------------------


def course_register_serializer(course_register) -> dict:
    return {
        "Credit": course_register["Credit"],
        "Department": course_register["Department"],
        "CName": course_register["CName"],
        "FName": course_register["FName"],
        "LName": course_register["LName"],
        "STID": course_register["STID"],
        "CID": course_register["CID"]
    }

def list_serial_course_register(course_registers) -> list:
    return [course_register_serializer(course_register) for course_register in course_registers]


#---------------------------------------------------------------------------------------------


def presented_courses_serializer(presented_courses) -> dict:
    return {
        "CName": presented_courses["CName"],
        "Department": presented_courses["Department"],
        "Credit": presented_courses["Credit"],
        "FName": presented_courses["FName"],
        "LName": presented_courses["LName"],
        "CID": presented_courses["CID"],
        "LID": presented_courses["LID"]
    }

def list_serial_presented_courses(presented_courses) -> list:
    return [presented_courses_serializer(presented_course) for presented_course in presented_courses]
