import sqlite3
import queries as qu

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def show_movies():
    result = cursor.execute(qu.SHOW_MOVIES_QUERY)
    print("Current movies:")
    for row in result:
        print("[{}] - {} ({})".format(row[0], row[1], row[2]))


def get_movie_projections(movie_id, movie_date=""):
    cursor = conn.cursor()
    projections = []
    if movie_date == "":
        proj_ids = cursor.execute(
    qu.GET_PROJECTION_IDS_QUERY.format(movie_id)).fetchall()
    else:
        proj_ids = cursor.execute(
    qu.GET_PROJECTION_IDS_WITH_DATE_QUERY.format(
        movie_id, movie_date)).fetchall()

    if len(proj_ids) == 0:
        print("This projection doesnt exists!")
            return
        else:
        for proj_id in proj_ids:
            proj_count = cursor.execute(
    qu.GET_ELEM_COUNT_QUERY.format(
        proj_id['proj_id'])).fetchall()
            if len(proj_count) == 0:
                projections.append((proj_id['proj_id'], 0))
            else:
                projections.append(
    (proj_id['proj_id'], proj_count[0]['count']))
    return convert_to_projection_onfo_from_proj_id(projections)


def convert_to_projection_onfo_from_proj_id(projections):
    cursor = conn.cursor()
    result = []
    for projection in projections:
        data = cursor.execute(
    qu.GET_PROJECTION_TIME_DATE_FROM_ID_QUERY.format(
        projection[0])).fetchone()
        result.append((data['movie_name'], data['proj_type'], data['proj_date'], data['proj_time'], projection[1]]))

    return result


def show_movie_projections(movie_id, movie_date=""):
    rows = get_movie_projections(movie_id, movie_date)
    for row in rows:
        print("{} {} {} {} {}".format(row[0],
                                    row[1],
                                    row[2],
                                    row[3]))




show_movies()
show_movie_projections(1)









def show_movie_projections2(movieID, movieDATE=""):

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

        print(
    "Projections for movie '{}' on date {}:".format(
        movie[0], movieDATE))
        conn.commit()

        projections_for_movie_id="""
        SELECT id, proj_time, type
        FROM projections
        JOIN movie_pick_up
        ON projections.movie_id = movie_pick_up.movie_ID
        AND proj_date = movie_DATE
        """

        result=cursor.execute(projections_for_movie_id)
        for row in result:
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))
