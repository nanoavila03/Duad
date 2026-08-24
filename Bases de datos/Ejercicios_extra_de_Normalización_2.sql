-- =====================================================================
-- EJERCICIO 2: STUDENTS / COURSES / INSTRUCTORS
-- =====================================================================
--
-- ESTADO INICIAL
-- Student ID  Student Name  Course Code  Course Name  Instructor Name  Instructor Email
-- 301         Marco Gómez   CS101        Python I     Juan Pérez       juan@uni.edu
-- 301         Marco Gómez   CS102        Python II    Laura Rojas      laura@uni.edu
-- 302         Carla Ruiz    CS101        Python I     Juan Pérez       juan@uni.edu
--
-- Diagnóstico: Student ID se repite (301) y Course Code se repite
-- (CS101 en dos estudiantes distintos) -> llave compuesta (Student ID,
-- Course Code). Relación muchos-a-muchos entre estudiantes y cursos.
--
-- 1FN: llave compuesta (Student ID, Course Code).
-- 2FN: Student Name depende solo de Student ID; Course Name,
--      Instructor Name, Instructor Email dependen solo de Course Code
--      -> se separan en STUDENTS, un grupo "Course" y una tabla de
--      relación STUDENT_COURSES.
-- 3FN: dentro del grupo "Course", Instructor Email no depende
--      directamente de Course Code, depende de Instructor Name
--      (dependencia transitiva: Course Code -> Instructor Name ->
--      Instructor Email) -> se separa INSTRUCTORS. COURSES queda con
--      una referencia (INSTRUCTOR_ID) en vez de duplicar sus datos.
--
-- Nota: la relación Course -> Instructor es de UNO a MUCHOS (un
-- instructor da varios cursos, pero cada curso tiene un solo
-- instructor fijo en estos datos), así que basta una llave foránea en
-- COURSES; no hace falta una tabla de unión para eso. La tabla de
-- unión que sí es indispensable es STUDENT_COURSES, porque la
-- relación estudiante-curso sí es muchos-a-muchos (Marco toma dos
-- cursos, y CS101 tiene dos estudiantes).
--
-- Esquema final: INSTRUCTORS, COURSES, STUDENTS, STUDENT_COURSES

CREATE TABLE INSTRUCTORS (
    INSTRUCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    INSTRUCTOR_NAME VARCHAR(100) NOT NULL,
    INSTRUCTOR_EMAIL VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE COURSES (
    COURSE_CODE VARCHAR(10) PRIMARY KEY,
    COURSE_NAME VARCHAR(100) NOT NULL,
    INSTRUCTOR_ID INTEGER NOT NULL,
    FOREIGN KEY (INSTRUCTOR_ID) REFERENCES INSTRUCTORS(INSTRUCTOR_ID)
);

CREATE TABLE STUDENTS (
    STUDENT_ID INTEGER PRIMARY KEY,
    STUDENT_NAME VARCHAR(100) NOT NULL
);

CREATE TABLE STUDENT_COURSES (
    STUDENT_ID INTEGER NOT NULL,
    COURSE_CODE VARCHAR(10) NOT NULL,
    PRIMARY KEY (STUDENT_ID, COURSE_CODE),
    FOREIGN KEY (STUDENT_ID) REFERENCES STUDENTS(STUDENT_ID),
    FOREIGN KEY (COURSE_CODE) REFERENCES COURSES(COURSE_CODE)
);

-- =====================================================================
-- DATOS
-- =====================================================================

INSERT INTO INSTRUCTORS (INSTRUCTOR_ID, INSTRUCTOR_NAME, INSTRUCTOR_EMAIL) VALUES (1, 'Juan Pérez', 'juan@uni.edu');
INSERT INTO INSTRUCTORS (INSTRUCTOR_ID, INSTRUCTOR_NAME, INSTRUCTOR_EMAIL) VALUES (2, 'Laura Rojas', 'laura@uni.edu');

INSERT INTO COURSES (COURSE_CODE, COURSE_NAME, INSTRUCTOR_ID) VALUES ('CS101', 'Python I', 1);
INSERT INTO COURSES (COURSE_CODE, COURSE_NAME, INSTRUCTOR_ID) VALUES ('CS102', 'Python II', 2);

INSERT INTO STUDENTS (STUDENT_ID, STUDENT_NAME) VALUES (301, 'Marco Gómez');
INSERT INTO STUDENTS (STUDENT_ID, STUDENT_NAME) VALUES (302, 'Carla Ruiz');

INSERT INTO STUDENT_COURSES (STUDENT_ID, COURSE_CODE) VALUES (301, 'CS101');
INSERT INTO STUDENT_COURSES (STUDENT_ID, COURSE_CODE) VALUES (301, 'CS102');
INSERT INTO STUDENT_COURSES (STUDENT_ID, COURSE_CODE) VALUES (302, 'CS101');

-- =====================================================================
-- VERIFICACIÓN
-- =====================================================================

SELECT * FROM INSTRUCTORS;
SELECT * FROM COURSES;
SELECT * FROM STUDENTS;
SELECT * FROM STUDENT_COURSES;