-- (a)

select count(*)
from Plants P
join Families F on F.id = P.familyID
where F.name = 'Thespesia';
-- 18

-- (b)

select count(*)
from People Pe
where Pe.id not in (select planterID from PlantedIn) and Pe.position = 'Planter';
-- 9

-- (c)

select sum(1.0 * Fb.size * Pl.percentage / 100) as sqm
from Families F
join Plants P on P.familyID = F.id
join PlantedIn Pl on P.id = Pl.plantID
join Flowerbeds Fb on Fb.id = Pl.flowerbedID
where F.name = 'Vicia';
-- 27.3


drop view if exists capperc;
create view capperc
as
select Pl.flowerbedID as id, sum(Pl.percentage) as prec
from PlantedIn Pl
group by Pl.flowerbedID;

-- (d)

select C.id
from capperc C
where C.prec = 105;
-- 243

-- (e)

select count(*)
from Flowerbeds Fb
where Fb.id not in (
    select C.id 
    from capperc C
    where C.prec >= 100);
-- 271

-- (f)

select count(*)
from capperc C 
where C.prec < 100 and C.id in (
    select Pl.flowerbedID
    from Types T
    join Families F on F.typeID = T.id
    join Plants P on P.familyID = F.id
    join PlantedIn Pl on Pl.plantID = P.id
    where T.name = 'shrub');
-- 169

-- (g)

select count(*)
from (select Pl.flowerbedID
    from Types T
    join Families F on F.typeID = T.Id
    join Plants P on P.familyID = F.id
    join PlantedIn Pl on Pl.plantID = P.id
    group by Pl.flowerbedID
    having count(distinct T.name) = (
        select count(T.name)
        from Types T
    )) X;
-- 2

-- (h)

drop view if exists pdata;
create view pdata
as 
select Pe.id, Pe.name, Pe.position as pos, 1.0 * Fb.size * Pl.percentage / 100 as sqm, T.name as Pltype, Pa.name as parkname
from Types T
join Families F on F.typeID = T.id
join Plants P on P.familyID = F.id
join PlantedIn Pl on Pl.plantID = P.id
join People Pe on Pe.id = Pl.planterID
join Flowerbeds Fb on Fb.id = Pl.flowerbedID
join Parks Pa on Pa.id = Fb.parkID;

select P.id, P.name, sum(P.sqm)
from pdata P
group by P.id, P.name
having P.id in (
    select P2.id
    from Pdata P2 
    where P2.pos = 'Planter' and
    P2.Pltype = 'flower' and
    P2.Parkname = 'Kongens Have')
order by sum(p.sqm) desc

-- First 5 rows:
--     id          name                sum
-- 1	154	    Frank Jansen	    72.82
-- 2	110	    Jan Lauridsen	    72.04999999999998
-- 3	48	    Johan Mikaelsen	    70.41999999999999
-- 4	142	    Mikael Lauritz	    67.52999999999999
-- 5	156	    Mikael Mikaelsen	67.47