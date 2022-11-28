from flask import Flask, render_template,redirect, url_for
app = Flask(__name__)

@app.route('/')
def main():
   dicts ={'Python': url_for('PY'),'LPI':url_for('LPI'),'Flask':url_for('Flaskre'),'Django': url_for('django'),'main':url_for('main') }
   print(dicts['main'])
   return render_template('main.html', ur=dicts)

@app.route('/LPI')
def LPI():
   return render_template('resourcelpi.html')

@app.route('/Python')
def PY():
   return render_template('resourcepy.html')

@app.route('/Flask')
def Flaskre():
   return render_template('resourceflask.html')

@app.route('/Django')
def django():
   return render_template('resourcedjango.html')

if __name__ == '__main__':
   app.run(debug=True)