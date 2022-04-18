-- a.
select count(title) as hoursongs
from songs 
where extract(hours from duration) >= 1;

-- b.
select SUM(extract('epoch' from duration)) as all_song_duration_seconds
from songs;

-- c.
select count(A.album) as albums_TomWaits
from albums A
join albumartists AA on AA.albumid = A.albumid
join artists AR on AR.artistid = AA.artistid
where AR.artist = 'Tom Waits';

-- d.
select count(A.album) as albums_alt
from albums A 
join albumgenres AG on A.albumid = AG.albumid
join genres G on G.genreid = AG.genreid
where G.genre like 'Alt%'; 

-- e.
select count(count_titles) as dublicate_songs
from (select count(title) as count_titles
from songs 
group by title
having count(*) > 1) as titles;

-- f.
select avg(count_genres) as avg_genre_per_album
from (select count(G.genre) as count_genres
from albums A
join albumgenres AG on A.albumid = AG.albumid
join genres G on G.genreid = AG.genreid
group by A.album) as avg_genre;

-- g.
select count(A.album) as not_rock
from albums A
join albumgenres AG on AG.albumid = A.albumid
join genres G on G.genreid = AG.genreid
where G.genre not like 'Rock';

-- h.
select MAX(num_songs_year) as max_songs_in_year
from (select extract(year from releasedate) as Year, COUNT(title) num_songs_year
from songs 
group by Year) I;

-- i.
select year from (
select extract(year from releasedate) as year, count(*) as num 
from songs S
group by year
having count(*) = (SELECT MAX(num_songs_year) num
from (select extract(year from releasedate) as Year, COUNT(title) num_songs_year
from songs 
group by Year) I)) test;

-- j.
SELECT DISTINCT(songid), title
from (select extract(year from releasedate) as year, S.songid, S.title, S.duration
from songs S
    join songgenres SG on S.songid = SG.songid
    join genres G on SG.genreid = G.genreid
    join albumsongs ALS on S.songid = ALS.songid
    join albums A on ALS.albumid = A.albumid) I
where year = 1979 and extract(minutes from duration) > 3
order by title