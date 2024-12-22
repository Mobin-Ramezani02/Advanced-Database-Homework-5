from sqlalchemy.orm import Session
import models
import schemas

# خواندن کاربر با National_ID
def get_user(db: Session, national_id: int):
    return db.query(models.User).filter(models.User.National_ID == national_id).first()

# خواندن کاربر با ایمیل
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.Username == email).first()

# خواندن لیست کاربران (با قابلیت صفحه‌بندی)
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# ایجاد کاربر جدید
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        First_Name=user.First_Name,
        Last_Name=user.Last_Name,
        Phone=user.Phone,
        National_ID=user.National_ID,
        Role=user.Role,
        Username=user.Username,
        Password=user.Password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# حذف کاربر با National_ID
def delete_user(db: Session, national_id: int):
    db_user = db.query(models.User).filter(models.User.National_ID == national_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
