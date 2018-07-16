# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify
from pictures_data import Pictures

# create Flask app
app = Flask(__name__)

# --- API Routes ---
@app.route('/api/pictures')
def api_pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def api_pics_by_id(id):
    return jsonify([item for item in Pictures if item['id']==id][0])

@app.route('/api/pictures/<country>')
def api_pics_by_country(country):
    return jsonify([item for item in Pictures if item['country'].lower() == country.lower()])

# --- HTML Routes ---
@app.route('/')
def index():
    return "Hello world"

@app.route('/pictures')
def pictures():
    return render_template('pictures_index.html', picture_list = Pictures)

@app.route('/pictures/<int:id>')
def pics_by_id(id):
    picture = [item for item in Pictures if item['id']==id][0]
    return render_template('picture_show.html', picture = picture)

@app.route('/pictures/<country>')
def pics_by_country(country):
    pictures = [item for item in Pictures if item['country'].lower() == country.lower()]
    return render_template('pictures_index.html', picture_list = pictures)

# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
