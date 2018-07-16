# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify
from pictures_data import Pictures
# import Pictures


# create Flask app
app = Flask(__name__)






# --- API Routes ---

@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def pictures_by_id(id):
    return jsonify([picture for picture in Pictures if picture['id'] == id][0])

@app.route('/api/pictures/<country>')
def pictures_by_country(country):
    return jsonify([picture for picture in Pictures if picture['country'].lower() == country.lower()])


# --- HTML Routes ---
@app.route('/pictures')
def pictures_show():
    return render_template('pictures_index.html',pictures = Pictures)

@app.route('/pictures/<int:id>')
def pictures_id_show(id):
    # for pic in Pictures:
    #     if pic['id'] == id:
    #         return render_template('picture_show.html', picture=pic)
    x = [picture for picture in Pictures if picture['id'] == id]
    return render_template('pictures_index.html', pictures = x,id = id)

@app.route('/pictures/<country>')
def pictures_by_country_show(country):
    x = [picture for picture in Pictures if picture['country'].lower() == country]
    return render_template('pictures_index.html',pictures = x)






# run our Flask app
if __name__ == '__main__':
    app.run(debug = True)
