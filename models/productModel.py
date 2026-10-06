from pydantic import BaseModel


class Student(BaseModel):
    id: int | None = None
    name: str
    email: str
    course: str
    semester: int
