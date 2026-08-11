-- =====================================================================
-- NORMALIZACIÓN: ORDERS
-- =====================================================================
--
-- ESTADO INICIAL (tabla sin normalizar)
--
-- Order ID  Customer Name  Customer Phone  Address          Item ID  Item Name      Price  Quantity  Special Request  Delivery Time
-- 001       Alice          123-456-7890    123 Main St      101      Cheeseburger   $8     2         No onions        6:00 PM
-- 001       Alice          123-456-7890    123 Main St      102      Fries          $3     1         Extra ketchup    6:00 PM
-- 002       Bob            987-654-3210    456 Elm St       103      Pizza          $12    1         Extra cheese     7:30 PM
-- 002       Bob            987-654-3210    4th Avenue       102      Fries          $3     2         None             7:30 PM
-- 003       Claire         555-123-4567    789 Oak St       105      Salad          $6     1         No croutons      12:00 PM
-- 004       Claire         555-123-4567    464 Georgia St   106      Water          $1     1         None             5:00 PM
--
-- ¿Por qué no cumple ninguna Forma Normal?
--   - Order ID se repite (001 y 002 aparecen dos veces cada uno), así
--     que por sí solo no identifica una fila de forma única.
--   - Hay grupos repetidos: el mismo pedido aparece en varias filas,
--     una por cada producto que contiene, repitiendo en cada una los
--     datos del cliente y del pedido (Customer Name, Customer Phone,
--     Address, Delivery Time).
--   - Inconsistencia detectada: Order ID = 002 tiene dos direcciones
--     distintas (456 Elm St y 4th Avenue) para el mismo pedido, lo
--     que confirma que Address no debería depender de la fila del
--     producto, sino ser un solo valor por pedido.
--
-- ---------------------------------------------------------------------
-- PASO 1 — Primera Forma Normal (1FN)
-- ---------------------------------------------------------------------
-- Se define una llave primaria compuesta: (Order ID, Item ID). Esto ya
-- identifica de forma única cada fila (cada combinación pedido-
-- producto aparece una sola vez), y no hay celdas con múltiples
-- valores.
--
-- CREATE TABLE ORDERS_1NF (
--     ORDER_ID INTEGER NOT NULL,
--     CUSTOMER_NAME VARCHAR(100) NOT NULL,
--     CUSTOMER_PHONE VARCHAR(20) NOT NULL,
--     ADDRESS VARCHAR(150) NOT NULL,
--     ITEM_ID INTEGER NOT NULL,
--     ITEM_NAME VARCHAR(100) NOT NULL,
--     PRICE DECIMAL(10,2) NOT NULL,
--     QUANTITY INT NOT NULL,
--     SPECIAL_REQUEST VARCHAR(150),
--     DELIVERY_TIME TIME NOT NULL,
--     PRIMARY KEY (ORDER_ID, ITEM_ID)
-- );
--
-- Válida en 1FN, pero con redundancia: Customer Name, Customer Phone,
-- Address y Delivery Time se repiten cada vez que un pedido tiene más
-- de un producto (ver Order 001, dos filas con los mismos datos de
-- cliente).
--
-- ---------------------------------------------------------------------
-- PASO 2 — Segunda Forma Normal (2FN)
-- ---------------------------------------------------------------------
-- Se analiza de qué parte de la llave (Order ID, Item ID) depende
-- cada columna:
--
--   Customer Name     -> depende solo de Order ID (el nombre no
--                          cambia según el producto pedido)
--   Customer Phone    -> depende solo de Order ID
--   Address            -> depende solo de Order ID (una dirección
--                          por pedido)
--   Delivery Time      -> depende solo de Order ID
--   Item Name          -> depende solo de Item ID (no cambia según
--                          el pedido en que aparezca)
--   Price               -> depende solo de Item ID (dato de catálogo)
--   Quantity            -> depende de Order ID + Item ID (llave
--                          completa): solo tiene sentido para "este
--                          producto en este pedido específico"
--   Special Request     -> depende de Order ID + Item ID (llave
--                          completa): es específico de un producto
--                          dentro de un pedido
--
-- Se separan en tablas propias las columnas que dependen de una sola
-- parte de la llave:
--
-- CREATE TABLE ORDERS_2NF (         -- depende solo de Order ID
--     ORDER_ID INTEGER PRIMARY KEY,
--     CUSTOMER_NAME VARCHAR(100) NOT NULL,
--     CUSTOMER_PHONE VARCHAR(20) NOT NULL,
--     ADDRESS VARCHAR(150) NOT NULL,
--     DELIVERY_TIME TIME NOT NULL
-- );
--
-- CREATE TABLE ITEMS_2NF (          -- depende solo de Item ID
--     ITEM_ID INTEGER PRIMARY KEY,
--     ITEM_NAME VARCHAR(100) NOT NULL,
--     PRICE DECIMAL(10,2) NOT NULL
-- );
--
-- CREATE TABLE ORDER_ITEMS_2NF (    -- depende de la llave completa
--     ORDER_ID INTEGER NOT NULL,
--     ITEM_ID INTEGER NOT NULL,
--     QUANTITY INT NOT NULL,
--     SPECIAL_REQUEST VARCHAR(150),
--     PRIMARY KEY (ORDER_ID, ITEM_ID)
-- );
--
-- ---------------------------------------------------------------------
-- PASO 3 — Tercera Forma Normal (3FN)
-- ---------------------------------------------------------------------
-- Se revisa si queda alguna dependencia transitiva:
--   - ITEMS_2NF: Item Name y Price dependen directamente de Item ID.
--     Sin dependencia transitiva. OK en 3FN.
--   - ORDER_ITEMS_2NF: Quantity y Special Request dependen
--     directamente de la llave compuesta (Order ID, Item ID). Sin
--     dependencia transitiva. OK en 3FN.
--   - ORDERS_2NF: aquí sí hay que revisar con cuidado. Customer Name
--     y Customer Phone dependen de Order ID, pero en realidad
--     dependen del CLIENTE, no del pedido en sí — si el mismo
--     cliente hace otro pedido, su nombre y teléfono se repetirían
--     de nuevo. Esto es una dependencia transitiva:
--     Order ID -> Customer -> Customer Name, Customer Phone.
--
--     En cambio, Address y Delivery Time SÍ se quedan en Orders: son
--     datos propios de ese pedido específico. Prueba de esto: Claire
--     tiene dos pedidos (003 y 004) con direcciones y horas
--     diferentes, lo que confirma que estos datos pertenecen al
--     pedido, no al cliente.
--
-- Para eliminar la dependencia transitiva, se separa Customer en su
-- propia tabla (CUSTOMERS), y Orders queda solo con una referencia
-- (CUSTOMER_ID) más los datos que sí le pertenecen (Address,
-- Delivery Time).
--
-- =====================================================================
-- ESQUEMA FINAL (3FN)
-- =====================================================================

CREATE TABLE CUSTOMERS (
    CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CUSTOMER_NAME VARCHAR(100) NOT NULL,
    CUSTOMER_PHONE VARCHAR(20) NOT NULL
);

CREATE TABLE ITEMS (
    ITEM_ID INTEGER PRIMARY KEY,
    ITEM_NAME VARCHAR(100) NOT NULL,
    PRICE DECIMAL(10, 2) NOT NULL
);

CREATE TABLE ORDERS (
    ORDER_ID INTEGER PRIMARY KEY,
    CUSTOMER_ID INTEGER NOT NULL,
    ADDRESS VARCHAR(150) NOT NULL,
    DELIVERY_TIME TIME NOT NULL,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID)
);

CREATE TABLE ORDER_ITEMS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ORDER_ID INTEGER NOT NULL,
    ITEM_ID INTEGER NOT NULL,
    QUANTITY INT NOT NULL,
    SPECIAL_REQUEST VARCHAR(150),
    FOREIGN KEY (ORDER_ID) REFERENCES ORDERS(ORDER_ID),
    FOREIGN KEY (ITEM_ID) REFERENCES ITEMS(ITEM_ID)
);

-- =====================================================================
-- DATOS
-- =====================================================================

INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_PHONE) VALUES (1, 'Alice', '123-456-7890');
INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_PHONE) VALUES (2, 'Bob', '987-654-3210');
INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_PHONE) VALUES (3, 'Claire', '555-123-4567');

INSERT INTO ITEMS (ITEM_ID, ITEM_NAME, PRICE) VALUES (101, 'Cheeseburger', 8.00);
INSERT INTO ITEMS (ITEM_ID, ITEM_NAME, PRICE) VALUES (102, 'Fries', 3.00);
INSERT INTO ITEMS (ITEM_ID, ITEM_NAME, PRICE) VALUES (103, 'Pizza', 12.00);
INSERT INTO ITEMS (ITEM_ID, ITEM_NAME, PRICE) VALUES (105, 'Salad', 6.00);
INSERT INTO ITEMS (ITEM_ID, ITEM_NAME, PRICE) VALUES (106, 'Water', 1.00);

INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, ADDRESS, DELIVERY_TIME) VALUES (1, 1, '123 Main St', '18:00');
INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, ADDRESS, DELIVERY_TIME) VALUES (2, 2, '456 Elm St', '19:30');
INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, ADDRESS, DELIVERY_TIME) VALUES (3, 3, '789 Oak St', '12:00');
INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, ADDRESS, DELIVERY_TIME) VALUES (4, 3, '464 Georgia St', '17:00');

INSERT INTO ORDER_ITEMS (ORDER_ID, ITEM_ID, QUANTITY, SPECIAL_REQUEST) VALUES (1, 101, 2, 'No onions');
INSERT INTO ORDER_ITEMS (ORDER_ID, ITEM_ID, QUANTITY, SPECIAL_REQUEST) VALUES (1, 102, 1, 'Extra ketchup');
INSERT INTO ORDER_ITEMS (ORDER_ID, ITEM_ID, QUANTITY, SPECIAL_REQUEST) VALUES (2, 103, 1, 'Extra cheese');
INSERT INTO ORDER_ITEMS (ORDER_ID, ITEM_ID, QUANTITY, SPECIAL_REQUEST) VALUES (2, 102, 2, 'None');
INSERT INTO ORDER_ITEMS (ORDER_ID, ITEM_ID, QUANTITY, SPECIAL_REQUEST) VALUES (3, 105, 1, 'No croutons');
INSERT INTO ORDER_ITEMS (ORDER_ID, ITEM_ID, QUANTITY, SPECIAL_REQUEST) VALUES (4, 106, 1, 'None');

-- =====================================================================
-- VERIFICACIÓN
-- =====================================================================

SELECT * FROM CUSTOMERS;
SELECT * FROM ITEMS;
SELECT * FROM ORDERS;
SELECT * FROM ORDER_ITEMS;