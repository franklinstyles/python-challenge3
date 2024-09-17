-- Create the bands table
CREATE TABLE IF NOT EXISTS bands (
    name TEXT PRIMARY KEY,
    hometown TEXT NOT NULL
);

-- Create the venues table
CREATE TABLE IF NOT EXISTS venues (
    title TEXT PRIMARY KEY,
    city TEXT NOT NULL
);

-- Create the concerts table
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_name TEXT NOT NULL,
    venue_title TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_name) REFERENCES bands (name),
    FOREIGN KEY (venue_title) REFERENCES venues (title)
);
