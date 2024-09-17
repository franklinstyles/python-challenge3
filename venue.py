class Venue:
    def __init__(self, title, city, db):
        self.title = title
        self.city = city
        self.db = db

    def concert_on(self, date):
        query = """
        SELECT * FROM concerts
        WHERE venue_title = ? AND date = ?
        LIMIT 1;
        """
        result = self.db.execute_query(query, (self.title, date))
        return result

    def most_frequent_band(self):
        query = """
        SELECT band_name
        FROM concerts
        WHERE venue_title = ?
        GROUP BY band_name
        ORDER BY COUNT(*) DESC
        LIMIT 1;
        """
        result = self.db.execute_query(query, (self.title,))
        return result[0][0] if result else None
