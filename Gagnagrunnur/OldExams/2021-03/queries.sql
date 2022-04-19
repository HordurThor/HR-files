
-- (a)

select count(*)
from vaccines V
join companies C on C.id = V.comID
where C.name = 'Amgen';
-- 23

select count(*)
from vaccines V
join diseases D on D.id = V.disID
where D.name = 'Coronavirus';
-- 3


-- (b)

select count(distinct I.peoID)
from injections I
    join vaccines V on V.id = I.vacID
    join diseases D on D.id = V.disID
    join categories C on C.id = D.catID
where C.name = 'Immune diseases' and not D.curable;
-- 282

select count(distinct I.peoID)
from injections I
    join vaccines V on V.id = I.vacID
    join diseases D on D.id = V.disID
    join categories C on C.id = D.catID
where C.name = 'Bone diseases' and D.curable;
-- 514


-- (c)

drop view if exists vaceffecttime;
create view vaceffecttime
as
select V.id as vacID, D.name as disname, V.effectyears
from vaccines V
    join diseases D on D.id = V.disID
    group by V.id, D.name;


select V.vacID
from vaceffecttime V
where V.disname = 'Coronavirus' and V.effectyears = (
    select min(V.effectyears)
    from vaceffecttime V
    where V.disname = 'Coronavirus'
);
-- 535

select V.vacID
from vaceffecttime V
where V.disname = 'Coronavirus' and V.effectyears = (
    select max(V.effectyears)
    from vaceffecttime V
    where V.disname = 'Coronavirus'
);
-- 536


-- (d)

select count(*)
from diseases D
where D.id not in (
select V.disID
From vaccines V
group by V.disID
having count(*) >= 5);
-- 10


-- (e)

drop view if exists activevac;
create view activevac
as
select distinct I.peoID, V.disID
from injections I
    join vaccines V on V.id = I.vacID
where I.injectionyear + V.effectyears >= 2021;

select count(*)
from activevac A
    join diseases D on D.id = A.disID
where D.name = 'Sleep Apnea'
-- 113

select count(*)
from activevac A
    join diseases D on D.id = A.disID
where D.name = 'Coronavirus'
-- 235


-- (f)

select (1.0 *( select count(*) from injections) / 
(select count(*) from people))
-- 57.4908088235294118

-- (g)