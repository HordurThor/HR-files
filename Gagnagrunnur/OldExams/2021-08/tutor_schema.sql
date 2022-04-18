drop table if exists Attend;
drop table if exists Tutor;
drop table if exists Censor;
drop table if exists Lectures;
drop table if exists Students;
drop table if exists Teachers;


CREATE TABLE Teachers (
TID INTEGER PRIMARY KEY,
name varchar not null
);

create table Students (
SID INTEGER PRIMARY KEY,
name varchar not null
);

create table Lectures (
LID INTEGER PRIMARY KEY,
subject varchar not null
);

create table Censor (
CID INTEGER PRIMARY KEY,
name varchar not null
);

create table Tutor (
fromyear integer,
teacherID integer not null,
studentID integer,
cencorID integer not null,
foreign key (teacherID) references Teachers(TID),
foreign key (studentID) references Students(SID),
foreign key (cencorID) references Censor(CID),
primary key (studentID, fromyear)
);

create table Attend (
studentID INTEGER,
lectureID INTEGER,
foreign key (studentID) references Students(SID),
foreign key (lectureID) references Lectures(LID),
primary key (studentID, lectureID)
);