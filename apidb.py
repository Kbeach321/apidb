from flask import Flask, jsonify  ##imports flask from Flask##
app = Flask(__name__) ##creates an instance of Flask##
import records
db = records.Database("postgres://localhost/sports_analysis")


@app.route("/") # Routes to another page # Application Route # [Function Decoration] #
def sports_table():
    rows = db.query("SELECT * FROM epl_data;")
    return jsonify(rows.export('json'))
