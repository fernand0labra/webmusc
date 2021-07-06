# Import Dependencies
from flask import Flask, render_template, request
from database.dbConfig import startDB, getAuthorInfo, getWorkInfo

###################################################################

# Create the Flask Object
app = Flask(__name__)

# Initialize Database
startDB()

headings = ("Name", "Opus") # Table Headings Definition
data = (("",""), ("NO INFO", "NO INFO")) # Table Data Definition

###################################################################

# Initial Function
@app.route("/")
def start():
    return render_template('index.html', table_headings=headings, table_data=data)

# First Query to the Database [POST]
#    Author :: The author of the work
#    Ttype  :: The type of work
@app.route('/parameters', methods=['POST'])
def parameters():
    # Obtain the user input from the URL
    author = request.form['author']
    ttype = request.form['ttype']

    # Obtain the Database Info
    data = getAuthorInfo(author, ttype)

    if (len(data)==0) :
        data = (("",""), ("NO INFO", "NO INFO"))

    # Render template with Information from the Database
    return render_template('index.html', table_headings=headings, table_data=data)

# Second Query to the Database [GET]
#   Name :: The name of the work
#   Opus :: The number of the work
@app.route('/details')
def details():
    # Obtain the web info from the URL
    name = request.args.get('name')
    opus = request.args.get('opus')

    # Obtain the Database Info
    data = getWorkInfo(name, opus)

    # Rendder template with Information from the Database
    return render_template('details.html', title=name,
                            author=str(data[0][0]).replace(" ", "_"),
                            ttype=str(data[0][1]).replace(" ", "_"),
                            year=str(data[0][2]).replace(" ", "_"),
                            opus=str(data[0][3]).replace(" ", "_"),
                            videoURL=str(data[0][4]).replace(" ", "_"))

