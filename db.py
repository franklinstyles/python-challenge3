import sqlite3

class Database:
    def __init__(self, db_name='music.db'):
        self.db_name = db_name

    def execute_query(self, query, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            conn.commit()
            return result
        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}")
            conn.rollback()
        except sqlite3.OperationalError as e:
            print(f"OperationalError: {e}")
        finally:
            conn.close()
