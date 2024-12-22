from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base


class Student(Base):
    __tablename__ = "student"

    STID = Column(String, primary_key=True, nullable=False)
    FName = Column(String, nullable=False)
    LName = Column(String, nullable=False)
    Father = Column(String)
    Birth = Column(String)
    SerialID = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(String)
    CPhone = Column(String)
    HPhone = Column(String)
    Department = Column(String)
    Major = Column(String)
    Married = Column(Boolean)
    ID = Column(String, unique=True, nullable=False)


# ------------------------------------------------------------


class Lecturer(Base):
    __tablename__ = "lecturer"

    LID = Column(String, primary_key=True, nullable=False)
    FName = Column(String, nullable=False)
    LName = Column(String, nullable=False)
    ID = Column(String, unique=True, nullable=False)
    Department = Column(String)
    Major = Column(String)
    Birth = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(String)
    CPhone = Column(String)
    HPhone = Column(String)


# ------------------------------------------------------------


class Course(Base):
    __tablename__ = "course"

    CID = Column(String, primary_key=True)
    CName = Column(String, nullable=False)
    Department = Column(String, nullable=False)
    Credit = Column(Integer, nullable=False)

# ------------------------------------------------------------

class CourseRegister(Base):
    __tablename__ = "course_register"

    Credit = Column(Integer, nullable=False)
    Department = Column(String, nullable=False)
    CName = Column(String, nullable=False)
    FName = Column(String, nullable=False)
    LName = Column(String, nullable=False)
    STID = Column(String, ForeignKey("student.STID", ondelete="CASCADE"), primary_key=True)
    CID = Column(String, ForeignKey("course.CID", ondelete="CASCADE"), primary_key=True)

# ------------------------------------------------------------

class PresentedCourses(Base):
    __tablename__ = "presented_courses"

    CName = Column(String, nullable=False)
    Department = Column(String, nullable=False)
    Credit = Column(Integer, nullable=False)
    FName = Column(String, nullable=False)
    LName = Column(String, nullable=False)
    CID = Column(String, ForeignKey("course.CID", ondelete="CASCADE"), primary_key=True, nullable=False)
    LID = Column(String, ForeignKey("lecturer.LID", ondelete="CASCADE"), primary_key=True, nullable=False)