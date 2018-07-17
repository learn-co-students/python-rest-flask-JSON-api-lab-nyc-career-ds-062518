# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify

# import Pictures
from pictures_data import Pictures

# create Flask app
app = Flask(__name__)

# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def picture (id):
    for pic in Pictures:
        if id == pic["id"]:
            return jsonify(pic)

@app.route('/api/pictures/<country>')
def country(country):
    return jsonify([pic for pic in Pictures if pic["country"].lower()==country.lower()])

# --- HTML Routes ---

@app.route('/pictures')
def return_pics():
    return render_template("pictures_index.html", pictures = [Pictures[0],Pictures[1], Pictures[2],Pictures[3],Pictures[4]])

@app.route('/pictures/<int:id>')
def return_pic(id):
    for picture in Pictures:
        if id==picture["id"]:
            return render_template("picture_show.html", picture = picture)

@app.route('/pictures/<country>')
def return_country(country):
    pictures_list = []
    for picture in Pictures:
        if picture["country"].lower()==country.lower():
            pictures_list.append(picture)
    return render_template("pictures_index.html", pictures = pictures_list)

# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
