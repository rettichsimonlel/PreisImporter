import pytest
from main import import_data, visualize_data

def test_dummy():
    assert True

def test_data():
    assert import_data('data.txt')[0][0] == "Lenzing"
    assert import_data('data.txt')[0][1] == 170447112
    assert import_data('data.txt')[0][2] == 34.75

    assert import_data('data.txt')[1][0] == "Andritz"
    assert import_data('data.txt')[1][1] == 170447131
    assert import_data('data.txt')[1][2] == 59.41

def test_visualize():
    data = import_data('data.txt')
    assert visualize_data(data) == True
