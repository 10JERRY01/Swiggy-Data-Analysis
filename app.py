import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function for SQLite
def get_db_connection():
    conn = sqlite3.connect('swiggy_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to the homepage with form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get selected analysis type from the form
        analysis_type = request.form['analysis_type']
        
        # Perform corresponding analysis based on user selection
        plot_url = perform_analysis(analysis_type)
        
        return render_template("analysis.html", analysis_type=analysis_type, plot_url=plot_url)
    
    return render_template("index.html")

# Function to perform analysis and generate the corresponding plot
def perform_analysis(analysis_type):
    # Load data from the SQLite database
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM restaurants", conn)
    conn.close()
    
    # Based on the selected analysis type, perform different analyses
    if analysis_type == 'Average Delivery Time by City':
        fig, ax = plt.subplots()
        city_avg_delivery_time = df.groupby('City')['Delivery time'].mean().sort_values(ascending=False)
        city_avg_delivery_time.plot(kind='bar', ax=ax)
        ax.set_title("Average Delivery Time by City")
        ax.set_ylabel("Average Delivery Time (min)")
        ax.set_xlabel("City")
    
    elif analysis_type == 'Price Distribution':
        fig, ax = plt.subplots()
        df['Price'].plot(kind='hist', bins=50, ax=ax)
        ax.set_title("Price Distribution")
        ax.set_xlabel("Price")

    # Convert the plot to a base64 string to display it on the webpage
    plot_url = convert_plot_to_base64(fig)
    return plot_url

# Function to convert a plot to base64 string for embedding in HTML
def convert_plot_to_base64(fig):
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return plot_url

if __name__ == "__main__":
    app.run(debug=True)
