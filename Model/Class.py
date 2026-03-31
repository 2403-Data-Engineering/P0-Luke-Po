class Class:
    def __init__(self, id, name, students, professor):
        self.id = id
        self.name = name
        self.students = students
        self.professor = professor
    
    # Getters
    def getClassId(self):
        return self.id
    def getName(self):
        return self.name
    def getStudents(self):
        return self.students
    def getProfessor(self):
        return self.professor
    
    # Setters
    def setClassId(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def setStudents(self, students):
        self.students = students
    def setProfessor(self, professor):
        self.professor = professor
    