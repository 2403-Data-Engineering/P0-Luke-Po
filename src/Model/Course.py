from Model.Professor import Professor
from Model.Student import Student

class Course:
    def __init__(self, id: int=0, name: str="Dummy Class", students: list[Student]=[Student()], professor: Professor=Professor()):
        self.id = id
        self.name = name
        self.students = students
        self.professor = professor
    
    # Getters
    def getClassId(self) -> int:
        return self.id
    def getName(self) -> str:
        return self.name
    def getStudents(self) -> list[Student]:
        return self.students
    def getProfessor(self) -> Professor:
        return self.professor
    
    # Setters
    def setClassId(self, id: int) -> None:
        self.id = id
    def setName(self, name: str) -> None:
        self.name = name
    def setStudents(self, students: list[Student]) -> None:
        self.students = students
    def setProfessor(self, professor: Professor) -> None:
        self.professor = professor
    