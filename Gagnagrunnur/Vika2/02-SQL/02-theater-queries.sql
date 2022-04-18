-- (c) Bjorn Thor Jonsson, 2016-2021
-- Introduction to Database Design @ ITU
-- Lecture 2: Examples from slides

-- SLIDE 77
-- Actors in the production ‘Hamlet’ who have higher prod_salary than the director of the production.
select R.actor
from Roles r
	join Conducts C on C.production = R.production
where R.production = 'Hamlet'
	and R.prod_salary > C.prod_salary;

-- This variant does not work.  Why?
select R.actor
from Roles r
	natural join Conducts C 
where R.production = 'Hamlet'
	and R.prod_salary > C.prod_salary;

-- SLIDE 78
-- Actors in the production ‘Hamlet’ who have higher base_salary than the director of the production.
select A.actor
from Roles r
	join Conducts C on C.production = R.production
	join Actors A on A.actor = R.actor
	join Directors D on D.director = C.director
where R.production = 'Hamlet'
	and A.base_salary > D.base_salary;

-- SLIDE 79
-- Total prod_salary cost for actors per production, highest first
select R.production, sum(R.prod_salary) as prod_salary_total
from Roles R
group by R.production
order by prod_salary_total desc;

-- SLIDE 80
-- Total salary of each actor in 2015.
select A.actor, sum(R.prod_salary) + A.base_salary as salary_total
from Actors A
	join Roles R on A.actor = R.actor
	join Productions P on R.production = P.production
where P.year = 2015
group by A.actor;

-- SLIDE 81
-- Total salary of each director from 2000, highest first.
select D.director, sum(C.prod_salary) + D.base_salary as salary_total
from Directors D
	join Conducts C on D.director = C.director
	join Productions P on C.production = P.production
where P.year >= 2000
group by D.director
order by salary_total desc;

-- SLIDE 82
-- All actors who live at the same address as some director.
-- This is NOT sufficient
select A.actor
from Actors A 
	join Directors D on A.address = D.address;

-- This is
select distinct A.actor
from Actors A 
	join Directors D on A.address = D.address;

-- SLIDE 83
-- All actors who live at the same address as the director of one of the productions they acted in.
select distinct A.actor
from Actors A 
	join Directors D on A.address = D.address
	join Roles R on R.actor = A.actor
	join Conducts C on C.director = D.director and R.production = C.production;

-- SLIDE 84
-- All actors who had multiple roles in the same production, and the number of roles per production.
select R.actor, R.production, count(*) as num_roles
from Roles R
group by R.actor, R.production
having count(*) > 1;
