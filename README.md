# FLASK scaffold

Run with uWSGI:
*   Install virtual environment and libraries: 
    *   python -m venv .
    *   source bin/activate
    *   pip install -r requirements.txt
*   uwsgi --module src.__main__:app --http :5000  --buffer-size 32768 --post-buffering 1