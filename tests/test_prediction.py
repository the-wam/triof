import pytest

from src.iaAzure import predictionAzure



def test_predictionAzure():

    out = predictionAzure("/static/images/camera/couvert-plastique.jpg")


    assert type(out) == str
    assert "couvert" == out