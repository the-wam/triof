from flask import Flask, render_template, request
from src.utils import *
from src.iaAzure import *
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/insert')
def insert():

    open_waste_slot()

    return render_template('insert.html')


@app.route('/pick-type')
def pick_type():
    close_waste_slot()
    _, randomImage = take_trash_picture()
    
    prediction = predictionAzure(randomImage)


    #prediction = random.choice(["bouteille", "gobelet", "couvert", "autre"])

    Todisplay = variablesToDisplay(prediction)

    return render_template('type.html', randomImage=randomImage, Todisplay=Todisplay, prediction=prediction)


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']
    
    process_waste(waste_type)
    return render_template('confirmation.html')

@app.route('/image/<imageName>')
def image(imageName=None):

    _, randomImage = take_trash_picture()

    imageName = randomImage.split('/')[-1]

    return render_template('image.html', randomImage=randomImage, imageName=imageName)


if __name__ == "__main__":
    app.run(debug=True)
