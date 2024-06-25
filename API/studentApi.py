from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from Config.database import get_db
from .Utilities import studentdbutility
from .models.main import Student
# from ..Models import models

app = FastAPI()

@app.post("/student")
# Add response schema
def create_student(student: Student, db: Session = Depends(get_db)):
    db_std = studentdbutility.get_user_by_email_and_name(db, email= student.email, name = student.name)
    if(db_std):
        raise HTTPException(status_code=400, detail="Email already registered")
    return studentdbutility.create_std(db=db, student=student)

@app.get("/student/{reg_id}")
def get_student_by_id(reg_id: int, db: Session = Depends(get_db)):
    try:
        data = studentdbutility.get_std_by_id(reg_id, db)
        if not data:
            raise HTTPException(status_code=404, detail="Data not found for the registered ID")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error {e}")
    
@app.put("/student")
def update_student_info(data: Student, db: Session = Depends(get_db)):
    try:
        studentdbutility.update_student_details(data, db)
        return "Data Updated successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    
@app.delete("/student/{reg_id}")
def delete_student_details(reg_id: int, db: Session = Depends(get_db)):
    try:
        studentdbutility.delete_student(reg_id, db)
        return "Data Deleted successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")