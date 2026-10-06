from fastapi import APIRouter, Response

from controllers.productController import (
    create_student_controller,
    get_students_controller,
    get_student_by_id_controller,
    update_student_controller,
    delete_student_controller
)

from models.productModel import Student


studentRouter = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Create Student
@studentRouter.post("/create")
def create_student(student: Student, response: Response):
    return create_student_controller(student, response)


# Get All Students
@studentRouter.get("/all")
def get_students(response: Response):
    return get_students_controller(response)


# Get Student by ID
@studentRouter.get("/{student_id}")
def get_student(student_id: int, response: Response):
    return get_student_by_id_controller(student_id, response)


# Update Student
@studentRouter.put("/{student_id}")
def update_student(
    student_id: int,
    student: Student,
    response: Response
):
    return update_student_controller(
        student_id,
        student,
        response
    )


# Delete Student
@studentRouter.delete("/{student_id}")
def delete_student(
    student_id: int,
    response: Response
):
    return delete_student_controller(
        student_id,
        response
    )
