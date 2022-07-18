# DML

select_all_user = """SELECT * FROM USER"""
select_all_doctor = """SELECT * FROM DOCTOR"""
select_all_specialty = """SELECT * FROM SPECIALTY"""
select_all_appointment = """SELECT * FROM APPOINTMENT"""
select_all_prescription = """SELECT * FROM PRESCRIPTION"""
select_all_patient = """SELECT * FROM PATIENT"""

insert_user = """INSERT INTO USER (LOGIN,CRYPTOGRAPHIC_PASSWD, USERTYPE) VALUES ("""
insert_doctor = """INSERT INTO DOCTOR (USERID, DOCTOR_TYPE) VALUES ("""
initial_users = """INSERT INTO USER (LOGIN,USERTYPE,CRYPTOGRAPHIC_PASSWD) VALUES ('SUPERADMIN', 'ADMIN', '1234')"""
initial_specialties = """INSERT INTO SPECIALTY (SPECIALTY) values ('Cardiologist'), ('Physician'), ('Family Care')"""
initial_doctor = """INSERT INTO DOCTOR (USERID, DOCTOR_TYPE) VALUES ('1', '1')"""

list_initial_data = [initial_users, initial_specialties, initial_doctor]

begin_transaction = "BEGIN TRANSACTION"