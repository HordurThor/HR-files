drop table if exists R2;
drop table if exists R3;
drop table if exists E5;
drop table if exists E4;
drop table if exists E3;
drop table if exists E1;
drop table if exists E2;

create table E2 (
E2ID int primary key
);

create table E1 (
E1ID int Primary key,
E2ID int not null references E2(E2ID)
);

create table E3 (
E3ID int primary key,
E1ID int not null references E1(E1ID)
);

create table E4 (
E4ID int primary key
);

create table E5 (
E5ID int primary key
);

create table R3 (
E5ID int not null references E5(E5ID),
E4ID int primary key references E4(E4ID)
);

create table R2 (
E1ID int references E1(E1ID),
E4ID int references R3(E4ID),
primary key (E1ID, E4ID)
);

