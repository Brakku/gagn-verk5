
drop table if EXISTS lausnir;
create table lausnir(
	lid int,
	author_id int,
	spurn_id int,
	texti text,
	rating int
);

drop table if EXISTS users;
create table users(
	uid int,
	username varchar(20) unique,
	passw text,
	status int,
	privlage int
);



drop table if EXISTS spurningar;
create table spurningar(
	sid int,
	author_id int,
	stype int,
	title text,
	stext text
);

drop PROCEDURE if EXISTS addlausn;
CREATE PROCEDURE addlausn(lid int,author_id int,spurn_id int,texti text,rating int)
LANGUAGE SQL
AS $$
INSERT INTO  lausnir
VALUES (lid,author_id,spurn_id,texti,rating);
$$;

drop PROCEDURE if EXISTS addspurning;
CREATE PROCEDURE addspurning(sid int,author_id int,stype int,title text,stext text)
LANGUAGE SQL
AS $$
INSERT INTO  spurningar
VALUES (sid,author_id,stype,title,stext);
$$;

drop PROCEDURE if EXISTS adduser;
CREATE PROCEDURE adduser(uid integer, username varchar(20),	passw text,status int,privlage int)
LANGUAGE SQL
AS $$
INSERT INTO  users
VALUES (uid,username,passw,status,privlage);
$$;

drop PROCEDURE if EXISTS upuser;
CREATE PROCEDURE upuser(iid integer, iusername varchar(20),	ipassw text,istatus int,iprivlage int)
LANGUAGE SQL
AS $$
UPDATE users
SET username=iusername, passw = ipassw, status = istatus, privlage = iprivlage
WHERE uid =iid; 
$$;

drop PROCEDURE if EXISTS upspurning;
CREATE PROCEDURE upspurning(iid int,iauthor_id int,istype int,ititle text,istext text)
LANGUAGE SQL
AS $$
UPDATE spurningar
SET author_id=iauthor_id, stype=istype, title=ititle, stext=istext
WHERE sid =iid; 
$$;


drop PROCEDURE if EXISTS deluser;
CREATE PROCEDURE deluser(iid int)
LANGUAGE SQL
AS $$
DELETE FROM users WHERE uid = iid and status =1
$$;

drop PROCEDURE if EXISTS delspur;
CREATE PROCEDURE delspur(iid int)
LANGUAGE SQL
AS $$
DELETE FROM spurningar WHERE sid = iid
$$;

drop PROCEDURE if EXISTS dellausn;
CREATE PROCEDURE dellausn(iid int)
LANGUAGE SQL
AS $$
DELETE FROM lausnir WHERE lid = iid
$$;



drop PROCEDURE if EXISTS adminchangestatus;
CREATE PROCEDURE adminchangestatus(iid integer, istatus int)
LANGUAGE SQL
AS $$
UPDATE users
SET status = istatus
WHERE uid =iid; 
$$;