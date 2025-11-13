import sys
from unittest.mock import patch

# This 'patch' tricks Streamlit into thinking it's not running
# from a command line, so it doesn't try to open a browser.
@patch('streamlit.util.get_local_ip', return_value='127.0.0.1')
def test_app_loads(mock_get_local_ip):
    """
    Test if the app.py file can be imported and runs.
    This is a basic 'smoke test'.
    """
    try:
        import app
        assert app is not None
    except Exception as e:
        assert False, f"App failed to load: {e}"

def test_model_variable():
    """
    Test if the 'model' variable in the app is loaded.
    """
    import app
    assert app.model is not None