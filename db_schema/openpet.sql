CREATE TABLE origin (
    id integer primary key,
    name varchar,
    url varchar
);
CREATE TABLE location (
    id integer primary key,
    name varchar,
    url varchar,
    longitude numeric,
    latitude numeric,
    phone varchar(30)
);
CREATE TABLE species (
    id integer primary key,
    name varchar
);
CREATE TABLE race (
    id integer primary key,
    species_id integer not null references species(id),
    name varchar
);
CREATE TABLE specimen (
    id integer primary key,
    origin_id integer not null references origin(id),
    origin_internal_id varchar,
    race_id integer not null references race,
    location_id integer not null references location,
    sex integer,
    birthdate datetime,
    entrydate datetime,
    summary varchar,
    description text,
    image varchar
);
