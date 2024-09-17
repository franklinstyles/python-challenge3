class Concert:
    def __init__(self, id, db):
        self.id = id
        self.db = db

    def band(self):
        query = """
        SELECT * FROM bands
        WHERE name = (
            SELECT band_name FROM concerts
            WHERE id = ?
        );
        """
        result = self.db.execute_query(query, (self.id,))
        return result[0] if result else None

    def venue(self):
        query = """
        SELECT * FROM venues
        WHERE title = (
            SELECT venue_title FROM concerts
            WHERE id = ?
        );
        """
        result = self.db.execute_query(query, (self.id,))
        return result[0] if result else None

    def hometown_show(self):
        query = """
        SELECT COUNT(*) > 0 AS is_hometown
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.id = ? AND bands.hometown = venues.city;
        """
        result = self.db.execute_query(query, (self.id,))
        return result[0][0] == 1 if result else False

    def introduction(self):
        query = """
        SELECT 'Hello ' || venues.city || '!!!!! We are ' || bands.name || ' and we\'re from ' || bands.hometown AS intro
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.id = ?;
        """
        result = self.db.execute_query(query, (self.id,))
        return result[0][0] if result else None
