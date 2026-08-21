-- =====================================================================
-- EJERCICIO 1: EMPLOYEES / DEPARTMENTS / PROJECTS
-- =====================================================================
--
-- ESTADO INICIAL
-- Employee ID  Employee Name  Department   Department Phone  Project ID  Project Name    Project Budget
-- 201          Ana Rivera     IT           2222-2222         P001        Web App         50000
-- 201          Ana Rivera     IT           2222-2222         P002        API REST        25000
-- 202          Luis Mendez    Marketing    1111-1111         P003        Campaña TV      30000
--
-- Diagnóstico: Employee ID se repite -> llave compuesta (Employee ID,
-- Project ID). Relación muchos-a-muchos entre empleados y proyectos.
--
-- 1FN: llave compuesta (Employee ID, Project ID) resuelve la
--      identificación única de cada fila.
-- 2FN: Employee Name/Department/Department Phone dependen solo de
--      Employee ID; Project Name/Project Budget dependen solo de
--      Project ID -> se separan en EMPLOYEES, PROJECTS y una tabla de
--      relación EMPLOYEE_PROJECTS.
-- 3FN: dentro de EMPLOYEES, Department Phone depende de Department
--      (no directamente de Employee ID) -> dependencia transitiva ->
--      se separa DEPARTMENTS.
--
-- Esquema final: DEPARTMENTS, EMPLOYEES, PROJECTS, EMPLOYEE_PROJECTS

CREATE TABLE DEPARTMENTS (
    DEPARTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DEPARTMENT_NAME VARCHAR(50) UNIQUE NOT NULL,
    DEPARTMENT_PHONE VARCHAR(20) NOT NULL
);

CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID INTEGER PRIMARY KEY,
    EMPLOYEE_NAME VARCHAR(100) NOT NULL,
    DEPARTMENT_ID INTEGER NOT NULL,
    FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID)
);

CREATE TABLE PROJECTS (
    PROJECT_ID VARCHAR(10) PRIMARY KEY,
    PROJECT_NAME VARCHAR(100) NOT NULL,
    PROJECT_BUDGET DECIMAL(10,2) NOT NULL
);

CREATE TABLE EMPLOYEE_PROJECTS (
    EMPLOYEE_ID INTEGER NOT NULL,
    PROJECT_ID VARCHAR(10) NOT NULL,
    PRIMARY KEY (EMPLOYEE_ID, PROJECT_ID),
    FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEES(EMPLOYEE_ID),
    FOREIGN KEY (PROJECT_ID) REFERENCES PROJECTS(PROJECT_ID)
);

-- =====================================================================
-- DATOS
-- =====================================================================

INSERT INTO DEPARTMENTS (DEPARTMENT_ID, DEPARTMENT_NAME, DEPARTMENT_PHONE) VALUES (1, 'IT', '2222-2222');
INSERT INTO DEPARTMENTS (DEPARTMENT_ID, DEPARTMENT_NAME, DEPARTMENT_PHONE) VALUES (2, 'Marketing', '1111-1111');

INSERT INTO EMPLOYEES (EMPLOYEE_ID, EMPLOYEE_NAME, DEPARTMENT_ID) VALUES (201, 'Ana Rivera', 1);
INSERT INTO EMPLOYEES (EMPLOYEE_ID, EMPLOYEE_NAME, DEPARTMENT_ID) VALUES (202, 'Luis Mendez', 2);

INSERT INTO PROJECTS (PROJECT_ID, PROJECT_NAME, PROJECT_BUDGET) VALUES ('P001', 'Web App', 50000.00);
INSERT INTO PROJECTS (PROJECT_ID, PROJECT_NAME, PROJECT_BUDGET) VALUES ('P002', 'API REST', 25000.00);
INSERT INTO PROJECTS (PROJECT_ID, PROJECT_NAME, PROJECT_BUDGET) VALUES ('P003', 'Campaña TV', 30000.00);

INSERT INTO EMPLOYEE_PROJECTS (EMPLOYEE_ID, PROJECT_ID) VALUES (201, 'P001');
INSERT INTO EMPLOYEE_PROJECTS (EMPLOYEE_ID, PROJECT_ID) VALUES (201, 'P002');
INSERT INTO EMPLOYEE_PROJECTS (EMPLOYEE_ID, PROJECT_ID) VALUES (202, 'P003');

-- =====================================================================
-- VERIFICACIÓN
-- =====================================================================

SELECT * FROM DEPARTMENTS;
SELECT * FROM EMPLOYEES;
SELECT * FROM PROJECTS;
SELECT * FROM EMPLOYEE_PROJECTS;