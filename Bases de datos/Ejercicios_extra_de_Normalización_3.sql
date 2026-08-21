-- =====================================================================
-- EJERCICIO 3: APPOINTMENTS / PATIENTS / DOCTORS
-- =====================================================================
--
-- ESTADO INICIAL
-- Appointment ID  Patient Name  Patient Phone  Doctor Name  Specialty     Date        Time
-- A01             Diana Vargas  8888-1111      Dr. Soto     Pediatría     2024-08-01  10:00 AM
-- A02             Diana Vargas  8888-1111      Dr. Soto     Pediatría     2024-08-10  10:00 AM
-- A03             Edwin Mora    8999-2222      Dr. Mora     Cardiología   2024-08-05  01:00 PM
--
-- Diagnóstico: a diferencia de los ejercicios anteriores, Appointment
-- ID YA es único por fila (A01, A02, A03 no se repiten) -> no hace
-- falta llave compuesta, ya se cumple 1FN de forma directa.
--
-- 1FN: Appointment ID como llave primaria simple. Sin grupos
--      repetidos ni celdas con varios valores.
-- 2FN: como la llave no es compuesta, 2FN se cumple automáticamente
--      al estar en 1FN (no aplica el análisis de dependencia parcial).
-- 3FN: sí hay dependencias transitivas que resolver:
--        - Patient Phone depende de Patient Name (del paciente), no
--          directamente de Appointment ID -> se separa PATIENTS.
--        - Specialty depende de Doctor Name (del doctor), no
--          directamente de Appointment ID -> se separa DOCTORS.
--      APPOINTMENTS queda con referencias (PATIENT_ID, DOCTOR_ID) en
--      vez de duplicar esos datos.
--
-- Esquema final: PATIENTS, DOCTORS, APPOINTMENTS

CREATE TABLE PATIENTS (
    PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PATIENT_NAME VARCHAR(100) NOT NULL,
    PATIENT_PHONE VARCHAR(20) NOT NULL
);

CREATE TABLE DOCTORS (
    DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DOCTOR_NAME VARCHAR(100) NOT NULL,
    SPECIALTY VARCHAR(100) NOT NULL
);

CREATE TABLE APPOINTMENTS (
    APPOINTMENT_ID VARCHAR(10) PRIMARY KEY,
    PATIENT_ID INTEGER NOT NULL,
    DOCTOR_ID INTEGER NOT NULL,
    APPOINTMENT_DATE DATE NOT NULL,
    APPOINTMENT_TIME VARCHAR(10) NOT NULL,
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENTS(PATIENT_ID),
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(DOCTOR_ID)
);

-- =====================================================================
-- DATOS
-- =====================================================================

INSERT INTO PATIENTS (PATIENT_ID, PATIENT_NAME, PATIENT_PHONE) VALUES (1, 'Diana Vargas', '8888-1111');
INSERT INTO PATIENTS (PATIENT_ID, PATIENT_NAME, PATIENT_PHONE) VALUES (2, 'Edwin Mora', '8999-2222');

INSERT INTO DOCTORS (DOCTOR_ID, DOCTOR_NAME, SPECIALTY) VALUES (1, 'Dr. Soto', 'Pediatría');
INSERT INTO DOCTORS (DOCTOR_ID, DOCTOR_NAME, SPECIALTY) VALUES (2, 'Dr. Mora', 'Cardiología');

INSERT INTO APPOINTMENTS (APPOINTMENT_ID, PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, APPOINTMENT_TIME) VALUES ('A01', 1, 1, '2024-08-01', '10:00 AM');
INSERT INTO APPOINTMENTS (APPOINTMENT_ID, PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, APPOINTMENT_TIME) VALUES ('A02', 1, 1, '2024-08-10', '10:00 AM');
INSERT INTO APPOINTMENTS (APPOINTMENT_ID, PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, APPOINTMENT_TIME) VALUES ('A03', 2, 2, '2024-08-05', '01:00 PM');

-- =====================================================================
-- VERIFICACIÓN
-- =====================================================================

SELECT * FROM PATIENTS;
SELECT * FROM DOCTORS;
SELECT * FROM APPOINTMENTS;