from flask import *  
import cv2
import base64
import numpy as np
# from rembg import remove


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

            decodedInput = base64.b64decode(image_string)
            inputNpData = np.frombuffer(decodedInput, np.uint8)
            input = cv2.imdecode(inputNpData, cv2.IMREAD_UNCHANGED)
            # output = remove(input)
            output = input
            retval, buffer = cv2.imencode('.png', output)
            outputImage = base64.b64encode(buffer)
            return render_template("success.html", content = outputImage.decode('utf-8'))

if __name__ == '__main__':  
    app.run(host= '0.0.0.0', debug = True)  
    
