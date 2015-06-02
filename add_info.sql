INSERT INTO Movies(movie_name, movie_rating)
VALUES ("The Hunger Games:Catching Fire", 7.9),
	("Wreck-it Ralph", 7.8),
	("Her", 8.3);

INSERT INTO Projections(movie_id, proj_type, proj_date, proj_time)
VALUES (1, "3D", date("2014-04-01"), time("19:10")),
       (1, "2D", date("2014-04-01"), time("19:00")),
       (1, "4DX", date("2014-04-02"), time("21:00")),
       (3, "2D", date("2014-04-05"), time("20:20")),
       (2, "3D", date("2014-04-02"), time("22:00"));

INSERT INTO Reservations(username, proj_id, row, col)
VALUES ("RadoRado", 1, 2, 1),
       ("RadoRado", 1, 3, 5),
       ("RadoRado", 1, 7, 8);
