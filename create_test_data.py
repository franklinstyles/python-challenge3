from db import Database
from band import Band
from venue import Venue
from concert import Concert

def create_test_data(db):
    # Clear existing data
    db.execute_query("DELETE FROM concerts;")
    db.execute_query("DELETE FROM bands;")
    db.execute_query("DELETE FROM venues;")
    
    # Create some test data
    db.execute_query("INSERT INTO bands (name, hometown) VALUES ('The Rockers', 'New York')")
    db.execute_query("INSERT INTO bands (name, hometown) VALUES ('The Drummers', 'Chicago')")
    db.execute_query("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
    db.execute_query("INSERT INTO venues (title, city) VALUES ('The Forum', 'Chicago')")
    db.execute_query("INSERT INTO concerts (band_name, venue_title, date) VALUES ('The Rockers', 'Madison Square Garden', '2024-09-15')")
    db.execute_query("INSERT INTO concerts (band_name, venue_title, date) VALUES ('The Drummers', 'The Forum', '2024-09-16')")

def test_methods(db):
    rockers = Band('The Rockers', 'New York', db)
    drummers = Band('The Drummers', 'Chicago', db)
    garden = Venue('Madison Square Garden', 'New York', db)
    forum = Venue('The Forum', 'Chicago', db)

    print("Rockers' Introductions:")
    print(rockers.all_introductions())

    print("Venue Concerts on '2024-09-15':")
    print(garden.concert_on('2024-09-15'))

    print("Venue Most Frequent Band:")
    print(garden.most_frequent_band())

    print("Most Performances:")
    print(Band.most_performances(db))

if __name__ == "__main__":
    db = Database()
    create_test_data(db)
    test_methods(db)
