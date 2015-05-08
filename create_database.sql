DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies(
	movie_id INTEGER PRIMARY KEY,
	movie_name TEXT,
	movie_rating FLOAT
);

DROP TABLE IF EXISTS Projections;

CREATE TABLE Projections(
	proj_id INTEGER PRIMARY KEY,
	movie_id INTEGER,
	proj_type TEXT,
	proj_date DATE,
	proj_time TIME,
	FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
);

DROP TABLE IF EXISTS Reservations;

CREATE TABLE Reservations(
	reserv_id INTEGER PRIMARY KEY,
	username TEXT,
	projection_id INTEGER,
	row INTEGER,
	col INTEGER,
	FOREIGN KEY(proj_id) REFERENCES Projections(proj_id)
);
