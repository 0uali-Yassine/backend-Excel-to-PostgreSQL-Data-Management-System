import psycopg2

class DB:
    conn = None

    def get_connect():
        try:
            DB.conn = psycopg2.connect(
                dbname="ExcelDMS",
                user="postgres",
                password="134559038",
                host="localhost",
                port="5432"
            )
            return DB.conn
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None

    def stop_connect():
        if DB.conn:
            DB.conn.close()
            print("Database connection closed.")
