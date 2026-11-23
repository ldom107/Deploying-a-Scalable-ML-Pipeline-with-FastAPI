import pytest
# TODO: add necessary import

import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import (
    train_model, 
    inference,
    compute_model_metrics
)

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # add description for the first test
    Test that train_model returns a Random Forest Classifier.
    """
    X_train = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])

    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)

# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    # add description for the second test
    Test that inference returns predictions as a NumPy array.
    """
    
    X_train = np.array([
        [1, 2], 
        [2, 3], 
        [3, 4], 
        [4, 5]
    ])

    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    predictions = inference(model, X_train)

    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == len(X_train)

# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # add description for the third test
    Test that compute_model_metrics returns the expected values.
    """
    
    y = np.array([1, 1, 0, 0])
    preds = np.array([1, 0, 1, 0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == 0.5
    assert recall == 0.5
    assert fbeta == 0.5