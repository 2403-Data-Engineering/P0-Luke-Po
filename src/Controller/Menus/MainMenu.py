from .Menu import Menu





class MainMenu(Menu):
    def render(self) -> None:
        print("Hello, welcome to the University Registration System. Please select an option:")
        print("1. Professor Management")
        print("2. Student Management")
        print("3. Course Management")
        print("4. Reports")
        print("5. Exit")
        
        user_input: str = input().lower()
        
        match user_input:
            case '1':
                from .ProfessorMenu import ProfessorMenu
                self.controller.navigate(ProfessorMenu(self.controller))
            case '2':
                from .StudentMenu import StudentMenu
                self.controller.navigate(StudentMenu(self.controller))
            case '3':
                from .CourseMenu import CourseMenu
                self.controller.navigate(CourseMenu(self.controller))
            case '4':
                from .ReportsMenu import ReportsMenu
                self.controller.navigate(ReportsMenu(self.controller))
            case '5':
                self.controller.quit()
            case _:
                print("Invalid choice, please try again.")