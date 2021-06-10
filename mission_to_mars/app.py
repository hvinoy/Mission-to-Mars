from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars



app = Flask(__name__)


@app.route("/scrape")
def scraper():
 
    marspage = scrape_mars.scrape()
    

if __name__ == "__main__":
    app.run(debug=True)