class Student:
    def __init__(self, id, first_name, last_name, year, major, email, classes):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major
        self.email = email
        self.classes = classes
    
    # Getters
    def getStudentId(self):
        return self.id
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getYear(self):
        return self.year
    def getMajor(self):
        return self.major
    def getEmail(self):
        return self.email
    def getClasses(self):
        return self.classes
    
    # Setters
    def setStudentId(self, id):
        self.id = id
    def setFirstName(self, first_name):
        self.first_name = first_name
    def setLastName(self, last_name):
        self.last_name = last_name
    def setYear(self, year):
        self.year = year
    def setMajor(self, major):
        self.major = major
    def setEmail(self, email):
        self.email = email
    def setClasses(self, classes):
        self.classes = classes
    