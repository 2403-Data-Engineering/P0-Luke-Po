from Model.Course import Course
from Model.Student import Student
from Model.Professor import Professor
from Controller.CourseController import CourseController
from Controller.Menus.CourseMenu import CourseMenu
from mdutils.mdutils import MdUtils
from mdutils.tools.Table import Table

class PrintReport:
    @staticmethod
    def print_student_markdown_file(student: Student, enrollments: list[Course]) -> None:
        # student = self.student_controller.get_student_by_id(student_id)
        markdown_file = MdUtils(file_name="student_markdown_file", title="Student Enrollment Report")
        
        # Student summary first:
        name = student.get_first_name() + " " + student.get_last_name() #name of the student up top
        student_id_str : str = "Student ID: " + str(student.get_student_id())
        student_year: str = "Year: " + str(student.get_year())
        student_major : str = "Major: " + student.get_major()
        student_email : str = "Email: " + student.get_email()
        markdown_file.new_header(level=1, title=name)
        markdown_file.new_header(level=2, title=student_id_str)
        markdown_file.new_header(level=2, title=student_year)
        markdown_file.new_header(level=2, title=student_major)
        markdown_file.new_header(level=2, title=student_email)
        
        # next go through each enrollment and see if it's the student
        
        markdown_file.new_header(level=2, title='Courses being Taken:')
        
        for course in enrollments:
            markdown_file.new_line(course.get_name())
            markdown_file.new_line('Details:' + '\n' + course.print_course())
            markdown_file.new_line('\n')
        
        # markdown_file.new_list(enrollments)
        
        
        # courses = []
        
        # for course in course_controller.get_all_courses():
        #     student_ids = []
        #     # make the list of students in the class
        #     for student in course.get_students():
        #         student_ids.append(student.get_student_id())
        #         # check if student is in the class
        #     if (student_id in student_ids):
        #         courses.append(course)
                
        # markdown_file.new_list(courses)
        
                
        markdown_file.create_md_file() #print the file
        
    @staticmethod
    def print_professor_markdown_file(professor: Professor, all_courses: list[Course], course_controller: CourseController) -> None:
        professor_id = professor.get_professor_id()
        courses_taught = []
        for course in all_courses:
            if (course.get('professor_id') is professor_id):
                courses_taught.append(course)
        #now we have all the courses the professor teaches
        
        markdown_file = MdUtils(file_name="professor_markdown_file", title="Professor Enrollment Report")
        # Professor summary first:
        name = professor.get_first_name() + " " + professor.get_last_name() #name of the student up top
        professor_id_str : str = "Professor ID: " + str(professor_id)
        prof_department: str = "Department: " + str(professor.get_department())
        prof_email : str = "Email: " + professor.get_email()
        markdown_file.new_header(level=1, title=name)
        markdown_file.new_header(level=2, title=professor_id_str)
        markdown_file.new_header(level=2, title=prof_department)
        markdown_file.new_header(level=2, title=prof_email)
        markdown_file.new_header(level=2, title='Courses Taught: ')
        
        #go through all courses taught, and get the student_list for them and print it
        for c in courses_taught:
            markdown_file.new_header(level=3, title=(c.get('name') + ': '))
            student_strs = []
            #get the student list for the course
            for s in course_controller.course_student_list(c.get('id')):
                s_name = s.get('first_name') + s.get('last_name')
                s_id_str = str(s.get('id'))
                
                student_strs.append((s_name + '; ' + s_id_str)) #get all the students and their ids
                
            markdown_file.new_list(student_strs)
            
        markdown_file.create_md_file()