class Band:
    def __init__(self, name, hometown, db):
        self.name = name
        self.hometown = hometown
        self.db = db

    def play_in_venue(self, venue_title, date):
        query = """
        INSERT INTO concerts (band_name, venue_title, date)
        VALUES (?, ?, ?);
        """
        self.db.execute_query(query, (self.name, venue_title, date))

    def all_introductions(self):
        query = """
        SELECT 'Hello ' || venues.city || '!!!!! We are ' || bands.name || ' and we\'re from ' || bands.hometown AS intro
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        JOIN venues ON concerts.venue_title = venues.title
        WHERE bands.name = ?;
        """
        results = self.db.execute_query(query, (self.name,))
        if results is None:
            print("No results found for introductions.")
            return []
        return [result[0] for result in results]

    @staticmethod
    def most_performances(db):
        query = """
        SELECT band_name
        FROM concerts
        GROUP BY band_name
        ORDER BY COUNT(*) DESC
        LIMIT 1;
        """
        result = db.execute_query(query)
        return result[0][0] if result else None
