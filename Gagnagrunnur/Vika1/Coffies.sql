DROP TABLE IF EXISTS Sells;
DROP TABLE IF EXISTS Coffeehouses;
DROP TABLE IF EXISTS Coffees;


CREATE TABLE Coffees(
	name VARCHAR(20) PRIMARY KEY,
	manufacturer VARCHAR(20) 
);

CREATE TABLE Coffeehouses(
	name VARCHAR(20) PRIMARY KEY,
	address VARCHAR(20),
	licence VARCHAR(20)
);

CREATE TABLE Sells(
	coffeehouse VARCHAR(20),
	coffee VARCHAR(20),
	price REAL,
	PRIMARY KEY(coffeehouse, coffee),
	FOREIGN KEY(coffee) REFERENCES Coffees(name),
	FOREIGN KEY(coffeehouse) REFERENCES Coffeehouses(name)
);

SELECT * FROM coffees;
SELECT * FROM Coffeehouses;
SELECT * FROM Sells;
