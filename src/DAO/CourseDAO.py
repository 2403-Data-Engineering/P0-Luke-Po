
from Model import Student
from Model import Professor
from Model.Course import Course
from DAO.StudentDAO import StudentDAO
from DAO.ProfessorDAO import ProfessorDAO
from Database import db_connection_manager
from mysql.connector.cursor import MySQLCursor
class CourseDAO:
    """Data Access Object for Course entities."""
    
    def get_all_courses(self) -> list[Course]:
        """Retrieve all courses in a list."""
        course_list = []
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM course"
            cursor.execute(sql)
            for row in cursor:
                course_list.append(row)
            connection.close()
        return course_list
            
    def get_enrollment_database(self) -> list[int]:
        enrollments = []
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM enrollment"
            cursor.execute(sql)
            for row in cursor:
                enrollments.append(row)
            connection.close()
        return enrollments
    
    def is_course_students_valid(self, course: Course) -> bool:
        return True
        # database_students = map(lambda s:s.get_student_id(), StudentDAO().get_all_students())
        # for student in course.get_students():
        #     if (student.get_student_id() not in database_students):
        #         return False
        # return True
    
    def add_student_to_course(self, student_id: int, course_id: int) -> None:
        enrollment_id_str = str(student_id) + str(course_id)
        enrollment_id = int(enrollment_id_str) #enrollment id is made of student_id then course_id
        if (StudentDAO().database_contains_student(student_id)): #if student database already does not have student
            return
        elif (enrollment_id in self.get_enrollment_database()): #if enrollment database doesn't already have the student
            return
        else:
            with db_connection_manager.get_connection() as connection:
                cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
                cursor.execute("INSERT INTO enrollment (student_id, course_id) VALUES (%(student_id)s, %(course_id)s)", {'student_id': student_id, 'course_id': course_id})
                # put it into the database
                
    def remove_student_from_course(self, student_id: int, course_id: int) -> None:
        enrollment_id_str = str(student_id) + str(course_id)
        enrollment_id = int(enrollment_id_str) #enrollment id is made of student_id then course_id
        if (StudentDAO().database_contains_student(student_id)): #if student database already does not have student
            return
        elif (enrollment_id in self.get_enrollment_database()): #if enrollment database doesn't already have the student
            return
        else:
            with db_connection_manager.get_connection() as connection:
                cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
                cursor.execute("DELETE FROM enrollment WHERE student_id = %(student_id)s AND course_id = %(course_id)s)", {'student_id': student_id, 'course_id': course_id})
                # put it into the database
            
    
    def get_course_by_id(self, course_id: int) -> Course:
        """Retrieve a course by its ID."""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM course WHERE id = %s"
            cursor.execute(sql, [course_id])
        return cursor.fetchone() #type: ignore
    
    def create_course(self, course_data: Course) -> None:
        course_name = course_data.get_name()
        course_professor_id = course_data.get_professor().get_professor_id() #int which is foreign key
        course_students = course_data.get_students()
        if (ProfessorDAO().database_contains_professor(course_professor_id) and self.is_course_students_valid(course_data)): #if the prof is in the database and all students within the course are valid, then ok to create
            """Create a new course."""
            with db_connection_manager.get_connection() as connection:
                cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
                # sql = "INSERT INTO course (course_data) VALUES (%(course_data)s)", {"course_data": course_data}
                cursor.execute("INSERT INTO course (name, professor_id) VALUES (%(name)s, %(professor_id)s)", {'name': course_name, 'professor_id': course_professor_id})
                new_id = cursor.lastrowid
                course_data.set_course_id(new_id)
                for student in course_students: #for every student listed in the new course, add that pair into the enrollment table
                    cursor.execute("INSERT INTO enrollment (student_id, course_id) VALUES (%(student_id)s, %(course_id)s)", {'student_id': student.get_student_id(), 'course_id': new_id})
            
    
    def update_course(self, course_id: int, course_data: Course) -> None:
        course_name = course_data.get_name()
        course_students = course_data.get_students()
        course_professor_id = course_data.get_professor().get_professor_id()
        """Update an existing course by its ID"""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("UPDATE course SET name = %(course_name)s, professor = %(course_professor)s WHERE id = %(id)s", {'course_name' : course_name, 'course_professor_id' : course_professor_id, 'id' : course_id })

            # now add students to course but only if they are in the student database
            for student in course_students: # if student-course relationship is already in the enrollment table, then I think the INSERT INTO will just replace that
                if(StudentDAO().database_contains_student(student.get_student_id()) and ProfessorDAO().database_contains_professor(course_professor_id)):
                    cursor.execute("INSERT INTO enrollment (student_id, course_id) VALUES (%(student_id)s, %(course_id)s)", {'student_id': student.get_student_id(), 'course_id': course_id})
                else: #don't do anything if either doesn't exist in database
                    pass
                    
    
    def delete_course(self, course_id: int) -> None:
        """Delete a course by its ID."""
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("DELETE FROM course WHERE id = %s", [course_id])
    
    
    
    def student_enrollment_courses(self, student_id: int) -> list[Course]:
        courses_enrolled = []
        courses = []
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("SELECT * FROM enrollment WHERE student_id = %s", [student_id]) #get all courses where found student_id
            courses_enrolled = cursor.fetchall() # type: ignore
            print(courses_enrolled)
        for c in courses_enrolled:
            #get the individual course ids from the enrollments table, and get the courses from those course_ids
            courses.append(self.get_course_by_id(c.__getattribute__('course_id')))
        return courses

    

        
    
