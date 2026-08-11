-- =====================================================================
-- NORMALIZACIÓN: CARS
-- =====================================================================
--
-- ESTADO INICIAL (tabla sin normalizar)
--
-- VIN            Make      Model   Year  Color   Owner ID  Owner Name  Owner Phone     Insurance Company  Insurance Policy
-- 1HGCM82633A    Honda     Accord  2003  Silver  101       Alice       123-456-7890    ABC Insurance      Fire & Theft
-- 1HGCM82633A    Honda     Accord  2003  Silver  102       Bob         987-654-3210    XYZ Insurance      Full Cover
-- 5J6RM4H79EL    Honda     CR-V    2014  Blue    103       Claire      555-123-4567    DEF Insurance      Collision
-- 1G1RA6EH1FU    Chevrolet Volt    2015  Red     104       Dave        111-222-3333    GHI Insurance      Basic Legal
--
-- ¿Por qué no cumple ninguna Forma Normal?
--   - VIN se repite (1HGCM82633A aparece dos veces), así que por sí
--     solo no es una llave primaria válida.
--   - Hay grupos repetidos: los datos del vehículo (Make, Model, Year,
--     Color) se repiten en cada fila donde aparece el mismo VIN,
--     aunque el vehículo es el mismo objeto físico.
--   - No hay una sola columna que identifique de forma única cada fila.
--
-- ---------------------------------------------------------------------
-- PASO 1 — Primera Forma Normal (1FN)
-- ---------------------------------------------------------------------
-- Se define la llave compuesta (VIN, Owner ID), ya que la combinación
-- vehículo-dueño sí identifica de forma única cada fila (un mismo VIN
-- puede tener más de un Owner ID asociado, pero la pareja nunca se
-- repite).
--
-- CREATE TABLE CARS_1NF (
--     VIN VARCHAR(17) NOT NULL,
--     MAKE VARCHAR(50) NOT NULL,
--     MODEL VARCHAR(50) NOT NULL,
--     YEAR INT NOT NULL,
--     COLOR VARCHAR(30),
--     OWNER_ID INTEGER NOT NULL,
--     OWNER_NAME VARCHAR(100) NOT NULL,
--     OWNER_PHONE VARCHAR(20) NOT NULL,
--     INSURANCE_COMPANY VARCHAR(100),
--     INSURANCE_POLICY VARCHAR(100),
--     PRIMARY KEY (VIN, OWNER_ID)
-- );
--
-- Válida en 1FN, pero con redundancia: los datos del Honda Accord
-- (Make, Model, Year, Color) se repiten en las dos filas donde
-- aparece su VIN.
--
-- ---------------------------------------------------------------------
-- PASO 2 — Segunda Forma Normal (2FN)
-- ---------------------------------------------------------------------
-- Se analiza de qué parte de la llave (VIN, Owner ID) depende cada
-- columna:
--
--   Make, Model, Year, Color        -> depende solo de VIN
--                                       (características físicas del
--                                       vehículo; no cambian según el
--                                       dueño)
--   Owner Name, Owner Phone         -> depende solo de Owner ID
--                                       (datos de la persona; no
--                                       cambian según el vehículo)
--   Insurance Company, Insurance
--   Policy                          -> depende de VIN + Owner ID
--                                       (llave completa): la póliza
--                                       depende de la combinación
--                                       específica, ya que el mismo
--                                       Accord tiene aseguradoras
--                                       distintas según el dueño
--                                       (Alice vs. Bob)
--
-- Se separan las columnas que dependen de una sola parte de la llave
-- en tablas propias: VEHICLES (por VIN), OWNERS (por Owner ID), y
-- una tabla de relación para lo que depende de la llave completa.
--
-- ---------------------------------------------------------------------
-- PASO 3 — Tercera Forma Normal (3FN)
-- ---------------------------------------------------------------------
-- Se revisa si queda alguna dependencia transitiva:
--   - VEHICLES: Make, Model, Year, Color dependen directamente de VIN.
--     Sin dependencia transitiva. OK en 3FN.
--   - OWNERS: Owner Name, Owner Phone dependen directamente de
--     Owner ID. Sin dependencia transitiva. OK en 3FN.
--   - VEHICLE_OWNERS: Insurance Company e Insurance Policy dependen
--     de la llave completa (VIN, Owner ID), no de ningún otro
--     atributo no-llave. OK en 3FN.
--
-- ¿De quién depende el seguro? Este es el punto clave: el seguro no
-- pertenece solo al vehículo (el mismo Accord tiene dos pólizas según
-- el dueño) ni solo al dueño (un dueño podría asegurar vehículos
-- distintos con aseguradoras distintas). Depende de la combinación
-- específica vehículo-dueño, por lo que su lugar correcto es la tabla
-- de relación VEHICLE_OWNERS.
--
-- Extensión adicional (historial): dado que el Accord tiene dos
-- dueños (Alice y Bob), se agregan a VEHICLE_OWNERS las columnas
-- OWNERSHIP_START y OWNERSHIP_END para distinguir el dueño histórico
-- del dueño actual (OWNERSHIP_END IS NULL = dueño vigente). Esto no
-- es parte estricta de la normalización, sino una decisión de
-- modelado para reflejar que la propiedad de un vehículo cambia en
-- el tiempo.
--
-- =====================================================================
-- ESQUEMA FINAL (3FN)
-- =====================================================================

CREATE TABLE VEHICLES (
    VIN VARCHAR(17) PRIMARY KEY,
    MAKE VARCHAR(50) NOT NULL,
    MODEL VARCHAR(50) NOT NULL,
    YEAR INT NOT NULL,
    COLOR VARCHAR(30)
);

CREATE TABLE OWNERS (
    OWNER_ID INTEGER PRIMARY KEY,
    OWNER_NAME VARCHAR(100) NOT NULL,
    OWNER_PHONE VARCHAR(20) NOT NULL
);

CREATE TABLE VEHICLE_OWNERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    VIN VARCHAR(17) NOT NULL,
    OWNER_ID INTEGER NOT NULL,
    INSURANCE_COMPANY VARCHAR(100),
    INSURANCE_POLICY VARCHAR(100),
    OWNERSHIP_START DATE,
    OWNERSHIP_END DATE,  -- NULL si es el dueño actual
    FOREIGN KEY (VIN) REFERENCES VEHICLES(VIN),
    FOREIGN KEY (OWNER_ID) REFERENCES OWNERS(OWNER_ID)
);

-- =====================================================================
-- DATOS
-- =====================================================================

INSERT INTO VEHICLES (VIN, MAKE, MODEL, YEAR, COLOR) VALUES ('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver');
INSERT INTO VEHICLES (VIN, MAKE, MODEL, YEAR, COLOR) VALUES ('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue');
INSERT INTO VEHICLES (VIN, MAKE, MODEL, YEAR, COLOR) VALUES ('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red');

INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (101, 'Alice', '123-456-7890');
INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (102, 'Bob', '987-654-3210');
INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (103, 'Claire', '555-123-4567');
INSERT INTO OWNERS (OWNER_ID, OWNER_NAME, OWNER_PHONE) VALUES (104, 'Dave', '111-222-3333');

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, INSURANCE_COMPANY, INSURANCE_POLICY, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('1HGCM82633A', 101, 'ABC Insurance', 'Fire & Theft', '2003-06-01', '2020-01-15');  -- Alice: dueña anterior

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, INSURANCE_COMPANY, INSURANCE_POLICY, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('1HGCM82633A', 102, 'XYZ Insurance', 'Full Cover', '2020-01-16', NULL);  -- Bob: dueño actual

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, INSURANCE_COMPANY, INSURANCE_POLICY, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('5J6RM4H79EL', 103, 'DEF Insurance', 'Collision', '2014-08-01', NULL);  -- Claire: dueña actual

INSERT INTO VEHICLE_OWNERS (VIN, OWNER_ID, INSURANCE_COMPANY, INSURANCE_POLICY, OWNERSHIP_START, OWNERSHIP_END)
VALUES ('1G1RA6EH1FU', 104, 'GHI Insurance', 'Basic Legal', '2015-03-10', NULL);  -- Dave: dueño actual

-- =====================================================================
-- VERIFICACIÓN
-- =====================================================================

SELECT * FROM VEHICLES;
SELECT * FROM OWNERS;
SELECT * FROM VEHICLE_OWNERS;