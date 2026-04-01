from .Menu import Menu
class StudentMenu(Menu):
    def render(self) -> None:
        print("Welcome to the Student Menu. Please select an option:")
        print("1. View All Students")
        print("2. Create a Student")
        print("3. View a Student")
        print("4. Update a Student")
        print("5. Delete a Student")
        print("6. Go Back to the Main Menu")