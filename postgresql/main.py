from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas

# ایجاد جداول پایگاه داده
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# **************************************


# Read (SELECT) -> student
@app.get("/student/select/")
async def read_users(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return {"student": students}


# Create (INSERT) -> student
@app.post("/student/create/")
async def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    # ایجاد و ذخیره دانشجوی جدید
    db_student = models.Student(
        STID=student.STID,
        FName=student.FName,
        LName=student.LName,
        Father=student.Father,
        Birth=student.Birth,
        SerialID=student.SerialID,
        BornCity=student.BornCity,
        Address=student.Address,
        PostalCode=student.PostalCode,
        CPhone=student.CPhone,
        HPhone=student.HPhone,
        Department=student.Department,
        Major=student.Major,
        Married=student.Married,
        ID=student.ID,
    )

    db.add(db_student)
    db.commit()

    raise HTTPException(status_code=200, detail="دانشجوی جدید با موفقیت ثبت شد")


# Update -> student
@app.put("/student/update/{stid}")
async def update_student(stid: str, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.STID == stid)
    if not db_student.first():
        raise HTTPException(status_code=404, detail=f"دانشجو با شماره دانشجویی {stid} یافت نشد")

    db_student.update(student.dict(exclude_unset=True))
    db.commit()

    return {"message": "اطلاعات دانشجو با موفقیت به‌روزرسانی شد", "student": db_student.first()}


# Delete -> student
@app.delete("/student/delete/{stid}")
async def delete_student(stid: str, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.STID == stid).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="دانشجو یافت نشد!")

    db.delete(db_student)
    db.commit()

    return {"message": "دانشجو با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------


# Read (SELECT) -> lecturer
@app.get("/lecturer/select/")
async def read_lecturers(db: Session = Depends(get_db)):
    lecturers = db.query(models.Lecturer).all()
    return {"lecturer": lecturers}


# Create (INSERT) -> lecturer
@app.post("/lecturer/create/")
async def create_lecturer(lecturer: schemas.Lecturer, db: Session = Depends(get_db)):
    # ایجاد و ذخیره استاد جدید
    db_lecturer = models.Lecturer(
        LID=lecturer.LID,
        FName=lecturer.FName,
        LName=lecturer.LName,
        ID=lecturer.ID,
        Department=lecturer.Department,
        Major=lecturer.Major,
        Birth=lecturer.Birth,
        BornCity=lecturer.BornCity,
        Address=lecturer.Address,
        PostalCode=lecturer.PostalCode,
        CPhone=lecturer.CPhone,
        HPhone=lecturer.HPhone,
    )

    db.add(db_lecturer)
    db.commit()

    raise HTTPException(status_code=200, detail="استاد جدید با موفقیت ثبت شد")


# Update -> lecturer
@app.put("/lecturer/update/{lid}")
async def update_lecturer(lid: str, lecturer: schemas.LecturerUpdate, db: Session = Depends(get_db)):
    db_lecturer = db.query(models.Lecturer).filter(models.Lecturer.LID == lid)
    if not db_lecturer.first():
        raise HTTPException(status_code=404, detail=f"استاد با کد {lid} یافت نشد")

    db_lecturer.update(lecturer.dict(exclude_unset=True))
    db.commit()

    return {"message": "اطلاعات استاد با موفقیت به‌روزرسانی شد", "lecturer": db_lecturer.first()}


# Delete -> lecturer
@app.delete("/lecturer/delete/{lid}")
async def delete_lecturer(lid: str, db: Session = Depends(get_db)):
    db_lecturer = db.query(models.Lecturer).filter(models.Lecturer.LID == lid).first()
    if not db_lecturer:
        raise HTTPException(status_code=404, detail="استاد یافت نشد!")

    db.delete(db_lecturer)
    db.commit()

    return {"message": "استاد با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------


# Read (SELECT) -> course
@app.get("/course/select/")
async def read_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return {"course": courses}


# Create (INSERT) -> course
@app.post("/course/create/")
async def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    # ایجاد و ذخیره درس جدید
    db_course = models.Course(
        CID=course.CID,
        CName=course.CName,
        Department=course.Department,
        Credit=course.Credit,
    )

    db.add(db_course)
    db.commit()

    raise HTTPException(status_code=200, detail="درس جدید با موفقیت ثبت شد")


# Update -> course
@app.put("/course/update/{cid}")
async def update_course(cid: str, course: schemas.CourseUpdate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.CID == cid)
    if not db_course.first():
        raise HTTPException(status_code=404, detail=f"درس با کد {cid} یافت نشد")

    db_course.update(course.dict(exclude_unset=True))
    db.commit()

    return {"message": "اطلاعات درس با موفقیت به‌روزرسانی شد", "course": db_course.first()}


# Delete -> course
@app.delete("/course/delete/{cid}")
async def delete_course(cid: str, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.CID == cid).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="درس یافت نشد!")

    db.delete(db_course)
    db.commit()

    return {"message": "درس با موفقیت حذف شد"}


#---------------------------------------------------------------------------------------------

# Read (SELECT) -> CourseRegister
@app.get("/course_register/select/")
async def read_course_registers(db: Session = Depends(get_db)):
    course_registers = db.query(models.CourseRegister).all()
    return {"course_register": course_registers}


# Create (INSERT) -> CourseRegister
@app.post("/course_register/create/")
async def create_course_register(course_register: schemas.CourseRegister, db: Session = Depends(get_db)):
    db_course_register = models.CourseRegister(
        Credit=course_register.Credit,
        Department=course_register.Department,
        CName=course_register.CName,
        FName=course_register.FName,
        LName=course_register.LName,
        STID=course_register.STID,
        CID=course_register.CID,
    )

    db.add(db_course_register)
    db.commit()

    raise HTTPException(status_code=200, detail="ثبت ‌نام درس جدید با موفقیت انجام شد")


# Update -> CourseRegister
@app.put("/course_register/update/{stid}/{cid}")
async def update_course_register(stid: str,cid: str,course_register: schemas.CourseRegisterUpdate, db: Session = Depends(get_db)):
    db_course_register = db.query(models.CourseRegister).filter(models.CourseRegister.STID == stid, models.CourseRegister.CID == cid)
    if not db_course_register.first():
        raise HTTPException(
            status_code=404, detail=f"ثبت ‌نام با شماره دانشجویی {stid} و کد درس {cid} یافت نشد"
        )

    db_course_register.update(course_register.dict(exclude_unset=True))
    db.commit()

    return {"message": "اطلاعات ثبت‌ نام با موفقیت به‌ روزرسانی شد", "course_register": db_course_register.first()}


# Delete -> CourseRegister
@app.delete("/course_register/delete/{stid}/{cid}")
async def delete_course_register(stid: str, cid: str, db: Session = Depends(get_db)):
    db_course_register = db.query(models.CourseRegister).filter(models.CourseRegister.STID == stid, models.CourseRegister.CID == cid).first()
    if not db_course_register:
        raise HTTPException(status_code=404, detail="ثبت ‌نام مورد نظر یافت نشد!")

    db.delete(db_course_register)
    db.commit()

    return {"message": "ثبت ‌نام با موفقیت حذف شد"}

#---------------------------------------------------------------------------------------------

# Read (SELECT) -> PresentedCourses
@app.get("/presented_courses/select/")
async def read_presented_courses(db: Session = Depends(get_db)):
    presented_courses = db.query(models.PresentedCourses).all()
    return {"presented_course": presented_courses}


# Create (INSERT) -> PresentedCourses
@app.post("/presented_courses/create/")
async def create_presented_course(presented_course: schemas.PresentedCourses, db: Session = Depends(get_db)):
    db_presented_course = models.PresentedCourses(
        CName=presented_course.CName,
        Department=presented_course.Department,
        Credit=presented_course.Credit,
        FName=presented_course.FName,
        LName=presented_course.LName,
        CID=presented_course.CID,
        LID=presented_course.LID,
    )

    db.add(db_presented_course)
    db.commit()

    raise HTTPException(status_code=200, detail="درس ارائه ‌شده جدید با موفقیت ثبت شد")


# Update -> PresentedCourses
@app.put("/presented_courses/update/{lid}/{cid}")
async def update_presented_course(lid: str, cid: str, presented_course: schemas.PresentedCoursesUpdate, db: Session = Depends(get_db)):
    db_presented_course = db.query(models.PresentedCourses).filter(models.PresentedCourses.LID == lid, models.PresentedCourses.CID == cid)
    if not db_presented_course.first():
        raise HTTPException(status_code=404, detail=f"درس ارائه ‌شده با کد استاد {lid} و کد درس {cid} یافت نشد")

    db_presented_course.update(presented_course.dict(exclude_unset=True))
    db.commit()

    return {"message": "اطلاعات درس ارائه‌ شده با موفقیت به ‌روزرسانی شد", "presented_course": db_presented_course.first()}


# Delete -> PresentedCourses
@app.delete("/presented_courses/delete/{lid}/{cid}")
async def delete_presented_course(lid: str, cid: str, db: Session = Depends(get_db)):
    db_presented_course = db.query(models.PresentedCourses).filter(models.PresentedCourses.LID == lid, models.PresentedCourses.CID == cid).first()
    if not db_presented_course:
        raise HTTPException(status_code=404, detail="درس ارائه ‌شده مورد نظر یافت نشد!")

    db.delete(db_presented_course)
    db.commit()

    return {"message": "درس ارائه ‌شده با موفقیت حذف شد"}
