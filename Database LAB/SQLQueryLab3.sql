CREATE DATABASE Minions;

USE Minions;
CREATE TABLE Minions
(
	Id INT NOT NULL,
	Name VARCHAR(50) NOT NULL ,
	Age DECIMAL(3,0) NOT NULL,
	PRIMARY KEY (Id),
);

CREATE TABLE Towns
(
	Id int NOT NULL,
	Name VARCHAR(50) NOT NULL ,
	PRIMARY KEY (Id),
);

ALTER TABLE Minions
	ADD TownId INT FOREIGN KEY REFERENCES Towns(Id) NOT NULL;

SELECT * from Minions

/* Program 4*/

CREATE DATABASE Movies;

USE Movies;

CREATE TABLE Directors
(
	Id           INT NOT NULL PRIMARY KEY,
	DirectorName NVARCHAR(70) NOT NULL,
	Notes        NVARCHAR(MAX)
);

INSERT INTO Directors(Id, DirectorName)
	VALUES
	(1, 'Director 1'),
	(2, 'Director 2'),
	(3, 'Director 3'),
	(4, 'Director 4'),
	(5, 'Director 5');

CREATE TABLE Genres
(
	Id INT NOT NULL PRIMARY KEY,
	GenreName NVARCHAR(70) NOT NULL,
	Notes NVARCHAR(MAX)
);

INSERT INTO Genres(Id, GenreName)
	VALUES
	(1,'Genre 1'),
	(2,'Genre 2'),
	(3,'Genre 3'),
	(4,'Genre 4'),
	(5,'Genre 5');

CREATE TABLE Categories
(
	Id  INT NOT NULL PRIMARY KEY,
	CategoryName NVARCHAR(70) NOT NULL,
	Notes NVARCHAR(MAX)
);

INSERT INTO Categories(Id, CategoryName)
	VALUES
	(1, 'Cat 1'),
	(2, 'Cat 2'),
	(3, 'Cat 3'),
	(4, 'Cat 4'),
	(5, 'Cat 5');

CREATE TABLE Movies
(
	Id  INT NOT NULL PRIMARY KEY,
	Title NVARCHAR(255) NOT NULL,
	DirectorId INT FOREIGN KEY REFERENCES Directors(Id),
	CopyrightYear INT,
	Length NVARCHAR(50),
	GenreId INT FOREIGN KEY REFERENCES Genres(Id),
	CategoryId INT FOREIGN KEY REFERENCES Categories(Id),
	Rating INT,
	Notes NVARCHAR(MAX)
	);

INSERT INTO Movies(Id, Title, DirectorId, GenreId, CategoryId)
	VALUES
	(1,'Title One',2,3,4),
	(2,'Title Two',3,4,5),
	(3,'Title Three',1,2,3),
	(4,'Title Four',5,1,3),
	(5,'Title Five',3,5,2);

SELECT * from Genres