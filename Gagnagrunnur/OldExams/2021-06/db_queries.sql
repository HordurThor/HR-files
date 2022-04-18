-- (a)

select count(*) 
from clubs C
join cities I on I.id = C.cityID
where I.name = 'London';
-- 6

-- (b)

select count(*) 
from (select distinct W.playerID
from signedwith W
where W.clubID not in (
    select C.id
    from clubs C)) X;
-- 7

-- (c)
drop view if exists awaywins;
create view awaywins
as
select M.awayID, count(M.awaywin) as wins
from matches M
where M.awaywin = true
group by M.awayID;


select count(*)
from awaywins 
where wins = (
    select max(wins)
    from awaywins);
-- 2

-- (d)

select sum(M.awaygoals)
from matches M
join signedwith W on W.clubID = M.awayID and W.seasonID = M.seasonID
join players P on P.id = W.playerID
where P.name = 'Steven Gerrard';
-- 62

drop view if exists teamplayers;
create view teamplayers
as
select W.playerID, count(distinct W.clubID) as count_clubs
from signedwith W
group by W.playerID;

-- (e)

select P.name
from teamplayers T
join players P on P.id = T.playerID
where T.count_clubs = (
    select max(T2.count_clubs)
    from teamplayers T2
)
-- Ruud van Nistelrooy

-- (f)

select count(*)
from players P
where P.id not in (
    select W.playerID
    from signedwith W
    join clubs C on C.id = W.clubID
    join cities S on S.id = C.cityID
    where S.name = 'London'
)
-- 22

-- (g)

select count(*)
from (select M.awayID, count(distinct M.homeID)
from clubs C
join cities S on S.id = C.cityID
join matches M on M.homeID = C.id
where S.name = 'London' and M.awaywin
group by M.awayID
having count(distinct M.homeID) = (
    select count(*)
    from clubs C
    join cities S on  C.cityID = S.id
    where S.name = 'London'
    )
) X;
-- 14

-- (h)

drop view if exists points;
create view points
as
select M.awayID as clubID, 3 as points, M.seasonID
from matches M
where M.awaygoals > M.homegoals
union all
select M.awayID, 1, M.seasonID
from matches M
where M.awaygoals = M.homegoals
union all
select M.homeID, 3, M.seasonID
from matches M
where M.homegoals > M.awaygoals
union all
select M.homeID, 1, M.seasonID
from matches M
where M.homegoals = M.awaygoals;

select C.name, sum(P.points) as points
from points P
join clubs C on C.id = P.clubID
where P.seasonID = 2035
group by C.name
order by sum(P.points) DESC; 
-- 	
--      name     points
-- 1	Chelsea	    63
-- 2	West Ham	62
-- 3	Fulham	    62
-- 4	FCK	        61
-- 5	AC	        60