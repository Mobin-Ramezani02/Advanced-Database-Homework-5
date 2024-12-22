from pydantic import BaseModel, Field

class Student(BaseModel):
    FName: str = Field(max_length=50)
    LName: str = Field(max_length=50)
    Father: str = Field(max_length=50)
    Birth: str = Field(min_length=10, max_length=10)
    SerialID: str = Field(min_length=9, max_length=9)
    BornCity: str = Field(max_length=70)
    Address: str = Field(max_length=200)
    PostalCode: str = Field(min_length=10, max_length=10)
    CPhone: str = Field(min_length=11, max_length=11)
    HPhone: str = Field(min_length=11, max_length=11)
    Department: str = Field(max_length=70)
    Major: str = Field(max_length=70)
    Married: bool
    ID: str = Field(min_length=10, max_length=10)

    class Config:
        from_attributes = True

# ------------------------------------------------------------


class Lecturer(BaseModel):
    FName: str = Field(max_length=50)
    LName: str = Field(max_length=50)
    ID: str = Field(min_length=10, max_length=10)
    Department: str = Field(max_length=70)
    Major: str = Field(max_length=70)
    Birth: str = Field(min_length=10, max_length=10)
    BornCity: str = Field(max_length=70)
    Address: str = Field(max_length=200)
    PostalCode: str = Field(min_length=10, max_length=10)
    CPhone: str = Field(min_length=11, max_length=11)
    HPhone: str = Field(min_length=11, max_length=11)
    class Config:
        from_attributes = True

# ------------------------------------------------------------

class Course(BaseModel):
    CName: str = Field(max_length=25)
    Department: str = Field(max_length=70)
    Credit: int = Field(ge=1, le=4)
    class Config:
        from_attributes = True

# ------------------------------------------------------------

class CourseRegister(BaseModel):
    Credit: int = Field(ge=1, le=4)
    Department: str = Field(max_length=70)
    CName: str = Field(max_length=25)
    FName: str = Field(max_length=50)
    LName: str = Field(max_length=50)
    STID: str = Field(min_length=11, max_length=11)
    CID : str = Field(min_length=5, max_length=5)
    class Config:
        from_attributes = True

# ------------------------------------------------------------

class PresentedCourses(BaseModel):
    CName: str = Field(max_length=25)
    Department: str = Field(max_length=70)
    Credit: int = Field(ge=1, le=4)
    FName: str = Field(max_length=50)
    LName: str = Field(max_length=50)
    CID : str = Field(min_length=5, max_length=5)
    LID : str = Field(min_length=6, max_length=6)
    class Config:
        from_attributes = True
