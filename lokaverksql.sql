

drop table if EXISTS users;
create table users(
	uid int,
	username varchar(20),
	passw int,
	status int,
	privlage int,
	spurningar integer[]
);

drop table if EXISTS spurningar;
create table spurningar(
	sid int,
	author_id int,
	stype int,
	title text,
	stext text
);

INSERT INTO spurningar(sid)
values (1);

SELECT * from spurningar


