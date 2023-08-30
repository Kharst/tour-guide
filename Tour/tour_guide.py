import streamlit as st
import sqlite3

st.set_page_config(page_title="Tour Guide", page_icon=":tada:", layout="wide")

st.title("South Africa Tour Guide")
st.header("Available Tours")
st.write("This is an application for a Tour Guide.")

# Create or connect to the SQLite database
conn = sqlite3.connect("tour_guide.db")
cursor = conn.cursor()

# Sample tour data (replace this with actual data from your database)
tours = [
    {
        "id": 1,  # This is an example ID, replace with actual IDs from the database
        "name": "Cape Town City Tour",
        "description": "Explore the beautiful city of Cape Town and its landmarks.",
        "itinerary": "Day 1: Table Mountain, Day 2: Robben Island...",
        "price": "$150",
    },
    {
        "id": 2,  # This is an example ID, replace with actual IDs from the database
        "name": "Safari Adventure",
        "description": "Embark on an exciting safari adventure in Kruger National Park.",
        "itinerary": "Day 1: Game drive, Day 2: Bush walk...",
        "price": "$300",
    },
    # Add more tour objects here...
]


# Display each tour
for tour in tours:
    tour_name = tour["name"]
    # Unique key for each form
    tour_key = f"booking_form_{tour_name.replace(' ', '_')}"
    with st.form(key=tour_key):
        st.subheader(tour_name)
        st.write(tour["description"])
        st.write("Itinerary:", tour["itinerary"])
        st.write("Price:", tour["price"])

        # Booking form
        num_participants = st.number_input(
            "Number of Participants", min_value=1, value=1)
        tour_date = st.date_input("Select a Date")

        submit_button = st.form_submit_button("Book Now")

        # Handle booking submission
        if submit_button:
            # Save booking to database (replace this with actual logic)
            cursor.execute("INSERT INTO bookings (tour_id, num_participants, tour_date) VALUES (?, ?, ?)",
                           (tour["id"], num_participants, tour_date))
            conn.commit()
            st.success(
                f"Booking for {tour_name} on {tour_date} for {num_participants} participants was successful!")

# Close the database connection
conn.close()
