import sys
import os

print("Current directory:", os.getcwd())
print("App directory:", os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
