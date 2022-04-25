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
    thoughtID int not null references Loners (LID),
    lasted int not null,
    name varchar not null
);

create table left_for (
    JID int references Jojos(JID),
    HID int references Homes(HID),
    what varchar,
    primary key (JID, HID, what)
);

create table get_back (
    JID int not null,
    HID int not null,
    LID int primary key references Loners(LID),
    what varchar not null,
    to_where varchar not null,
    foreign key (JID, HID, what) references left_for (JID, HID, what)
);