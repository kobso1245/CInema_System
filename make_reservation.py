from settings import DB_FILE_NAME
CONN = sqlite3.connect(DB_FILE_NAME)
CONN.row_factory = sqlite3.Row

PROMPT_FOR_NAME= "Please write down your name: "
PROMPT_FOR_TICKETS_CNT = "Please write down the number of tickets you need: "
PROMPT_FOR_MOVIE_ID = "Please write down the movie id: "
PROMPT_FOR_PROJECTION_ID = "Please write down the projection id: "


ROWS = 10
COLS = 10
SEATS = ROWS * COLS



COUNT_FOR_PROJECTION_QUERY = '''
SELECT COUNT(proj_id) AS count
FROM Reservations
WHERE proj_id = {}
'''

SHOW_ALL_TAKEN_SEATS_QUERY = '''
SELECT row, col, 
FROM Reservations
WHERE proj_id = {}
'''



def execute_count_projections_query_and_get_result(proj_id):
    cursor = CONN.cursor()
    data = cursor.execute(COUNT_FOR_PROJECTION_QUERY.format(proj_id)).fetchone()
    return data['count']


def has_spots(ticketsi proj_id):
    taken_seats = execute_count_projections_query_and_get_result()
    if tickets + taken_seats > SEATS:
        return False
    else:
        return True


def show_ask_and_return_answer_for_projection_seats(movie_id):
    show_movie_projections(movie_id)
    proj_id = open(PROMPT_FOR_PROJECTION_ID)
    has_available_spots = has_spots(tickets, proj_id)
    return has_available_spots


def execute_show_all_taken_seats_query(proj_id):
    cursor = CONN.cursor()
    data = cursor.execute(SHOW_ALL_TAKEN_SEATS_QUERY.format(proj_id)).fetchall()
    return [(proj['row'], proj['col']) for proj in data]



def get_available_seats(proj_id):
    taken_seats = execute_show_all_taken_seats_query(proj_id)
    all_seats = [(row, col) for row in range(1, ROWS + 1) for col in range(1, COLS+1)]
    set_taken_seats = set(taken_seats)
    set_all_seats = set(all_seats)
    return set_all_seats - set_taken_seats



def print_free_seats(proj_id, available_seats):
    for seat in available_seats:
        print(seat)

def make_reservation():
    name = input(PROMPT_FOR_NAME)
    tickets = input(PROMPT_FOR_TICKETS_CNT)
    show_movies()
    movie_id = input(PROMPT_FOR_MOVIE_ID)
    has_available_spots = show_ask_and_return_answer_for_projection_seats(movie_id)
    while not has_available_spots:
        has_available_spots = show_ask_and_return_answer_for_projection_seats(movie_id)


    available_seats = get_available_seats(proj_id)
    print_free_seats(proj_id, available_seats) 
   


