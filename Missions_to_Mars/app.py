from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_marslist_app"
mongo = PyMongo(app)



# Default route
@app.route("/")
def index():
    listings = mongo.db.marslistings.find_one()
    return render_template("index.html", listings=listings)

# Scarping data route
@app.route("/scrape")
def scraper():
    listings = mongo.db.marslistings
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
