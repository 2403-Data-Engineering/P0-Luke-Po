import json
from Model.Course import Course
from Model.Professor import Professor
from Model.Student import Student

class ParseJSON:
    
    @staticmethod
    def parse_professor(json_str: str) -> Professor:
        data = json.loads(json_str)
        return Professor(id=data.get("id", 0), first_name=data.get("firstname", "Dummy"), last_name=data.get("lastname", "Professor"), department=data.get("department", "Dummy Department"), email=data.get("email", "Dummy@email.com"))
    
    
    @staticmethod
    def parse_student(json_str: str) -> Student:
        data = json.loads(json_str)
        return Student(id=data.get("id", 0), first_name=data.get("firstname", "Dummy"), last_name=data.get("lastname", "Student"), year=data.get("year", 0), major=data.get("major", "Dummy Major"), email=data.get("email", "Dummy@email.com"))
    
    @staticmethod
    def parse_course(json_str: str) -> Course:
        data = json.loads(json_str)
        students = [Student(**s) for s in data.get("students", [])]
        print(students)
        professor = Professor(**data.get("professor", {}))
        return Course(id=data.get("id", 0), name=data.get("name", "Dummy Class"), students=students, professor=professor)
    

    

    