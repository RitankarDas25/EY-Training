-- Create the Database
CREATE DATABASE HospitalDB;
USE HospitalDB;

-- 1. Patients Table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender CHAR(1),
    city VARCHAR(50)
);

-- 2. Doctors Table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50),
    experience INT
);

-- 3. Appointments Table
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- 4. MedicalRecords Table
CREATE TABLE MedicalRecords (
    record_id INT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    diagnosis VARCHAR(100),
    treatment VARCHAR(100),
    date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- 5. Billing Table
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY,
    patient_id INT NOT NULL,
    amount DECIMAL(10,2),
    bill_date DATE,
    status VARCHAR(20), -- e.g., 'Paid', 'Unpaid'
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Insert 10 Patients (from different Indian cities)
INSERT INTO Patients (patient_id, name, age, gender, city) VALUES
(101, 'Aditi Sharma', 35, 'F', 'Mumbai'),
(102, 'Ravi Kumar', 58, 'M', 'Delhi'),
(103, 'Pooja Singh', 12, 'F', 'Bengaluru'),
(104, 'Vikram Reddy', 70, 'M', 'Hyderabad'),
(105, 'Neha Patel', 28, 'F', 'Ahmedabad'),
(106, 'Arjun Menon', 45, 'M', 'Chennai'),
(107, 'Sana Khan', 22, 'F', 'Kolkata'),
(108, 'Ganesh Iyer', 65, 'M', 'Pune'),
(109, 'Priya Das', 19, 'F', 'Jaipur'),
(110, 'Siddharth Jain', 51, 'M', 'Lucknow');

-- Insert 5 Doctors (with various specializations)
INSERT INTO Doctors (doctor_id, name, specialization, experience) VALUES
(1, 'Dr. Anil Varma', 'Cardiology', 15),
(2, 'Dr. Meera Rao', 'Orthopedics', 10),
(3, 'Dr. Rohan Gupta', 'Pediatrics', 8),
(4, 'Dr. Seema Dube', 'Neurology', 20),
(5, 'Dr. Vivek Saini', 'Oncology', 12);

-- Insert Appointments
INSERT INTO Appointments (appointment_id, patient_id, doctor_id, appointment_date, status) VALUES
(1001, 102, 1, '2025-09-29', 'Completed'),
(1002, 104, 1, '2025-10-01', 'Scheduled'),
(1003, 103, 3, '2025-09-30', 'Scheduled'),
(1004, 106, 2, '2025-09-29', 'Completed'),
(1005, 101, 4, '2025-10-02', 'Scheduled'),
(1006, 108, 5, '2025-10-03', 'Scheduled');

-- Insert Medical Records (linked to completed appointments)
INSERT INTO MedicalRecords (record_id, patient_id, doctor_id, diagnosis, treatment, date) VALUES
(2001, 102, 1, 'Hypertension', 'Prescribe medication A', '2025-09-29'),
(2002, 106, 2, 'Fractured Hand', 'Casting and Painkillers', '2025-09-29');

-- Insert Billing
INSERT INTO Billing (bill_id, patient_id, amount, bill_date, status) VALUES
(3001, 102, 500.00, '2025-09-29', 'Paid'),
(3002, 104, 850.50, '2025-10-01', 'Unpaid'), -- Unpaid Bill
(3003, 106, 6200.00, '2025-09-29', 'Paid'),
(3004, 101, 400.00, '2025-10-02', 'Unpaid'), -- Unpaid Bill
(3005, 108, 1200.00, '2025-10-03', 'Scheduled'); -- Scheduled Bill

SELECT
    P.patient_id,
    P.name AS patient_name,
    D.name AS doctor_name,
    D.specialization
FROM
    Patients P
JOIN
    Appointments A ON P.patient_id = A.patient_id
JOIN
    Doctors D ON A.doctor_id = D.doctor_id
WHERE
    D.specialization = 'Cardiology'
GROUP BY
    P.patient_id, P.name, D.name, D.specialization;
    
    SELECT
    A.appointment_id,
    A.appointment_date,
    P.name AS patient_name,
    A.status
FROM
    Appointments A
JOIN
    Patients P ON A.patient_id = P.patient_id
WHERE
    A.doctor_id = 1 -- Replace 1 with the target doctor_id
ORDER BY
    A.appointment_date;
    
    SELECT
    B.bill_id,
    P.name AS patient_name,
    B.amount,
    B.bill_date,
    B.status
FROM
    Billing B
JOIN
    Patients P ON B.patient_id = P.patient_id
WHERE
    B.status = 'Unpaid'
ORDER BY
    B.bill_date;
    
    DELIMITER $$
CREATE PROCEDURE GetPatientHistory(
    IN p_patient_id INT
)
BEGIN
    SELECT
        MR.date AS visit_date,
        D.name AS doctor_name,
        D.specialization,
        MR.diagnosis,
        MR.treatment
    FROM
        MedicalRecords MR
    JOIN
        Doctors D ON MR.doctor_id = D.doctor_id
    WHERE
        MR.patient_id = p_patient_id
    ORDER BY
        MR.date DESC;
END$$
DELIMITER ;

CALL GetPatientHistory(102);

DELIMITER $$
CREATE PROCEDURE GetDoctorAppointments(
    IN p_doctor_id INT
)
BEGIN
    SELECT
        A.appointment_id,
        P.name AS patient_name,
        P.city,
        A.appointment_date,
        A.status
    FROM
        Appointments A
    JOIN
        Patients P ON A.patient_id = P.patient_id
    WHERE
        A.doctor_id = p_doctor_id
    ORDER BY
        A.appointment_date ASC;
END$$
DELIMITER ;
CALL GetDoctorAppointments(3);
