CREATE DATABASE UniversityDB; 
USE UniversityDB; 
-- Students Table 
CREATE TABLE Students ( 
student_id INT PRIMARY KEY, 
name VARCHAR(50), 
city VARCHAR(50) 
); 
-- Courses Table 
CREATE TABLE Courses ( 
course_id INT PRIMARY KEY, 
course_name VARCHAR(50), 
credits INT 
); 
-- Enrollments Table 
CREATE TABLE Enrollments ( 
enroll_id INT PRIMARY KEY, 
student_id INT, 
course_id INT, 
grade CHAR(2), 
FOREIGN KEY (student_id) REFERENCES Students(student_id), FOREIGN KEY (course_id) REFERENCES Courses(course_id) ); 
-- Insert Students 
INSERT INTO Students VALUES 
(1, 'Rahul', 'Mumbai'), 
(2, 'Priya', 'Delhi'), 
(3, 'Arjun', 'Bengaluru'), 
(4, 'Neha', 'Hyderabad'), 
(5, 'Vikram', 'Chennai'); 
-- Insert Courses 
INSERT INTO Courses VALUES 
(101, 'Mathematics', 4), 
(102, 'Computer Science', 3), 
(103, 'Economics', 2), 
(104, 'History', 3); 
-- Insert Enrollments 
INSERT INTO Enrollments VALUES 
(1, 1, 101, 'A'), 
(2, 1, 102, 'B'), 
(3, 2, 103, 'A'), 
(4, 3, 101, 'C'),
(5, 4, 102, 'B'), 
(6, 5, 104, 'A'); 

DELIMITER $$
CREATE PROCEDURE GetAllStudents()
BEGIN
    -- Selects all columns and all rows from the Students table
    SELECT 
        student_id, 
        name, 
        city
    FROM 
        Students;
END$$
DELIMITER ;
CALL GetAllStudents();

DELIMITER $$
CREATE PROCEDURE GetAllCourses()
BEGIN
    -- Selects course_id, course_name, and credits from the Courses table
    SELECT 
        course_id, 
        course_name, 
        credits
    FROM 
        Courses;
END$$
DELIMITER ;

CALL GetAllCourses();

DELIMITER $$
CREATE PROCEDURE GetStudentsByCity(
    IN city_name VARCHAR(50)
)
BEGIN
    -- Selects students where the city matches the input parameter
    SELECT 
        student_id, 
        name, 
        city
    FROM 
        Students
    WHERE 
        city = city_name;
END$$
DELIMITER ;

CALL GetStudentsByCity('Mumbai');

DELIMITER $$
CREATE PROCEDURE GetStudentsWithCourses()
BEGIN
    SELECT 
        s.student_id, 
        s.name AS student_name, 
        c.course_name, 
        e.grade
    FROM 
        Students s
    INNER JOIN 
        Enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        Courses c ON e.course_id = c.course_id
    ORDER BY 
        s.name, c.course_name;
END$$
DELIMITER ;

CALL GetStudentsWithCourses();

DELIMITER $$
CREATE PROCEDURE GetStudentsByCourse(
    IN input_course_id INT
)
BEGIN
    SELECT 
        s.student_id, 
        s.name AS student_name, 
        c.course_name
    FROM 
        Students s
    INNER JOIN 
        Enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        Courses c ON e.course_id = c.course_id
    WHERE 
        c.course_id = input_course_id
    ORDER BY 
        s.name;
END$$
DELIMITER ;

CALL GetStudentsByCourse(102);

DELIMITER $$
CREATE PROCEDURE CountStudentsPerCourse()
BEGIN
    SELECT 
        c.course_name, 
        COUNT(e.student_id) AS student_count
    FROM 
        Courses c
    LEFT JOIN 
        Enrollments e ON c.course_id = e.course_id
    GROUP BY 
        c.course_name, c.course_id -- Group by c.course_id to ensure correctness if course_names weren't unique
    ORDER BY 
        student_count DESC, c.course_name;
END$$
DELIMITER ;

CALL CountStudentsPerCourse();

DELIMITER $$
CREATE PROCEDURE GetFullEnrollmentDetails()
BEGIN
    SELECT 
        s.student_id, 
        s.name AS student_name, 
        c.course_name, 
        e.grade
    FROM 
        Students s
    INNER JOIN 
        Enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        Courses c ON e.course_id = c.course_id
    ORDER BY 
        s.name, c.course_name;
END$$
DELIMITER ;

CALL GetFullEnrollmentDetails();

DELIMITER $$
CREATE PROCEDURE GetCoursesByStudent(
    IN input_student_id INT
)
BEGIN
    SELECT 
        c.course_id, 
        c.course_name, 
        c.credits,
        e.grade
    FROM 
        Students s
    INNER JOIN 
        Enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        Courses c ON e.course_id = c.course_id
    WHERE 
        s.student_id = input_student_id
    ORDER BY 
        c.course_name;
END$$
DELIMITER ;
CALL GetCoursesByStudent(1);

DELIMITER $$
CREATE PROCEDURE GetBestGradeInAnyCourse()
BEGIN
    SELECT 
        c.course_name,
        MAX(e.grade) AS highest_grade_achieved
    FROM 
        Courses c
    JOIN 
        Enrollments e ON c.course_id = e.course_id
    GROUP BY 
        c.course_name
    ORDER BY 
        highest_grade_achieved DESC, c.course_name
    LIMIT 1; -- Get only the top-ranked course/grade combination
END$$
DELIMITER ;
call GetBestGradeInAnyCourse();