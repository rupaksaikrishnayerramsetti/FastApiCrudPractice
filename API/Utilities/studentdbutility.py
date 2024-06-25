from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.main import Student
from Models.models import Student as StudentMain

def get_user_by_email_and_name(db: Session, email: str, name: str):
    return db.query(StudentMain).filter(StudentMain.name==name, StudentMain.email==email).first()

def create_std(db: Session, student: Student):
    try:
        data = StudentMain(
            name = student.name,
            email = student.email,
            branch = student.branch,
            section = student.section
        )
        db.add(data)
        db.commit()
        db.close()
        return "Data inserted successfully"
    except Exception as e :
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    
def get_std_by_id(reg_id: int, db: Session):
    return db.query(StudentMain).filter(StudentMain.reg_id == reg_id).first()

def update_student_details(data: Student, db: Session):
    try:
        temp = db.query(StudentMain).filter(StudentMain.reg_id==data.reg_id, StudentMain.email==data.email).first()
        if not temp:
            raise HTTPException(status_code=404, detail="Data not found as per the student details")
        temp.name, temp.email, temp.branch, temp.section = data.name, data.email, data.branch, data.section
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    finally:
        db.close()

def delete_student(reg_id: int, db: Session):
    try:
        temp = db.query(StudentMain).filter(StudentMain.reg_id==reg_id).first()
        if not temp:
            raise HTTPException(status_code=404, detail="Data not found as per the student details")
        db.delete(temp)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    finally:
        db.close()   