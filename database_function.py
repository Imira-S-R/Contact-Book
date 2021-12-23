import psycopg2
from config import config
from connect import connect

def create_table () :
    commands = """
        CREATE TABLE contact_book_table (
        id serial PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        number BIGINT NOT NULL
        );
        """
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_contact(name, number):
    """ insert a new vendor into the vendors table """
    sql = """
    INSERT INTO 
    contact_book_table (name, number)
    VALUES(%s, %s) RETURNING id;
    """
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name, number,))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id

def delete_contact (id) :
    sql = f"""
    DELETE FROM contact_book_table WHERE "id" = {id};
    """
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        cur.execute(sql, (id))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id

def get_records():
    # SQL to get records from Postgres
    s = "SELECT * FROM contact_book_table"
    # Error trapping
    conn = None
    contacts = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Execute the SQL
        cur.execute(s)
        # Retrieve records from Postgres into a Python List
        contacts = cur.fetchall()
    except psycopg2.Error as e:
        t_message = "Database error: "
        print(t_message)
    
    # Close the database cursor and connection
    cur.close()
    conn.close()

    return contacts

def update_contact(id, name, number):
    sql = """UPDATE contact_book_table
              SET name = %s, 
              number = %s
              WHERE id = %s;
              """
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name, number, id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

