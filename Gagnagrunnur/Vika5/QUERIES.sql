-- a.
select count(*) as count_no_height
from person
where height is Null;

-- b.
select count(*) as name_harrison_or_ford
from person
where name like 'Harrison%' or name like '%Ford';

-- c.
select count(*) as movies_with_avg_height_190
from (select movieid, avg(height)
    from person P
    join involved I on I.personid = P.id
    group by movieid
    having avg(height) < 190) X;

-- d.
select count(*) as movies_with_dublicate_genre_entry
from (select distinct M.title, G.genre, count(G.genre)
    from movie M
    join movie_genre MG on MG.movieid = M.id
    join genre G on G.genre = MG.genre
    group by M.title, G.genre
    having count(G.genre) > 1) X;

-- e.
select count(distinct I.personid) as actors_in_spielberg_movies
from (select I.movieid
    from involved I 
    join person P on I.personid = P.id
    where P.name like 'Steven Spielberg' and I.role like 'director') X
join involved I on X.movieid = I.movieid
where I.role like 'actor';

-- f.
select count(*) as Movies_not_reg_in_involved_1999
from involved I
right join movie M on I.movieid = M.id 
where I.movieid is Null and M.year = 1999;

-- g.
select count(*) as director_and_actor
from (select I.personid, count(I.movieid)
    from(select I.personid, I.movieid
        from  involved I 
        where I.role like 'director') X
    join involved I on X.personid = I.personid
    where I.role like 'actor' and X.movieid = I.movieid
    group by I.personid
    having count(I.movieid) > 1) Y;

-- h.
select count(*) as director_and_actor_in_roles
from (select distinct M.title
    from (select I.movieid, I.role
        from involved I
        join movie M on I.movieid = M.id
        where I.role like 'director' and year = 1999) X
    join involved I on X.movieid = I.movieid
    join movie M on I.movieid = M.id
    where I.role like 'actor' and X.movieid = I.movieid) Y;

-- i.
select count(*) as actors_in_all_genres_in_cata_lame
from (select I.personid, count(distinct G.genre)
    from involved I
    join movie_genre MG on I.movieid = MG.movieid
    join genre G on MG.genre = G.genre
    where G.category like 'Lame'
    group by I.personid
    having count(distinct G.genre) = (select count(distinct G.genre) as count_genras
        from involved I
        join movie_genre MG on I.movieid = MG.movieid
        join Genre G on MG.genre = G.genre
        where G.category like 'Lame')) X;

-- j.
select X.title
from (select M.title, count(MR.toid) as count_references
    from movie_reference MR
    join movie M on MR.toid = M.id
    group by M.title
    order by count_references desc limit 1) X;

 