import psycopg2

PGHOST = 'ep-restless-lake-a18z5oa2-pooler.ap-southeast-1.aws.neon.tech'
PGDATABASE = 'koval214'
PGUSER = 'koval214_owner'
PGPASSWORD = 'npg_9P8krcQCRvZF'
PORT = 5432


with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS topic (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            )
        """

        cursor.execute(query)

        query = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                model VARCHAR(50) NOT NULL,
                topic_id INTEGER REFERENCES topic(id),
                customer_id INTEGER REFERENCES customer(id)
            );
            """
        cursor.execute(query)


with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query_insert =  'INSERT INTO topic (name) VALUES (%s)'
        cursor.execute(query_insert, ('Technology',))


        query_insert = 'INSERT INTO topic (name) VALUES (%s) RETURNING id, name'
        cursor.execute(query_insert, ('Science',))
        print(cursor.fetchone())

        query_insert = 'INSERT INTO topic (name) VALUES (%s) RETURNING id, name'
        cursor.execute(query_insert, ('Sports',))
        print(cursor.fetchone())


        query_insert = 'INSERT INTO customer (name) VALUES (%s) RETURNING id, name'
        owners = [
            ('Artur',),
            ('John',),
            ('Alice',),
        ]
        cursor.executemany(query_insert, owners)

        query_insert = 'INSERT INTO posts (model, topic_id, customer_id) VALUES (%s, %s, %s)'
        posts = [
            ('Technology', 1, 2),
            ('Science',1, 1),
            ('Sports',2, 3),
        ]
        cursor.executemany(query_insert, posts)
