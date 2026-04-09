from Controller.Menus.MainMenu import MainMenu
from Model.ParseJSON import ParseJSON
from Service.CourseService import CourseService
from Model.Course import Course
from Model.Student import Student
from Model.Professor import Professor
from .Menu import Menu
import json
class CourseMenu(Menu):
    def __init__(self, controller):
        super().__init__(controller)
        self.course_controller = self.controller.course_controller
        
    def render(self) -> None:
        print("Welcome to the course Menu. Please select an option:")
        print("1. View all coursees")
        print("2. Create a course")
        print("3. View a course")
        print("4. Update a course")
        print("5. Delete a course")
        print("6. Enroll a Student from a Course")
        print("7. Unenroll a Student from a Course")
        print("8. See all Students Enrolled in a Class")
        print("9. View all Courses a student is enrolled in")
        print("10. Go Back to the Main Menu")
        
        user_input = input().lower()
        
        match user_input:
            case '1':
                print("Viewing all coursees...")
                #need to call the FullRegistrationController's course service
                courses = self.course_controller.get_all_courses()
                for c in courses:
                    print(c)
                self.controller.navigate(CourseMenu(self.controller))
            case '2':
                print("Creating a Course...")
                print("Enter a the course you want to create in the format required (JSON):")
                print("""{"id": 0, "name": "Dummy Class", "students": [{"id": 0, "first_name": "Dummy", "last_name": "Student", "year": 0, "major": "Physics", "email": "dummys@gmail.com"}], "professor": {"id": 1, "first_name": "Dummy", "last_name": "Professor", "department": "Department", "email": "dummyprofessor@gmail.com"}}""")

                course_input = input()
                #TODO: Still need to check whether every id is valid and everything is valid                
                try:
                    course : Course = ParseJSON.parse_course(course_input)
                    self.course_controller.create_course(course)
                    print("Successfully created the Course in the Database!")
                except json.JSONDecodeError:
                    print("Unable to Parse, Navigating back to the Course Menu")
                except Exception:
                    print("An Error Occurred, Navigating back to Course Menu")
                self.controller.navigate(CourseMenu(self.controller))
            case '3':
                print("Viewing a Specific Course...")
                print("Enter the course id of the course you want to view:")
                course_id_input = int(input()) #get the course_id
                
                course : Course = self.course_controller.get_course_by_id(course_id_input) #get the course from its id
                # if (course is None):
                #     print("An Error Occured, Navigating back to the Course Menu")
                # else:
                #     course.print_course()
                print(course)
                self.controller.navigate(CourseMenu(self.controller))
            case '4':
                print("Updating a Course...")
                print("Enter the course you want to update in the format required (JSON):")
                print("""{"id": 0, "name": "Dummy Class", "students": [{"id": 0, "first_name": "Dummy", "last_name": "Student", "year": 0, "major": "Physics", "email": "dummys@gmail.com"}], "professor": {"id": 0, "first_name": "Dummy", "last_name": "Professor", "department": "Department", "email": "dummyprofessor@gmail.com"}}""")
                course_input = input()
                
                course : Course = ParseJSON.parse_course(course_input)
                self.course_controller.update_course(course)
                print("Update Complete!")
                
                # try:
                #     course : Course = ParseJSON.parse_course(course_input)
                #     self.course_controller.update_course(course)
                #     print("Update Complete!")
                # except json.JSONDecodeError:
                #     print("Unable to Parse, Navigating back to the Course Menu")
                # except Exception:
                #     print("An Error Occured, Navigating back to the Course Menu")
                
                self.controller.navigate(CourseMenu(self.controller))
            #only need id for deletion
            case '5':
                print("Deleting a Course...")
                print("Enter the course id of the course you want to delete:")
                print("Course ID")
                course_input = input()
                self.course_controller.get_course_service().delete_course(int(course_input))
                self.controller.navigate(CourseMenu(self.controller))
            case '6':
                print("Enter the id of the student you want to enroll")
                
                student_id_input = int(input())
                print("enter the id of the course you want the student to be enrolled in")
                course_id_input = int(input())
                self.course_controller.add_student_to_course(student_id_input, course_id_input)
                print("Student enrolled!")
                
                # try:
                #     print("Enter the id of the student you want to enroll")
                #     student_id_input = int(input())
                #     print("enter the id of the course you want the student to be enrolled in")
                #     course_id_input = int(input())
                #     self.course_controller.add_student_to_course(student_id_input, course_id_input)
                #     print("Student enrolled!")
                # except Exception:
                #     print("error enrolling student")
                self.controller.navigate(CourseMenu(self.controller))
            case '7':
                print("Enter the id of the student you want to unenroll")
                
                student_id_input = int(input())
                print("enter the id of the course you want the student to be unenrolled in")
                course_id_input = int(input())
                self.course_controller.remove_student_from_course(student_id_input, course_id_input)
                print("Student unenrolled!")
                
                # try:
                #     print("Enter the id of the student you want to unenroll")
                #     student_id_input = int(input())
                #     print("enter the id of the course you want the student to be unenrolled in")
                #     course_id_input = int(input())
                #     self.course_controller.remove_student_from_course(student_id_input, course_id_input)
                #     print("Student unenrolled!")
                # except Exception:
                #     print("error unenrolling student")
                self.controller.navigate(CourseMenu(self.controller))
            case '8':
                print("View all the students in a Course")
                
                print("Enter the id of the course you want to view")
                course_id_input = int(input())
                students = self.course_controller.course_student_list(course_id_input)
                print("Successfully found course's enrollments")
                for student in students:
                    print('\n')
                    print(student)

                self.controller.navigate(CourseMenu(self.controller))
            case '9':
                print("Viewing all classes a student has enrolled in")
                print("Enter the id of the student you want to view")
                
                student_id_input = int(input())
                courses = self.course_controller.student_enrollment_courses(student_id_input)
                
                print("Successfully found student enrollment courses")
                # print(courses)
                
                print('\n')
                for course in courses:
                    print(course.print_course())
                print('\n')
                # try:
                #     print("Enter the id of the student you want to view")
                #     student_id_input = int(input())
                #     self.course_controller.student_enrollment_courses(student_id_input)
                #     print("Successfully found student enrollment courses")
                # except Exception:
                #     print("error finding student enrollment courses")
                self.controller.navigate(CourseMenu(self.controller))
            case '10':
                self.controller.navigate(MainMenu(self.controller))
            case 'q':
                self.controller.quit()
            case _:
                print("Invalid choice, please try again.")
                self.controller.navigate(CourseMenu(self.controller))
                
    # def render_course(self) -> None:
    #     print("Welcome to the Specific Course Menu. Please select an option:")
    #     print("1. Add a student to this course")
    #     print("2. Remove a Student from this course")
    #     print("3. Go Back to the Main Menu")
    #     user_input = input().lower
    #     match user_input:
    #         case '1':
    #             #TODO
    #             pass
    #         case '2':
    #             #TODO
    #             pass
    #         case '3':
    #             from Controller.Menus.MainMenu import MainMenu
    #             self.controller.navigate(MainMenu(self.controller))
    #         case _:
    #             print("Invalid choice, please try again")
    #             self.controller.navigate(CourseMenu(self.controller))
        
