class Professor:
    def __init__(self, id, first_name, last_name, department, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        
    # Getters
    def getProfessorId(self):
        return self.id
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getDepartment(self):
        return self.department
    def getEmail(self):
        return self.email
    # Setters
    def setProfessorId(self, id):
        self.id = id
    def setFirstName(self, first_name):
        self.first_name = first_name
    def setLastName(self, last_name):
        self.last_name = last_name
    def setDepartment(self, department):
        self.department = department
    def setEmail(self, email):
        self.email = email