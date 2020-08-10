--CREATE OFFICE TABLE
CREATE TABLE office (
    office_name TEXT PRIMARY KEY,
    office_city TEXT NOT NULL,
    square_footage REAL NOT NULL
);

--CREATE RENTAL AGREEMENT TABLE
CREATE TABLE rental_agreement (
    agreement_id INTEGER PRIMARY KEY,
    rent_amount REAL NOT NULL,
    end_date TEXT,
    office_name TEXT NOT NULL, 
    FOREIGN KEY (office_name) REFERENCES office(office_name)
);

--CREATE PARTIES TABLE
CREATE TABLE parties (
    agency_id INTEGER,
    agreement_id INTEGER,
    FOREIGN KEY(agency_id) REFERENCES customer_agency(agency_id),
    FOREIGN KEY(agreement_id) REFERENCES rental_agreement(agreement_id)
    PRIMARY KEY(agency_id, agreement_id)
);

--CREATE CUSTOMER AGENCY TABLE
CREATE TABLE customer_agency (
    agency_id INTEGER PRIMARY KEY,
    agency_name TEXT NOT NULL,
    address TEXT NOT NULL,
    agency_city TEXT NOT NULL,
    phone_no TEXT NOT NULL
);
