import pytest
import pandas as pd
import numpy as np
from ml.data import process_data
from ml.model import compute_model_metrics
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_test_split():
    """
    # This is a test to check train-test split functionality
    """
    data = pd.DataFrame({
        'workclass': ['Private', 'Self-emp-not-inc', 'Local-gov'],
        'education': ['Bachelors', 'HS-grad', 'Masters'],
        'age': [25, 38, 28]
    })

    train = data.sample(frac=0.8, random_state=42)
    test = data.drop(train.index)

    assert len(train) == 2
    assert len(test) == 1
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)  

# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # This is a test to check compute_model_metrics functionality
    """
    y_true_value = np.array([1, 0, 1, 1, 0, 1])
    y_pred_value = np.array([1, 0, 0, 1, 0, 1]) 

    precision, recall, fbeta = compute_model_metrics(y_true_value, y_pred_value)

    assert precision == 1.0
    assert recall == 0.75
    assert round(fbeta, 4) == 0.8571



# TODO: implement the third test. Change the function name and input as needed
def test_process_data():
    """
    # This is a test to check process_data functionality
    """
    census_data = pd.DataFrame({
        'workclass': ['Private', 'Self-emp-not-inc', 'Local-gov'],
        'age': [25, 38, 28],
        'salary': ['<=50K', '>50K', '<=50K']
    }) 

    x, y, encoder, lb = process_data(
        census_data,
        categorical_features=['workclass'],
        label='salary',
        training=True)
    
    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert x.shape[0] == 3
    assert len(y) == 3
