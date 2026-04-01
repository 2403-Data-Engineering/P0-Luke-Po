from .Menu import Menu
class ProfessorMenu(Menu):
    def render(self) -> None:
        print("Welcome to the Professor Menu. Please select an option:")
        print("1. View all Professors")
        print("2. Create a Professor")
        print("3. View a Professor")
        print("4. Update a Professor")
        print("5. Delete a Professor")
        print("6. Go Back to the Main Menu")