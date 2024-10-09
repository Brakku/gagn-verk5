-- Database: lokaverk
-- DROP DATABASE IF EXISTS lokaverk;

CREATE DATABASE lokaverk
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table users(
	uid int,
	username varchar(20),
	passw int,
	status int,
	privlage int,
	spurningar integer[]
);

create table spurningar(
	sid int,
	author_id int,
	stype int,
	title text,
	stext text
);


