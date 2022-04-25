drop table if exists SellsTo;
drop table if exists Company;
drop table if exists Child;
drop table if exists Adult;
drop table if exists Taxpayer;
drop table if exists Person;


create table Person (
    PID int primary key
);

create table Taxpayer (
    TID int primary key
);

create table Adult (
    PID int primary key references Person(PID),
    TID int not null references Taxpayer(TID),
    role varchar not null
);

create table Child (
    PID int primary key references Person(PID),
    age int not null
);

create table Company (
    CID int primary key,
    TID int not null references Taxpayer(TID)
);

create table SellsTo (
    childID int not null references Child(PID),
    paysForID int not null references Adult(PID),
    comID int not null references Company(CID),
    day date,
    price int not null,
    unique (childID, comID),
    primary key (childID, comID, day)
);
