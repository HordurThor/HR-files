

-- (a) 

select count(*)
from monitors M
join humans H on H.hid = M.hid
join outlets O on O.oid = H.oid
where O.zip = 200 and M.mrating is not null;
-- 15


-- (b)

select count(*)
from outlets O
where O.oid not in ( 
    select H.oid
    from humans H
    );
-- 2


-- (c)

select count(*)
from sells S
join reviews R on R.sid = S.sid
where R.rwhen < S.swhen;
-- 3425


-- (d)

select P.pname
from produce P
join sells S on S.pid = P.pid
where S.sprice = (
    select max(S.sprice) from sells S
);
-- Bell Peppers
-- Beets


-- (e)

select count(*)
from humans H
where H.hid not in (
    select M.hid
    from monitors M
    where M.mrating is not null
);
-- 810


-- (f)

drop view if exists totalsales;
create view totalsales
as
select S.hid, sum(S.sprice) as totalsales
from sells S
group by S.hid;

select H.hname
from humans H
join totalsales T on T.hid = H.hid
where T.totalsales = (
    select max(totalsales)
    from totalsales
);
-- Luisa Jennudottir


-- (g)

select count(*)
from (
    select distinct S.pid, count(distinct O.oid)
    from sells S
    join humans H on H.hid = S.hid
    join outlets O on O.oid = H.oid
    where O.zip = 200
    group by S.pid
    having count(distinct O.oid) = (
        select count(*)
        from outlets O
        where O.zip = 200
    )
) X;
-- 4


-- (h)

select C.cname, H.hname, S.sprice, S.swhen
from customers C
join sells S on S.cid = C.cid
join reviews R on R.sid = S.sid 
join humans H on H.hid = S.hid and R.hid = H.hid
join outlets O on O.oid = H.oid
where O.zip = 130 and R.hid = S.hid

--       cname      hname             sprice       swhen
-- 1	Sandholt	Bergvin Eggertsson	6055	Sun Dec 25 2016 00:00:00 GMT+0000 (Greenwich Mean Time)