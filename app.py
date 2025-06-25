from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/datos')
def datos_json():
    return jsonify({"nombre" : "Mario", "edad": 30})

if __name__ == '__main__':
    app.run(debug = True)
