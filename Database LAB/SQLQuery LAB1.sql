CREATE DATABASE Students;

USE Students;
CREATE TABLE STUDENT
(
RollNo int PRIMARY KEY,
StudentName varchar(30) NOT NULL ,
DepartmentCode decimal(4,0) NOT NULL,
DOB DATE ,
Email varchar(255) NOT NULL,
StudentAddress varchar(255) NOT NULL,
);

CREATE TABLE COURSE
(
Ccode varchar(30) PRIMARY KEY,
CName varchar(30),
DepartmentCode decimal(4,0),
);

CREATE TABLE ENROLL
(
RollNo int FOREIGN KEY REFERENCES STUDENT(RollNo),
CCode varchar(30) FOREIGN KEY REFERENCES COURSE(CCode),
Semester char(30),
Grade varchar(30)
);

CREATE TABLE TEXTBOOK
(
CCode varchar(30) FOREIGN KEY REFERENCES COURSE(CCode),
Semester char(30) PRIMARY KEY,
Book_ISBN varchar(30)
);

CREATE TABLE BOOKDETAILS
(
Book_ISBN varchar(30) PRIMARY KEY,
Title varchar(30),
Publisher varchar(30),
Author varchar(30)
);

ALTER TABLE BOOKDETAILS
ADD Price int;

ALTER TABLE ENROLL
ADD CHECK(Grade in ('O', 'A+', 'A', 'B+', 'B', 'RA'))

