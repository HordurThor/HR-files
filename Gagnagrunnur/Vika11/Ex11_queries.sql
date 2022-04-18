-- a
select V.name, count(T.TesterID)
from Variants V
join Tests T on V.ID = T.VariantID
where V.name like 'omicron'
group by V.name

-- b
select x.count_tests
from (select count(T.TesterID) as count_tests
from Variants V
join Tests T on V.ID = T.VariantID
group by V.name) x
where count_tests = null;

-- c
select count(distinct V.name)
from Variants V
join Tests T on V.ID = T.VariantID
join Testers Ts on T.TesterID = Ts.ID
join Risks R on V.riskID = R.ID
join Kits K on T.kitID = K.ID
where R.level like 'extreme' 
and Ts.name like 'Kent Lauridsen' 
and K.producer like 'JJ';

-- d
select V.Name
from Variants V
where V.ID not in (select V.ID as variant_id
from Variants V
join Detects D on V.ID = D.VariantID
where D.accuracy > 50);

-- e
select min(avg_acc)
from (select distinct x.ID, avg(D.accuracy) as avg_acc
from (select V.ID, count(D.kitID) as count_kits
from Variants V
join Detects D on V.ID = D.VariantID
group by V.ID) x
join Detects D on x.ID = D.VariantID
where count_kits > 1 
group by x.ID) y

-- f