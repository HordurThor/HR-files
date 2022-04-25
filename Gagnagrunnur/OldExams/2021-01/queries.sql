

-- (a)

select count(*)
from models M
join makers S on S.id = M.makerID
where S.name = 'VOLVO'
--13

select count(*)
from cars C
join models M on M.id = C.modelID
join makers S on S.id = M.makerID
where S.name = 'VOLVO'
-- 664


-- (b)

select count(*)
from (select distinct M.makerID
from models M 
join cars C on C.modelID = M.id
join sales S on S.carID = C.id
where S.personID = 34) X;
-- 7


select count(*)
from (select distinct M.makerID
from models M 
join cars C on C.modelID = M.id
join sales S on S.carID = C.id
where S.personID = 45) X;
-- 7


-- (c)

drop view if exists makermodelcount;
create view makermodelcount
as
select M.makerID, count(M.id) as modelcount
from models M
group by M.makerID;


select count(*)
from makermodelcount
where modelcount = (select min(modelcount)
from makermodelcount);
-- 6

select makerID
from makermodelcount
where modelcount = (select max(modelcount)
from makermodelcount);
-- 10


-- (d)

select count(*)
from cars C
where C.id not in (
    select S.carID
    from sales S
    group by S.carID
    having count(S.carID) >= 2);
-- 818


-- (e)

drop view if exists carsales;
create view carsales
as
select S.carID, count(S.carID) as carsales
from sales S 
group by S.carID;

select S.carsales
from cars C
join carsales S on S.carID = C.id
where C.licence = 'LX363';
-- 11

select C.licence
from cars C
join carsales S on S.carID = C.id
where S.carsales = (select max(carsales) 
    from carsales);
-- SI998


-- (f)

select count(*)
from (select S.personID
    from sellers S
    where S.saleID not in (select S.saleID
        from sellers S
        group by S.saleID
        having count(S.personID) > 1)
    group by S.personID
    having count(S.saleID) > 0
        ) X;
-- 544


-- (g)

select count(*)
from (select S.personID
from sales S
join cars C on C.id = S.carID
join models M on M.id = C.modelID
join makers K on K.id = M.makerID
where K.name = 'LAMBORGHINI'
group by S.personID
having count(distinct M.id) = (
    select count(M.id)
    from models M
    join makers K on K.id = M.makerID
    where K.name = 'LAMBORGHINI'
)) X;

-- 23

select count(*)
from (select S.personID
from sales S
join cars C on C.id = S.carID
join models M on M.id = C.modelID
join makers K on K.id = M.makerID
where K.name = 'VOLVO'
group by S.personID
having count(distinct M.id) = (
    select count(M.id)
    from models M
    join makers K on K.id = M.makerID
    where K.name = 'VOLVO'
)) X;
-- 5

select count(*)
from (
    select C.id
    from cars C 
    join models M on M.id = C.modelID
    where C.prodyear < M.firstyear
    union all
    select C.id
    from cars C
    join models M on M.id = C.modelID
    where C.prodyear > M.lastyear
) X;
-- 3766