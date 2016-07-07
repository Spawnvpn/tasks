import MySQLdb
import MySQLdb.cursors


def get_connection():
    connection = MySQLdb.connect(user='root',
                                 passwd='123',
                                 db='books',
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def insert_books(values):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Books (title, ISBN) VALUES (%s, %s)", values)


def select(**kwargs):
    connection = get_connection()
    cursor = connection.cursor()
    q = "SELECT * FROM Books WHERE "
    for key, value in kwargs.items():
        select_id = key
        val = value
        q += "{}={}" .format(select_id, val)
    print(q)
    cursor.execute(q)
    # cursor.execute("SELECT * FROM Books")
    return cursor.fetchall()


# insert_books([
#      ('Book1', 'qwe-123'),
#      ('Book2', 'qwe-1212'),
#     ])


print(select(book_id="1"))

