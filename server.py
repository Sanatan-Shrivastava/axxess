from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request object
    file = request.files['file']

    # Get the filename from the form field named 'filename'
    filename = request.form.get('filename')

    # Save the file to the 'input' folder with the dynamic filename
    file.save(os.path.join('input', filename))

    # Return a response to the client
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run()
