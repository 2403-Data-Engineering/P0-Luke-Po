from Controller.Menus.MainMenu import MainMenu
from ...Service.ClassService import ClassService
from FullRegistrationController import FullRegistrationController


from .Menu import Menu
class ClassMenu(Menu):
    def __init__(self, controller):
        super().__init__(controller)
        self.class_controller = self.controller.class_controller
        
    def render(self) -> None:
        print("Welcome to the Class Menu. Please select an option:")
        print("1. View all Classes")
        print("2. Create a Class")
        print("3. View a Class")
        print("4. Update a Class")
        print("5. Delete a Class")
        print("6. Go Back to the Main Menu")
        
        user_input = input().lower()
        
        match user_input:
            case '1':
                print("Viewing all Classes...")
                #need to call the FullRegistrationController's class service
                classes = self.class_controller.get_class_service().get_all_classes()
                for c in classes:
                    print(c)
            case '2':
                print("Creating a Class...")
                print("Enter a the class you want to create in the format required:")
                print("Class Name, Students, Professor ID")
                
            case '3':
                print("Viewing a Specific Class...")
            case '4':
                print("Updating a Class...")
            case '5':
                print("Deleting a Class...")
            case '6':
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")
        