import os
import sys
import requests


def predictionAzure(image_path):
    """
        Function take a image path, and predicte is
    """

    # Add your Computer Vision subscription key and endpoint to your environment variables.
    #subscription_key = "3d596922873d4946a09cd7d28e74a3d8"
    # 'Ocp-Apim-Subscription-Key': subscription_key,
    
    endpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/69040bc7-d032-4457-8f64-33645d53e089/classify/iterations/Iteration1/image"


    # Set image_path to the local path of an image that you want to analyze.
    # Sample images are here, if needed:
    # https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images
    # image_path = "C:/Users/lbanco/datamoi/cours/app-ia/triof/camera/couvert-plastique-turquoise-v1-z.jpg"

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers = {
            'Content-Type': 'application/octet-stream',
            'Prediction-Key': 'a7771707633a4f6c8854c89f853cd62a'}

    #params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(endpoint, headers=headers, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()


    return cleenResult(analysis)


def cleenResult(analysis):

    predic = analysis["predictions"]

    score = [x['probability'] for x in predic]

    index = score.index(max(score))

    best_result = predic[index]["tagName"]

    return best_result


def variablesToDisplay(prediction):

    whithDisplay = {
        "bouteille":"",
        "gobelet":"",
        "couvert":""
    }

    if prediction == "bouteille":
        whithDisplay["bouteille"] = True
    elif prediction == "gobelet":
        whithDisplay["gobelet"] = True
    elif prediction == "couvert":
        whithDisplay["couvert"] = True
    else:
        pass

    return whithDisplay