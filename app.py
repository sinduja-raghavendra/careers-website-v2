from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
