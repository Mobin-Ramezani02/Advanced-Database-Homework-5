from fastapi import APIRouter, HTTPException
from models import *
from database import student_collection, lecturer_collection, course_collection, courseRegister_collection, presentedCourses_collection
from schemas import *
from bson import ObjectId

myRouter = APIRouter()


# Read (SELECT) -> student
@myRouter.get("/student/select/")
async def read_student():
    students = student_collection.find()
    return list_serial_student(students)


# Create (INSERT) -> student
@myRouter.post("/student/create/")
async def create_student(student: Student):
    student_collection.insert_one(dict(student))
    raise HTTPException(status_code=200, detail="دانشجوی جدید با موفقیت ثبت شد")


# Update -> student
@myRouter.put("/student/update/{stid}")
async def update_student(stid: str, student: Student):
    if not student_collection.find_one({"_id": ObjectId(stid)}):
        raise HTTPException(status_code=404, detail=f"دانشجو با شماره دانشجویی {stid} یافت نشد")

    student_collection.update_one({"_id": ObjectId(stid)}, {"$set": dict(student)})
    return {"message": "اطلاعات دانشجو با موفقیت به‌روزرسانی شد"}


# Delete -> student
@myRouter.delete("/student/delete/{stid}")
async def delete_student(stid: str):
    if not student_collection.find_one({"_id": ObjectId(stid)}):
        raise HTTPException(status_code=404, detail=f"دانشجو با شماره دانشجویی {stid} یافت نشد")

    student_collection.delete_one({"_id": ObjectId(stid)})
    return {"message": "دانشجو با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------


# Read (SELECT) -> lecturer
@myRouter.get("/lecturer/select/")
async def read_lecturer():
    lecturers = lecturer_collection.find()
    return list_serial_lecturer(lecturers)


# Create (INSERT) -> lecturer
@myRouter.post("/lecturer/create/")
async def create_lecturer(lecturer: Lecturer):
    lecturer_collection.insert_one(dict(lecturer))
    raise HTTPException(status_code=200, detail="استاد جدید با موفقیت ثبت شد")


# Update -> lecturer
@myRouter.put("/lecturer/update/{lid}")
async def update_lecturer(lid: str, lecturer: Lecturer):
    if not lecturer_collection.find_one({"_id": ObjectId(lid)}):
        raise HTTPException(status_code=404, detail=f"استادی با شماره استادی {lid} یافت نشد")

    lecturer_collection.update_one({"_id": ObjectId(lid)}, {"$set": dict(lecturer)})
    return {"message": "اطلاعات استاد با موفقیت به‌روزرسانی شد"}


# Delete -> lecturer
@myRouter.delete("/lecturer/delete/{lid}")
async def delete_lecturer(lid: str):
    if not lecturer_collection.find_one({"_id": ObjectId(lid)}):
        raise HTTPException(status_code=404, detail=f"استاد با شماره استادی {lid} یافت نشد")

    lecturer_collection.delete_one({"_id": ObjectId(lid)})
    return {"message": "استاد با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------

# Read (SELECT) -> course
@myRouter.get("/course/select/")
async def read_course():
    courses = course_collection.find()
    return list_serial_course(courses)


# Create (INSERT) -> course
@myRouter.post("/course/create/")
async def create_course(course: Course):
    course_collection.insert_one(dict(course))
    raise HTTPException(status_code=200, detail="درس جدید با موفقیت ثبت شد")


# Update -> course
@myRouter.put("/course/update/{cid}")
async def update_course(cid: str, course: Course):
    if not course_collection.find_one({"_id": ObjectId(cid)}):
        raise HTTPException(status_code=404, detail=f"درسی با شماره درسی {cid} یافت نشد")

    course_collection.update_one({"_id": ObjectId(cid)}, {"$set": dict(course)})
    return {"message": "اطلاعات درس با موفقیت به‌روزرسانی شد"}


# Delete -> course
@myRouter.delete("/course/delete/{cid}")
async def delete_course(cid: str):
    if not course_collection.find_one({"_id": ObjectId(cid)}):
        raise HTTPException(status_code=404, detail=f"درس با شماره درسی {cid} یافت نشد")

    course_collection.delete_one({"_id": ObjectId(cid)})
    return {"message": "درس با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------


# Read (SELECT) -> CourseRegister
@myRouter.get("/course_register/select/")
async def read_course_register():
    course_registers = courseRegister_collection.find()
    return list_serial_course_register(course_registers)


# Create (INSERT) -> CourseRegister
@myRouter.post("/course_register/create/")
async def create_course_register(course_register: CourseRegister):
    courseRegister_collection.insert_one(dict(course_register))
    raise HTTPException(status_code=200, detail="ثبت ‌نام درس جدید با موفقیت انجام شد")


# Update -> CourseRegister
@myRouter.put("/course_register/update/{crid}")
async def update_course_register(crid: str, course_register: CourseRegister):
    if not courseRegister_collection.find_one({"_id": ObjectId(crid)}):
        raise HTTPException(status_code=404, detail=f"ثبت نام درسی با شماره {crid} یافت نشد")

    courseRegister_collection.update_one({"_id": ObjectId(crid)}, {"$set": dict(course_register)})
    return {"message": "اطلاعات ثبت‌ نام با موفقیت به‌ روزرسانی شد"}


# Delete -> CourseRegister
@myRouter.delete("/course_register/delete/{crid}")
async def delete_course_register(crid: str):
    if not courseRegister_collection.find_one({"_id": ObjectId(crid)}):
        raise HTTPException(status_code=404, detail="ثبت ‌نام مورد نظر یافت نشد!")

    courseRegister_collection.delete_one({"_id": ObjectId(crid)})
    return {"message": "ثبت ‌نام با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------


# Read (SELECT) -> PresentedCourses
@myRouter.get("/presented_course/select/")
async def read_presented_course():
    presented_courses = presentedCourses_collection.find()
    return list_serial_presented_courses(presented_courses)


# Create (INSERT) -> PresentedCourse
@myRouter.post("/presented_course/create/")
async def create_presented_course(presented_course: PresentedCourses):
    presentedCourses_collection.insert_one(dict(presented_course))
    raise HTTPException(status_code=200, detail="درس ارائه ‌شده جدید با موفقیت ثبت شد")


# Update -> PresentedCourse
@myRouter.put("/presented_course/update/{pcid}")
async def update_presented_course(pcid: str, presented_course: PresentedCourses):
    if not presentedCourses_collection.find_one({"_id": ObjectId(pcid)}):
        raise HTTPException(status_code=404, detail=f"درس ارائه ‌شده با شماره {pcid} یافت نشد")

    presentedCourses_collection.update_one({"_id": ObjectId(pcid)}, {"$set": dict(presented_course)})
    return {"message": "اطلاعات درس ارائه‌ شده با موفقیت به ‌روزرسانی شد"}


# Delete -> PresentedCourse
@myRouter.delete("/presented_course/delete/{pcid}")
async def delete_presented_course(pcid: str):
    if not presentedCourses_collection.find_one({"_id": ObjectId(pcid)}):
        raise HTTPException(status_code=404, detail="درس ارائه ‌شده مورد نظر یافت نشد!")

    presentedCourses_collection.delete_one({"_id": ObjectId(pcid)})
    return {"message": "درس ارائه ‌شده با موفقیت حذف شد"}

