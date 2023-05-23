import pymysql
import hashlib
import datetime

config1 = {
    'host': '10.225.148.138',
    'user': 'root',
    'password': '1234',
    'database': 'teamdevopsuia',
}

config2 = {
    'host': 'us-cdbr-east-06.cleardb.net',
    'user': 'username',
    'password': 'password',
    'database': 'heroku_66e39329c433106',
}


def list_users():
    
    try:
        cnx = pymysql.connect(**config1)
    except pymysql.err.OperationalError:
        cnx = pymysql.connect(**config2)
    cursor = cnx.cursor()
    query = "SELECT user_id FROM users;"
    cursor.execute(query)
    result = [x[0] for x in cursor.fetchall()]

    cursor.close()
    cnx.close()

    return result

def verify(id, pw):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT password FROM users WHERE user_id = %s;"
    cursor.execute(query, (id,))
    result = cursor.fetchone()[0] == hashlib.sha256(pw.encode()).hexdigest()

    cursor.close()
    cnx.close()

    return result

def delete_user_from_db(id):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "DELETE FROM users WHERE user_id = %s;"
    cursor.execute(query, (id,))
    cnx.commit()

    query = "DELETE FROM notes WHERE user_id = %s;"
    cursor.execute(query, (id,))
    cnx.commit()

    query = "DELETE FROM images WHERE user_id = %s;"
    cursor.execute(query, (id,))
    cnx.commit()

    cursor.close()
    cnx.close()

def add_user(id, pw):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "INSERT INTO users (user_id, password) VALUES (%s, %s);"
    cursor.execute(query, (id.upper(), hashlib.sha256(pw.encode()).hexdigest()))
    cnx.commit()

    cursor.close()
    cnx.close()

def read_note_from_db(id):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT note_id, timestamp, note FROM notes WHERE user_id = %s;"
    cursor.execute(query, (id.upper(),))
    result = cursor.fetchall()

    cursor.close()
    cnx.close()

    return result

def match_user_id_with_note_id(note_id):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT user_id FROM notes WHERE note_id = %s;"
    cursor.execute(query, (note_id,))
    result = cursor.fetchone()[0]

    cursor.close()
    cnx.close()

    return result

def write_note_into_db(id, note_to_write):
    cnx = pymysql.connect(**config)
    cursor = cnx.cursor()

    current_timestamp = str(datetime.datetime.now())
    query = "INSERT INTO notes (user_id, timestamp, note, note_id) VALUES (%s, %s, %s, %s);"
    cursor.execute(query, (id.upper(), current_timestamp, note_to_write, hashlib.sha1((id.upper() + current_timestamp).encode()).hexdigest()))
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

def image_upload_record(uid, user_id, name, timestamp):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "INSERT INTO images (image_id, user_id, name, timestamp) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (uid, user_id, name, timestamp))
        connection.commit()

        cursor.close()
        connection.close()
    except pymysql.Error as error:
        print("Hata:", error)

def list_images_for_user(user_id):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "SELECT image_id, timestamp, name FROM images WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result
    except pymysql.Error as error:
        print("Hata:", error)

def match_user_id_with_image_uid(image_uid):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "SELECT user_id FROM images WHERE image_id = %s;"
        cursor.execute(query, (image_uid,))
        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result
    except pymysql.Error as error:
        print("Hata:", error)

def delete_image_from_db(image_uid):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        query = "DELETE FROM images WHERE image_id = %s;"
        cursor.execute(query, (image_uid,))
        connection.commit()

        cursor.close()
        connection.close()
    except pymysql.Error as error:
        print("Hata:", error)

if __name__ == "__main__":
    print(list_users())
