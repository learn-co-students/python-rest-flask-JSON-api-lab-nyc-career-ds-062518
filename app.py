from flask import Flask, render_template, jsonify
from pictures_data import Pictures

app = Flask(__name__)


# --- API Routes ---

@app.route('/api/pictures')
def api_pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def api_pics_by_id(id):
    return jsonify([item for item in Pictures if id == item['id']][0])

@app.route("/api/pictures/<country>")
def api_pics_by_country(country):
    return jsonify([item for item in Pictures if country.lower() == item['country'].lower()])

# --- HTML Routes ---

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/pictures')
def pictures():
    return render_template('pictures_index.html', picture_list = Pictures)

@app.route('/pictures/<int:id>')
def pics_by_id(id):
    picture = [item for item in Pictures if id == item['id']][0]
    return render_template('picture_show.html', picture = picture)

@app.route("/pictures/<country>")
def pics_by_country(country):
    picture_list = [item for item in Pictures if country.lower() == item['country'].lower()]
    return render_template('pictures_index.html', picture_list = picture_list)


if __name__ == '__main__':
    app.run(debug=True)
