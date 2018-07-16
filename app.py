from flask import Flask, render_template, jsonify

from pictures_data import Pictures


# create Flask app
app = Flask(__name__)

@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route("/api/pictures/<int:id>")
def pic_by_id(id):
    return jsonify([pic for pic in Pictures if pic['id'] == id][0])

# import pdb; pdb.set_trace()
@app.route("/api/pictures/<country>")
def pic_by_country(country):
    return jsonify([pic for pic in Pictures if pic['country'] == country])

@app.route('/pictures')
def pictures_html():
    return render_template('pictures_index.html', pictures = Pictures)

@app.route('/pictures/<int:id>')
def pic_by_id_html(id):
    onepic = [pic for pic in Pictures if pic['id'] == id][0]
    return render_template('picture_show.html', picture = onepic)

@app.route('/pictures/<country>')
def pic_by_country_html(country):
    country_pic = [pic for pic in Pictures if pic['country'] == country]
    return render_template('pictures_index.html', pictures= country_pic)

# @app.route("/pictures/<int:id>")
# def pic_by_id_html(id):
#     return jsonify([pic for pic in Pictures if pic['id'] == id][0])
#
# # import pdb; pdb.set_trace()
# @app.route("/pictures/<country>")
# def pic_by_country_html(country):
#     return jsonify([pic for pic in Pictures if pic['country'] == country])






# --- API Routes ---




# --- HTML Routes ---





# run our Flask app
if __name__ == '__main__':
    app.run(debug = True)
