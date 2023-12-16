from flask import Flask, request, render_template
import json
from flask_cors import CORS
import recommend  # Assuming recommend module is in the same directory as your Flask app

app = Flask(__name__)
CORS(app)

@app.route('/')
def music_recommender():
    return render_template('index.html')

@app.route('/artist', methods=['GET'])
def recommend_artists():
    artist_title = request.args.get('title')
    
    if artist_title:
        res = recommend.recommend(artist_title)
        return render_template("tempx.html", res=json.dumps(res))
    else:
        return "Error: Please provide an artist title."

if __name__ == '__main__':
    app.run(port=5000, debug=True)
