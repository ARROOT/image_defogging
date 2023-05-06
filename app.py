from flask import Flask, request, render_template #jsonify
#import cv2
#import numpy as np
#import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #if request.method == 'POST':
        # Get the image data from the request
        #img_data = request.files.get('image').read()

        # Convert the image data to a numpy array
        #img_np = np.frombuffer(img_data, np.uint8)

        # Read the image using OpenCV
        #img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

        # Do some processing on the image (e.g. resize it)
        #img_resized = cv2.resize(img, (400, 400))

        # Save the processed image to a file
        #cv2.imwrite('static/processed_image.jpg', img_resized)

        # Return a response to the client
        #return jsonify({'message': 'Image processed successfully'})

    # Render the HTML template
    return render_template('index.html')

#if __name__ == '__main__':
app.run(debug=True)
