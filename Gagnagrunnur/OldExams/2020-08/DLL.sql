drop table if exists Audit;
drop table if exists Client;
drop table if exists Shrink;
drop table if exists Office;
drop table if exists Manager;


create table Manager (
    MID int primary key
);

create table Office (
    OID int primary key,
    MID int not null references Manager(MID)
);

create table Shrink (
    SID int primary key,
    OID int not null references Office(OID),
    since date not null
);

create table Client (
    CID int primary key,
    SID int not null references Shrink(SID)
);

create table Audit (
    CID int references Client(CID),
    MID int references Manager(MID),
    primary key (CID, MID)
);