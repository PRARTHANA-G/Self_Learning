import sys


def test_model_variable():
    """
    Test if the 'model' variable in the app is loaded.
    """
    import app
    assert app.model is not None