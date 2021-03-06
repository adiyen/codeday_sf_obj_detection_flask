from flask import Flask, render_template, request
from werkzeug import secure_filename
# from object_detection import storage
from facial_detection import test
app = Flask(__name__)


upload_complete = False

def object_finder():
    test()
    
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    fname = ''
    if request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        f.save("static/pics/" + fname)
        object_finder()
    return render_template('upload.html', image=fname)

		
if __name__ == '__main__':
   app.run(debug = True)
