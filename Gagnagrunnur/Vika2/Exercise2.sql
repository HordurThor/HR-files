-- 1
SELECT name, record
FROM  sports

-- 2
SELECT distinct name
FROM sports inner join results on sports.ID = results.sportID
WHERE results.result > 0

-- 3
SELECT COUNT(distinct peopleID)
FROM results

-- 4
select peopleID, name
from results join people on results.peopleID = people.ID
Group by results.peopleID, people.name
having count(results.result) >= 20

-- 5
select distinct P.ID,  P.name, G.description
from results R 
join people P on R.peopleID = P.ID
join gender G on G.gender = P.gender
join sports S on R.sportID = S.ID
where S.record = R.result

-- 6
select S.name, count(distinct R.peopleID) as numathletes
from sports S
join results R on S.ID = R.sportID
where R.result = S.record
group by S.name

-- 7
select P.id, P.name, max(R.result) as best, round(cast(S.record - max(R.result) as numeric),2) as difference
from people P
join results R on P.ID = R.peopleID
join sports S on R.sportID = S.ID
where S.name = 'Triple Jump' 
group by P.id, S.record
having count(R.result) >= 20

-- 8
select P.id, P.name, G.description
from people P
join gender G on G.gender = P.gender



-- 14
select P.id, P.name, P.height, max(R.result), S.name, when R.result = S.record then 1 else 0
from  people P
join results R
join sports S

