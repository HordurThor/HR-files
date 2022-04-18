-- (c) Bjorn Thor Jonsson, 2016-2021
-- Introduction to Database Systems @ ITU
-- Lecture 2: Examples from slides

-- SLIDE 20
-- How many coffees
SELECT *
FROM Coffees;

-- What should this return?
SELECT 1 AS Query
FROM Coffees;

-- What should this return?
SELECT 1 AS Query;

-- SLIDE 21
-- Analog has a 50% discount on a second coffee of the same type.  
-- For each coffee sold there, show the price of two coffees (‘priceOfTwo’):
select coffee, price*1.5 as priceOfTwo
from Sells
where coffeehouse = 'Analog';

-- SLIDE 22
-- A coffeehouse patron named “Bjorn Jonsson” has passed out 
-- from caffeine shock.  Show a query to find his home phone
select phone
from Drinkers
where name = 'Bjorn Jonsson';

-- SLIDE 27
-- A coffeehouse patron by the last name of “Sivertsen” has passed out, 
-- again from caffeine shock.  Show a query to find his home phone
select phone
from Drinkers
where name like '% Sivertsen';

-- SLIDE 28
-- Someone has recommended a coffeehouse that sells coffee called “Blue”-something, 
-- that cost more than 100.  Unfortunately, he doesn’t remember the name of the coffeehouse.  
-- Find where that coffee is sold at such a high price.
select coffeehouse 
from Sells
where coffee like 'Blue%'
  and price > 100;

-- Add another data point (then retry query)
-- Analog should not appear 
insert into coffees values ('Kopi nuevo', 'Kopi Luwak Direct');
insert into sells values ('Analog', 'Kopi nuevo', 300);

-- Add another data point (then retry query)
insert into coffees values ('Blue nuevo', 'Kopi Luwak Direct');
insert into sells values ('Mocha', 'Blue nuevo', 300);

-- Find where that coffee is sold at such a high price, show each coffeehouse only once
select distinct coffeehouse 
from Sells
where coffee like 'Blue%'
  and price > 100;

-- SLIDE 36
-- For each person that “frequents” some coffeehouse, 
-- show the name of the person and the address of the coffeehouse
select drinker, address
from Frequents 
  join Coffeehouses on Frequents.coffeehouse = Coffeehouses.name;

-- Add a non-frequenting drinker, then re-run previous query
insert into Drinkers values ('Peter Sestoft', 'ITU', 55555555);

-- SLIDE 37
-- For each person that “frequents” some coffeehouse, 
-- show the address of the person and the address of the coffeehouse
select Drinkers.address, Coffeehouses.address
from Drinkers 
  join Frequents on Drinkers.name = Frequents.drinker
  join Coffeehouses on Frequents.coffeehouse = Coffeehouses.name;

select D.address, H.address
from Drinkers D
  join Frequents F on D.name = F.drinker
  join Coffeehouses H on F.coffeehouse = H.name;

-- SLIDE 39
-- For each person that “frequents” some coffeehouse, 
-- show the name of the person and the address of the coffeehouse
select Frequents.drinker, Coffeehouses.address
from Frequents
  join Coffeehouses on Frequents.coffeehouse = Coffeehouses.name;

-- Names only
select Frequents.drinker, Frequents.coffeehouse
from Frequents;

-- With IDs -- will not run, of course!
select D.name, H.name 
from Drinkers D
    join Frequents F on D.ID = F.DrinkerID
    join Coffeehouses H on H.ID = F.CoffeehouseID;

-- Drinkers and name of coffeehouses they frequent (if any)
-- Recall that Peter is in Drinkers, not in Frequents
select Drinkers.name, coffeehouse
from Drinkers 
   join Frequents on Drinkers.name = Frequents.drinker;

-- Repeat: *all* drinkers and name of coffeehouses they frequent (if any)
select Drinkers.name, coffeehouse
from Drinkers 
	left outer join Frequents on Drinkers.name = Frequents.drinker ;

-- Names of actual Drinkers (no coffeehouses)
select F.drinker
from Frequents F;

-- Add a frequenting record, repeat previous query
insert into Frequents values ('Johan Sivertsen', 'Mocha');

-- Names of actual Drinkers (without duplicates)
select distinct Frequents.drinker
from Frequents;

-- SLIDE 40
-- Don't use GROUP BY for this!
select F.drinker
from Frequents F
group by F.drinker;

-- And definitely don't use both!!!!
select distinct F.drinker
from Frequents F
group by F.drinker;

-- SLIDE 45
-- Should be 4 price values, 3 distinct
select count(price)
from Sells;

-- Correct way to apply distinct
select count(distinct price)
from Sells;

-- Incorrect way to apply distinct, why?
select distinct count(price)
from Sells;

-- SLIDE 46
-- Show the price of the most expensive coffee (from any coffeehouse)
select max(price)
from Sells;

-- SLIDE 54
-- For each coffeehouse, show the average price of all coffees in that coffeehouse
select coffeehouse, avg(price)
from Sells
group by coffeehouse;

-- SLIDE 55
-- For each coffeehouse, show the number of coffees sold 
-- in that coffeehouse, and the average price
select coffeehouse, count(*), avg(price)
from Sells
group by coffeehouse;

-- SLIDE 56
-- For each coffeehouse, show the average price of the most expensive coffee
select coffeehouse, max(price)
from Sells
group by coffeehouse;

-- SLIDE 58
-- Try to find the name of the coffeehouse with the most expensive coffee!
select coffeehouse, max(price)
from Sells;

-- This works, because when we have coffeehouse, we have price
-- We just don't have the MAX(price)
select coffeehouse, price
from Sells;

-- This works, because we have gone through the entire relation to compute MAX
-- We just don't have the individual coffeehouse names anymore
select max(price)
from Sells;

-- Succeed in finding the name of the coffeehouse with the most expensive coffee!
select coffee, price
from Sells 
where price = (select max(price) from Sells);

-- SLIDE 59
-- Show the name and price of the least expensive coffee (from any coffeehouse).
select coffee, price
from Sells 
where price = (select min(price) from Sells);

-- SLIDE 65
-- For each coffeehouse that sells more than two coffees, 
-- show the number of coffees sold in that coffeehouse and their average price.
select coffeehouse, count(*), avg(price)
from Sells
group by coffeehouse
having count(*) > 2;

-- SLIDE 66
-- For each coffeehouse, show the number of drinkers that frequent the coffeehouse
select coffeehouse, count(*)
from Frequents
group by coffeehouse;

-- SLIDE 67
-- For each drinker that frequents more than one coffeehouse, 
-- show the number of coffeehouses that he/she frequents.
select drinker, count(*)
from Frequents
group by drinker
having count(*) > 1;

-- SLIDE 71
-- Cheapest coffee
select distinct coffee
from Sells
where price = (select min(price) from Sells);

-- Cheapest coffee
-- on average
select distinct coffee
from Sells
group by coffee
having avg(price) = (
    select min(avgprice) 
    from (
        	select avg(price) as avgprice
        	from Sells
        	group by coffee
    ) X
);

-- SLIDE 72
-- Average Price of All Coffees
select avg(price)
from Sells;

-- SLIDE 73
-- Coffees Costing <2000 on Average
select coffee
from Sells
group by coffee
having avg(price) < 2000;

