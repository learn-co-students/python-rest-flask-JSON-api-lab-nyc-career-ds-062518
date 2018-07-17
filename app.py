from flask import Flask, render_template, jsonify
from pictures_data import Pictures

# create Flask app
app = Flask(__name__)

# --- API Routes ---

@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def picture(id):
    for jdata in Pictures:
        if jdata['id'] == id:
            return jsonify(jdata)

@app.route('/api/pictures/<country>')
def country(country):
    #return [jsonify(jdata) for jdata in Pictures if jdata['country'].upper() == country.upper()]
    lst = []
    for jdata in Pictures:
         if jdata['country'].upper() == country.upper():
             lst.append(jdata)
    return jsonify(lst)
    #         lst.append(jsonify(jdata))
    # return lst

# --- HTML Routes ---
@app.route('/pictures')
def show_pictures():
    return render_template('/pictures_index.html', pictures = Pictures)

@app.route('/pictures/<int:id>')
def show_picture_id(id):
    ids = [picture for picture in Pictures if picture['id'] == id]
    return render_template('/picture_show.html', picture = ids[0])

@app.route('/pictures/<country>')
def show_picture_country(country):
    countries = [picture for picture in Pictures if picture['country'].upper() == country.upper()]
    return render_template('/pictures_index.html', pictures = countries)
    #import pdb; pdb.set_trace()
# run our Flask app
if __name__ == '__main__':
    app.run(debug = True)
