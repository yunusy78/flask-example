import pymysql
from pymysql import Error
import datetime
import hashlib


# MySQL configurations       for
config = {
    'user': 'root',
    'password': '4922',
    'host': 'localhost',
    'database': 'sys'
}

def list_users():
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT name FROM users;"
    cursor.execute(query)
    result = [x[0] for x in cursor.fetchall()]

    cursor.close()
    cnx.close()

    return result

def verify(user_id, name):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT user_id FROM users WHERE user_id = %s;"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()[0] == hashlib.sha256(name.encode()).hexdigest()

    cursor.close()
    cnx.close()

    return result


def delete_user_from_db(id):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "DELETE FROM users WHERE user_id = %s;"
    cursor.execute(query, (id,))
    cnx.commit()

    # When we delete a user from the database USERS, we also need to delete all their notes data from database NOTES
    query = "DELETE FROM notes WHERE user_id = %s;"
    cursor.execute(query, (id,))
    cnx.commit()

    # When we delete a user from the database USERS, we also need to
    # [1] delete all their images from image pool (done in app.py)
    # [2] delete all their images records from database IMAGES
    query = "DELETE FROM images WHERE user_id = %s;"
    cursor.execute(query, (id,))
    cnx.commit()

    cursor.close()
    cnx.close()

def add_user(user_id, name):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "INSERT INTO users (user_id, name) VALUES (%s, %s);"
    cursor.execute(query, (user_id.upper(), hashlib.sha256(name.encode()).hexdigest()))
    cnx.commit()

    cursor.close()
    cnx.close()

def read_note_from_db(note_id):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT note_id, timestamp, note FROM notes WHERE user = %s;"
    cursor.execute(query, (note_id.upper(),))
    result = cursor.fetchall()

    cursor.close()
    cnx.close()

    return result

def match_user_id_with_note_id(note_id):
    # Given the note id, confirm if the current user is the owner of the note which is being operated.
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT user FROM notes WHERE note_id = %s;"
    cursor.execute(query, (note_id,))
    result = cursor.fetchone()[0]

    cursor.close()
    cnx.close()

    return result

def write_note_into_db(note_id, note_to_write):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    current_timestamp = str(datetime.datetime.now())
    query = "INSERT INTO notes (user_id, timestamp, note, note_id) VALUES (%s, %s, %s, %s);"
    cursor.execute(query, (note_id.upper(), current_timestamp, note_to_write, hashlib.sha1((note_id.upper() + current_timestamp).encode()).hexdigest()))
    cnx.commit()
    cursor.close()
    cnx.close()

def delete_note_from_db(note_id):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()
    query = "DELETE FROM notes WHERE note_id = %s;"
    cursor.execute(query, (note_id,))
    cnx.commit()
    cursor.close()
    cnx.close()


def image_upload_record(image_id, user_id, name, timestamp):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "INSERT INTO images (image_id, user_id, name, timestamp) VALUES (%s, %s, %s, %s)"
        values = (image_id, user_id, name, timestamp)
        cursor.execute(query, values)

        connection.commit()
        print(cursor.rowcount, "record inserted.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")



def list_images_for_user(user_id):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "SELECT image_id, timestamp, name FROM images WHERE user_id = %s"
        value = (user_id,)
        cursor.execute(query, value)

        result = cursor.fetchall()

        return result

    except Error as error:

        print(f"Error: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def match_user_id_with_image_uid(image_id):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "SELECT user_id FROM images WHERE image_id = %s"
        value = (image_id,)
        cursor.execute(query, value)

        result = cursor.fetchone()[0]

        return result

    except Error as error:

        print(f"Error: {error}")


    finally:

        try:

            if cursor:
                cursor.close()

        except NameError:

            pass

        try:

            if connection and connection.is_connected():
                connection.close()

        except NameError:

            pass

        print("MySQL connection is closed.")


def delete_image_from_db(image_id):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "DELETE FROM images WHERE image_id = %s"
        value = (image_id,)
        cursor.execute(query, value)

        connection.commit()
        print(cursor.rowcount, "record(s) deleted.")

    except Error as error:
        print(f"Error: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    print(list_users())
