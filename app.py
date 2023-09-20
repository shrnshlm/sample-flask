from flask import *  
import base64

app = Flask(__name__)

@app.route('/')  
def upload():  
    return render_template("index.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        if f.filename != '':
            image_string = base64.b64encode(f.read())
            return render_template("success.html", content = image_string.decode('utf-8'))

if __name__ == '__main__':  
    app.run(host= '0.0.0.0', debug = True)  
    
