import os

# Create the SQLite database
os.system("python create_database.py")

# Run the Streamlit app
os.system("streamlit run tour_guide_app.py")
