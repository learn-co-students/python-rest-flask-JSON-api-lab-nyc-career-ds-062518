from flask import Flask, render_template, jsonify
import pdb
from pictures_data import Pictures


# create Flask app
app=Flask(__name__)




# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def picture_id(id):
    return jsonify(Pictures[id-1])

@app.route('/api/pictures/<country>')
def picture_country(country):

    return jsonify([pic for pic in Pictures if pic['country'].lower() == country.lower()])



# --- HTML Routes ---

@app.route('/pictures')
def html_pictures():
    pictures = Pictures
    return render_template('pictures_index.html', pictures=Pictures)

@app.route('/pictures/<int:id>')
def html_picture_id(id):
    pictures = Pictures
    for picture in pictures:
        if picture['id'] == id:
            return render_template('picture_show.html', picture=picture, id=id )

@app.route('/pictures/<country>')
def html_pictures_country(country):
    pictures = [picture for picture in Pictures if picture['country'].lower() == country.lower()]
    return render_template('pictures_index.html', pictures=pictures, country=country )




# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
