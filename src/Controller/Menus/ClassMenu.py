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
                self.controller.navigate(ClassMenu(self.controller))
            case '2':
                print("Creating a Class...")
                print("Enter a the class you want to create in the format required:")
                print("Class Name, Students, Professor ID")
                
                class_input = input().split(",")
                try:
                    self.class_controller.get_class_service().create_class(class_input[0], class_input[1], int(class_input[2]))
                except Exception as e:
                    print("Error creating class, going back to Class Menu")
                else:
                    print("Class created successfully!")
                self.controller.navigate(ClassMenu(self.controller))
            case '3':
                print("Viewing a Specific Class...")
                c = self.class_controller.get_class_service().get_class_by_id()
                print(c)
                self.controller.navigate(ClassMenu(self.controller))
            case '4':
                print("Updating a Class...")
                print("Enter the class you want to update in the format required:")
                print("Class ID, Class Name, Students, Professor ID")
                class_input = input().split(",")
                self.class_controller.get_class_service().update_class(int(class_input[0]), class_input[1], class_input[2], int(class_input[3]))
                self.controller.navigate(ClassMenu(self.controller))
            case '5':
                print("Deleting a Class...")
                print("Enter the class id of the class you want to delete:")
                print("Class ID")
                class_input = input()
                self.class_controller.get_class_service().delete_class(class_input)
                self.controller.navigate(ClassMenu(self.controller))
            case '6':
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")
                self.controller.navigate(ClassMenu(self.controller))
        