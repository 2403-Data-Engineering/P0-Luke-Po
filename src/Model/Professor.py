class Professor:
    def __init__(self, id: int, first_name: str, last_name: str, department: str, email: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        
    # Getters
    def getProfessorId(self) -> int:
        return self.id
    def getFirstName(self) -> str:
        return self.first_name
    def getLastName(self) -> str:
        return self.last_name
    def getDepartment(self) -> str:
        return self.department
    def getEmail(self) -> str:
        return self.email
    
    # Setters
    def setProfessorId(self, id: int) -> None:
        self.id = id
    def setFirstName(self, first_name: str) -> None:
        self.first_name = first_name
    def setLastName(self, last_name: str) -> None:
        self.last_name = last_name
    def setDepartment(self, department: str) -> None:
        self.department = department
    def setEmail(self, email: str) -> None:
        self.email = email