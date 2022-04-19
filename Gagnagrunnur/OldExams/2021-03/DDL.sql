drop table if exists Grades;
drop table if exists Takes;
drop table if exists Examiner;
drop table if exists Course;
drop table if exists Student;
drop table if exists Term;


create table Term (
TID int primary key,
_desc varchar not null
);

create table Student (
SID int primary key,
TID int not null references term(TID)
);

create table Course (
CID int primary key
);

create table Examiner (
EID int primary key
);

create table Takes (
TakesID int primary key,
TID int not null references Term(TID),
CID int not null  references Course(CID),
SID int not null references Student(SID),
room varchar not null,
unique (TID, CID)
);

create table Grades (
TakesID int references Takes(TakesID),
EID int references Examiner(EID),
grade int not null,
primary key (TakesID, EID)
);

