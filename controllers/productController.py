from fastapi import Response
from models.productModel import Student


students = []


def create_student_controller(student: Student, response: Response):
    new_id = len(students) + 1
    student.id = new_id

    students.append(student)

    response.status_code = 201

    return {
        "isSuccess": True,
        "message": "Student created successfully",
        "data": student
    }


def get_students_controller(response: Response):
    response.status_code = 200

    return {
        "isSuccess": True,
        "data": students
    }


def get_student_by_id_controller(student_id: int, response: Response):
    for student in students:
        if student.id == student_id:
            response.status_code = 200

            return {
                "isSuccess": True,
                "data": student
            }

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Student not found"
    }


def update_student_controller(
    student_id: int,
    student: Student,
    response: Response
):
    for i in range(len(students)):
        if students[i].id == student_id:
            student.id = student_id
            students[i] = student

            response.status_code = 200

            return {
                "isSuccess": True,
                "message": "Student updated successfully",
                "data": student
            }

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Student not found"
    }


def delete_student_controller(student_id: int, response: Response):
    for i in range(len(students)):
        if students[i].id == student_id:
            students.pop(i)

            response.status_code = 204

            return

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Student not found"
    }
