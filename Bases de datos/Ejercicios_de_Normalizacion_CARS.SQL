-- =====================================================================
-- NORMALIZACIÓN: CARS (v2 — refinamiento adicional)
-- =====================================================================
--
-- Este archivo parte del esquema en 3FN de la primera entrega
-- (VEHICLES, OWNERS, VEHICLE_OWNERS) y resuelve dos dependencias
-- transitivas adicionales identificadas en la revisión:
--
-- ---------------------------------------------------------------------
-- PROBLEMA 1 — MAKE, MODEL, YEAR en VEHICLES
-- ---------------------------------------------------------------------
-- En el esquema anterior:
--
-- CREATE TABLE VEHICLES (
--     VIN VARCHAR(17) PRIMARY KEY,
--     MAKE VARCHAR(50) NOT NULL,
--     MODEL VARCHAR(50) NOT NULL,
--     YEAR INT NOT NULL,
--     COLOR VARCHAR(30)
-- );
--
-- MAKE, MODEL y YEAR no son atributos que dependan del VIN individual;
-- dependen del MODELO de vehículo (ej: "Honda Accord 2003"). Cada VIN
-- distinto que corresponda a un Honda Accord 2003 repetiría los mismos
-- tres valores. Con cientos de vehículos del mismo modelo, esa
-- información se duplicaría cientos de veces, y una corrección (por
-- ejemplo, un error de tipeo en "Accord") habría que aplicarla en
-- cada fila en vez de en un solo lugar. Esto es una dependencia
-- transitiva: VIN -> MODEL_ID -> (Make, Model, Year).
--
-- Solución: se extrae el modelo a su propia tabla, y VEHICLES solo
-- guarda una referencia (MODEL_ID) más lo que sí es propio de cada
-- vehículo físico individual (COLOR).
--
-- CREATE TABLE MODELS (
--     MODEL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
--     MAKE VARCHAR(50) NOT NULL,
--     MODEL VARCHAR(50) NOT NULL,
--     YEAR INT NOT NULL,
--     UNIQUE (MAKE, MODEL, YEAR)
-- );
--
-- CREATE TABLE VEHICLES (
--     VIN VARCHAR(17) PRIMARY KEY,
--     MODEL_ID INTEGER NOT NULL,
--     COLOR VARCHAR(30),
--     FOREIGN KEY (MODEL_ID) REFERENCES MODELS(MODEL_ID)
-- );
--
-- ¿Por qué COLOR se queda en VEHICLES y no se va a MODELS? Porque el
-- color es una característica del vehículo físico específico (dos
-- Honda Accord 2003 pueden ser de colores distintos), mientras que
-- Make/Model/Year son características del modelo en sí, compartidas
-- por todos los vehículos de esa línea.
--
-- ---------------------------------------------------------------------
-- PROBLEMA 2 — INSURANCE_COMPANY / INSURANCE_POLICY en VEHICLE_OWNERS
-- ---------------------------------------------------------------------
-- En el esquema anterior, INSURANCE_COMPANY e INSURANCE_POLICY vivían
-- como texto plano dentro de VEHICLE_OWNERS. Si varias combinaciones
-- vehículo-dueño comparten la misma aseguradora (por ejemplo, "ABC
-- Insurance" asegura a muchos dueños distintos), el nombre de la
-- compañía se repetiría en cada fila, con el mismo riesgo de
-- inconsistencia (ej: "ABC Insurance" escrito de forma distinta en
-- otra fila) y de actualización en cascada si la aseguradora cambia
-- de nombre.
--
-- Se identifican dos entidades independientes:
--   - La ASEGURADORA (compañía) — existe independientemente de
--     cualquier póliza específica.
--   - La PÓLIZA — pertenece a una aseguradora y tiene un tipo de
--     cobertura (Fire & Theft, Full Cover, etc.). Una póliza
--     específica es la que se asocia a la combinación vehículo-dueño.
--
-- CREATE TABLE INSURANCE_COMPANIES (
--     COMPANY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
--     COMPANY_NAME VARCHAR(100) UNIQUE NOT NULL
-- );
--
-- CREATE TABLE POLICIES (
--     POLICY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
--     COMPANY_ID INTEGER NOT NULL,
--     POLICY_TYPE VARCHAR(100) NOT NULL,
--     FOREIGN KEY (COMPANY_ID) REFERENCES INSURANCE_COMPANIES(COMPANY_ID)
-- );
--
-- VEHICLE_OWNERS ya no guarda el texto de la aseguradora ni de la
-- póliza directamente: en su lugar referencia POLICY_ID, y a través
-- de esa póliza se llega a la aseguradora (POLICY_ID -> COMPANY_ID).
--
-- =====================================================================
-- ESQUEMA FINAL (refinado)
-- =====================================================================

CREATE TABLE MODELS (
    MODEL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MAKE VARCHAR(50) NOT NULL,
    MODEL VARCHAR(50) NOT NULL,
    YEAR INT NOT NULL,
    UNIQUE (MAKE, MODEL, YEAR)
);

CREATE TABLE VEHICLES (
    VIN VARCHAR(17) PRIMARY KEY,
    MODEL_ID INTEGER NOT NULL,
    COLOR VARCHAR(30),
    FOREIGN KEY (MODEL_ID) REFERENCES MODELS(MODEL_ID)
);

CREATE TABLE OWNERS (
    OWNER_ID INTEGER PRIMARY KEY,
    OWNER_NAME VARCHAR(100) NOT NULL,
    OWNER_PHONE VARCHAR(20) NOT NULL
);

CREATE TABLE INSURANCE_COMPANIES (
    COMPANY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COMPANY_NAME VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE POLICIES (
    POLICY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COMPANY_ID INTEGER NOT NULL,
    POLICY_TYPE VARCHAR(100) NOT NULL,
    FOREIGN KEY (COMPANY_ID) REFERENCES INSURANCE_COMPANIES(COMPANY_ID)
);

CREATE TABLE VEHICLE_OWNERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    VIN VARCHAR(17) NOT NULL,
    OWNER_ID INTEGER NOT NULL,
    POLICY_ID INTEGER,
    OWNERSHIP_START DATE,
    OWNERSHIP_END DATE,  -- NULL si es el dueño actual
    FOREIGN KEY (VIN) REFERENCES VEHICLES(VIN),
    FOREIGN KEY (OWNER_ID) REFERENCES OWNERS(OWNER_ID),
    FOREIGN KEY (POLICY_ID) REFERENCES POLICIES(POLICY_ID)
);

-- =====================================================================
-- DATOS
-- =====================================================================

INSERT INTO MODELS (MODEL_ID, MAKE, MODEL, YEAR) VALUES (1, 'Honda', 'Accord', 2003);
INSERT INTO MODELS (MODEL_ID, MAKE, MODEL, YEAR) VALUES (2, 'Honda', 'CR-V', 2014);
INSERT INTO MODELS (MODEL_ID, MAKE, MODEL, YEAR) VALUES (3, 'Chevrolet', 'Volt', 2015);

INSERT INTO VEHICLES (VIN, MODEL_ID, COLOR) VALUES ('1HGCM82633A', 1, 'Silver');
INSERT INTO VEHICLES (VIN, MODEL_ID, COLOR) VALUES ('5J6RM4H79EL', 2, 'Blue');
INSERT INTO VEHICLES (VIN, MODEL_ID, COLOR) VALUES ('1G1RA6EH1FU', 3, 'Red');

INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (101, 'Alice', '123-456-7890');
INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (102, 'Bob', '987-654-3210');
INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (103, 'Claire', '555-123-4567');
INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (104, 'Dave', '111-222-3333');

INSERT INTO INSURANCE_COMPANIES (COMPANY_ID, COMPANY_NAME) VALUES (1, 'ABC Insurance');
INSERT INTO INSURANCE_COMPANIES (COMPANY_ID, COMPANY_NAME) VALUES (2, 'XYZ Insurance');
INSERT INTO INSURANCE_COMPANIES (COMPANY_ID, COMPANY_NAME) VALUES (3, 'DEF Insurance');
INSERT INTO INSURANCE_COMPANIES (COMPANY_ID, COMPANY_NAME) VALUES (4, 'GHI Insurance');

INSERT INTO POLICIES (POLICY_ID, COMPANY_ID, POLICY_TYPE) VALUES (1, 1, 'Fire & Theft');
INSERT INTO POLICIES (POLICY_ID, COMPANY_ID, POLICY_TYPE) VALUES (2, 2, 'Full Cover');
INSERT INTO POLICIES (POLICY_ID, COMPANY_ID, POLICY_TYPE) VALUES (3, 3, 'Collision');
INSERT INTO POLICIES (POLICY_ID, COMPANY_ID, POLICY_TYPE) VALUES (4, 4, 'Basic Legal');

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, POLICY_ID, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('1HGCM82633A', 101, 1, '2003-06-01', '2020-01-15');  -- Alice: dueña anterior

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, POLICY_ID, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('1HGCM82633A', 102, 2, '2020-01-16', NULL);  -- Bob: dueño actual

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, POLICY_ID, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('5J6RM4H79EL', 103, 3, '2014-08-01', NULL);  -- Claire: dueña actual

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, POLICY_ID, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('1G1RA6EH1FU', 104, 4, '2015-03-10', NULL);  -- Dave: dueño actual

-- =====================================================================
-- VERIFICACIÓN
-- =====================================================================

SELECT * FROM MODELS;
SELECT * FROM VEHICLES;
SELECT * FROM OWNERS;
SELECT * FROM INSURANCE_COMPANIES;
SELECT * FROM POLICIES;
SELECT * FROM VEHICLE_OWNERS;