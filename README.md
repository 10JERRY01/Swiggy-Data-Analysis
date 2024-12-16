# Swiggy-Data-Analysis-Dashboard
## Overview
- This project is a Flask web application that allows users to visualize and analyze Swiggy restaurant data stored in an SQLite database. The data is processed, analyzed, and presented through a user-friendly dashboard. The application supports various analysis options such as filtering by city, restaurant, and food type, and generates insights on restaurant pricing, ratings, and delivery times.

- The goal of this project is to help stakeholders (e.g., Swiggy team, restaurant owners) gain actionable insights from the data and make data-driven decisions.

## Features
- Data Ingestion: The project supports loading restaurant data from a CSV file into an SQLite database.
- Data Visualization: The dashboard displays key statistics such as average ratings, delivery times, and price distributions.
- User Interactivity: Users can interact with the dashboard by selecting analysis options to filter and view the data in different ways.
- Self-Serve Analysis: A simple self-serve interface allows users to select analysis parameters and generate custom insights.
## Technologies Used
- Flask: A micro web framework for building the web application.
- SQLite: A lightweight database used for storing the restaurant data.
- pandas: A powerful library for data manipulation and analysis.
- Jinja2: Template engine used to render dynamic HTML pages.
- HTML, CSS, Bootstrap: For styling the dashboard and making it responsive.
- Matplotlib/Seaborn: Libraries for generating charts and visualizations.
## Prerequisites
Before you can run this project, make sure you have the following installed:

- Python 3.x
- Flask
- pandas
- SQLite (SQLite comes bundled with Python, so no need for a separate installation)
- Matplotlib and Seaborn (optional, for visualizations)
'''
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('swiggy_data.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        ID INTEGER PRIMARY KEY,
        Area TEXT,
        City TEXT,
        Restaurant TEXT,
        Price REAL,
        Avg_ratings REAL,
        Total_ratings INTEGER,
        Food_type TEXT,
        Address TEXT,
        Delivery_time INTEGER
    )
''')

# Insert some sample data (add more rows if needed)
cursor.executemany('''
    INSERT INTO swiggy_data (Area, City, Restaurant, Price, Avg_ratings, Total_ratings, Food_type, Address, Delivery_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('Area1', 'City1', 'Restaurant1', 200, 4.5, 1200, 'Chinese', 'Address1', 30),
    ('Area2', 'City1', 'Restaurant2', 350, 4.2, 800, 'Biryani', 'Address2', 35),
    ('Area3', 'City2', 'Restaurant3', 150, 3.8, 200, 'North Indian', 'Address3', 40),
    # Add more rows as needed
])

# Commit the changes and close the connection
conn.commit()
conn.close()
3. Run the Flask Application
Once the database is set up, you can run the Flask application:

python app.py
The application will be hosted on http://localhost:5000/. Open this URL in your browser to access the dashboard.
'''
## Application Flow
- Home Page: The homepage displays an overview of the application and provides a form to choose analysis options.
- Analysis Page: Based on the user's input, the application will generate the requested analysis and display the results (e.g., filtered data, charts, statistics).
- Reports: The analysis results are displayed in a tabular format and as visual graphs.
- Data Export: Users can download the analyzed data (if the export feature is implemented).
## Features to Implement
- Data Export: Allow users to download filtered or analyzed data as CSV files.
- Charts & Visualizations: Add more detailed charts for trends, distribution, and correlation analysis.
- User Authentication: Implement user login to restrict access to certain analysis features.
- Performance Optimization: Handle large datasets more efficiently by using SQL queries and optimizing the Flask app.
## Future Enhancements
- Integrate real-time data updates from Swiggy API (if available).
- Provide more granular filters (e.g., by specific delivery times, price range).
- Improve the frontend with better visualizations using libraries like Plotly.
- Implement authentication to secure access to sensitive data.
## ML/AI Based future enhancements
- Recommendation System:
Build a recommendation system to suggest the best restaurants based on user preferences (e.g., food type, price range, city). You can implement a collaborative filtering or content-based recommendation algorithm to suggest restaurants that are similar to the ones a user has previously rated highly.
- AI-Powered Insights:
Integrate AI models to generate actionable insights automatically. For example, use Natural Language Generation (NLG) to summarize trends in data (e.g., "The average delivery time has decreased by 5% in the last month"). This can be displayed as part of the dashboard for easy consumption by non-technical stakeholders.
- Customer Segmentation:
Use unsupervised learning techniques (e.g., K-Means or DBSCAN) to segment customers based on their preferences, spending behavior, and ordering habits. This can help restaurants tailor marketing strategies, promotions, and offers to specific customer groups.
Conclusion
This project provides a scalable, self-serve data analysis platform for Swiggy restaurant data. Users can easily filter, visualize, and analyze data based on various parameters. The project serves as a foundation for building more advanced features like real-time analytics and interactive dashboards.
