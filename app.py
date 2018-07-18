from flask import Flask, render_template, jsonify

#import Pictures
from pictures_data import Pictures


# create Flask app
app = Flask(__name__)




# @app.route('/hello')
# def hello():
#     return HELLLLOOOOO

# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)


@app.route('/api/pictures/<int:id>')
def picture_id(id):
    for pic in Pictures:
        if id == pic["id"] :
            return jsonify(pic)



@app.route('/api/pictures/<country>')
def picture_country(country):
    return jsonify([pic for pic in Pictures if pic['country'].lower() == country])




# --- HTML Routes ---
@app.route('/pictures')
def pictures_html():
    pictures = Pictures
    return render_template('pictures_index.html', pictures=pictures)
    #'picture_show.html', city=city, country= country, id =id)

@app.route('/pictures/<int:id>')
def picture_id_html(id):
    for pic in Pictures:
        if id == pic["id"]:
            return render_template('picture_show.html', picture=pic)

@app.route('/pictures/<country>')
def picture_country_html(country):
    temp = [pic for pic in Pictures if pic['country'].lower() == country]
    return render_template('pictures_index.html', pictures=temp)


# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
