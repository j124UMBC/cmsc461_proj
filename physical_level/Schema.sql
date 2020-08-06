--CREATE OFFICE TABLE
CREATE TABLE office (
    office_name INT PRIMARY KEY,
    office_city TEXT NOT NULL,
    square_footage REAL NOT NULL
);

--CREATE RENTAL AGREEMENT TABLE
CREATE TABLE rental_agreement (
    agreement_id INT PRIMARY KEY,
    rent_amount REAL NOT NULL,
    end_date TEXT,
    office_name INT, 
    FOREIGN KEY (office_name) REFERENCES office(office_name)
);

--CREATE PARTIES TABLE
CREATE TABLE parties (
    agency_id INT,
    agreement_id INT,
    FOREIGN KEY(agency_id) REFERENCES customer_agency(agency_id),
    FOREIGN KEY(agreement_id) REFERENCES rental_agreement(agreement_id)
);

--CREATE CUSTOMER AGENCY TABLE
CREATE TABLE customer_agency (
    agency_id INT PRIMARY KEY,
    agency_name TEXT NOT NULL,
    address TEXT NOT NULL,
    agency_city TEXT NOT NULL,
    phone_no TEXT NOT NULL
);