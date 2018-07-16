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
def picture(id):
    return jsonify([jdata for jdata in Pictures if jdata['id'] == id][0])

@app.route('/api/pictures/<country>')
def picture_country(country):
    return jsonify([jdata for jdata in Pictures if jdata['country'].upper() == country.upper()])


# --- HTML Routes ---
@app.route('/pictures')
def picture_html():
    return render_template('/pictures_index.html', pictures = Pictures)

@app.route('/pictures/<int:id>')
def picture_html_id(id):
    id_list = [jdata for jdata in Pictures if jdata['id'] == id]
    return render_template('/picture_show.html', picture = id_list[0])

@app.route('/pictures/<country>')
def picture_html_country(country):
    country_list = [jdata for jdata in Pictures if jdata['country'].upper() == country.upper()]
    return render_template('/pictures_index.html', pictures = country_list)

# run our Flask app
if __name__ == '__main__':
    app.run(debug = True)
