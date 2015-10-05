SHOW_MOVIES_QUERY = '''
SELECT movie_id, movie_name, movie_rating
FROM Movies
'''


GET_PROJECTION_IDS_QUERY = '''
SELECT proj_id
FROM Projections
WHERE Projections.movie_id = {}
'''
GET_PROJECTION_IDS_WITH_DATE_QUERY = '''
SELECT proj_id
FROM Projections
WHERE Projections.movie_id = {} and Projections.proj_date = date({})
'''

GET_PROJECTION_TIME_DATE_FROM_ID_QUERY = '''
SELECT movie_name, proj_type, proj_date, proj_time
FROM Projections
JOIN Movies
ON Movies.movie_id = Projections.movie_id
WHERE Projections.proj_id = {}
'''

GET_ELEM_COUNT_QUERY = '''
SELECT COUNT(reserv_id) AS count
FROM Reservations
WHERE proj_id = {}
GROUP BY proj_id
'''


OUNT_FOR_PROJECTION_QUERY = '''
SELECT COUNT(proj_id) AS count
FROM Reservations
WHERE proj_id = {}
'''

SHOW_ALL_TAKEN_SEATS_QUERY = '''
SELECT row, col
FROM Reservations
WHERE proj_id = {}
'''

INSERT_INTO_RESERVATIONS = '''
INSERT INTO Reservations(username, proj_id, row, col)
VALUES({}, {}, {}, {})
'''
