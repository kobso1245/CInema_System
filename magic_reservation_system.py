import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def show_movies():
    result = cursor.execute("SELECT id, name, rating FROM Movies")
    print("Current movies:")
    for row in result:
        print("[{}] - {} ({})".format(row[0], row[1], row[2]))


def show_movie_projections(movieID, movieDATE=""):

    create_movie_pick_up_table = """
    CREATE TABLE movie_pick_up(
        movie_ID INT,
        movie_DATE DATE
    )"""

    fill_movie_pick_up = """
    INSERT INTO movie_pick_up(movie_ID, movie_DATE)
    VALUES(?, ?)
    """

    cursor.execute("DROP TABLE IF EXISTS movie_pick_up")
    cursor.execute(create_movie_pick_up_table)
    cursor.execute(fill_movie_pick_up, (movieID, movieDATE))
    conn.commit()

    get_movie = """SELECT name
    FROM movies
    JOIN movie_pick_up
    ON movies.id = movie_pick_up.movie_ID
    """
    movie = cursor.execute(get_movie).fetchone()

    if movieDATE == "":

        print("Projections for movie '{}':".format(movie[0]))
        conn.commit()

        projections_for_movie_id = """
        SELECT id, proj_date, proj_time, type
        FROM projections
        JOIN movie_pick_up
        ON projections.movie_id = movie_pick_up.movie_ID
        """

        result = cursor.execute(projections_for_movie_id)
        for row in result:
            print("[{}] - {} {} ({})".format(row[0], row[1], row[2], row[3]))

    else:

        print("Projections for movie '{}' on date {}:".format(movie[0], movieDATE))
        conn.commit()

        projections_for_movie_id = """
        SELECT id, proj_time, type
        FROM projections
        JOIN movie_pick_up
        ON projections.movie_id = movie_pick_up.movie_ID
        AND proj_date = movie_DATE
        """

        result = cursor.execute(projections_for_movie_id)
        for row in result:
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))

