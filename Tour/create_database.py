import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect("tour_guide.db")
cursor = conn.cursor()

# Create a tours table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tours (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        itinerary TEXT,
        price TEXT
    )
""")

# Create a bookings table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tour_id INTEGER,
        num_participants INTEGER,
        tour_date TEXT
    )
""")
conn.commit()

# Close the database connection
conn.close()
