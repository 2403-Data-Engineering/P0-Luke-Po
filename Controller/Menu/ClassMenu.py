from .menu import Menu
class ClassMenu(Menu):
    def render(self) -> None:
        print("Welcome to the Class Menu. Please select an option:")
        print("1. View all Classes")
        print("2. Create a Class")
        print("3. View a Class")
        print("4. Update a Class")
        print("5. Delete a Class")
        print("6. Go Back to the Main Menu")