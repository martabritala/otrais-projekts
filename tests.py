pyton -m pip install flask
        Flask
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Sveiki!"

    if __name__ =='__main__':
            @app.run(port = 5000)
            
print("Sveiki!")