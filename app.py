from flask import Flask, render_template, jsonify
from pictures_data import Pictures

app = Flask(__name__)

@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def by_id(id):
    return jsonify([pic for pic in Pictures if pic['id'] == id][0])

@app.route('/api/pictures/<country>')
def by_country(country):
    return jsonify([pic for pic in Pictures if pic['country'].lower() == country])

@app.route('/pictures')
def non_api_pictures():
    return render_template('pictures_index.html', pictures = Pictures)

@app.route('/pictures/<int:id>')
def non_api_by_id(id):
    onepic = [pic for pic in Pictures if pic['id'] == id][0]
    return render_template('picture_show.html', picture = onepic)

@app.route('/pictures/<country>')
def non_api_by_country(country):
    photos = [pic for pic in Pictures if pic['country'].lower() == country]
    return render_template('pictures_index.html', pictures = photos)

if __name__ == '__main__':
    app.run(debug=True)
