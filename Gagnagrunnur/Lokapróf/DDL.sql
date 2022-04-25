drop table if exists get_back;
drop table if exists left_for;
drop table if exists Jojos;
drop table if exists Loners;
drop table if exists Homes;


create table Homes (
    HID int primary key,
    state varchar not null
);

create table Loners (
    LID int primary key,
    status varchar not null
);

create table Jojos (
    JID int primary key,
    thoughtID int not null references Loners(LID),
    lasted int not null,
    name varchar not null
);

create table left_for (
    JID int not null references Jojos(JID),
    HID int not null references Homes(HID),
    what varchar primary key
);

create table get_back (
    LID int primary key,
    leftforID varchar not null references left_for(what),
    to_where varchar not null
);