from flask import Flask, jsonify, request
from models import YourModel  # Import your models here
from recommender import recommend_fashion  # Import your recommender function here

app = Flask(__name__)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    # Assuming data contains user preferences
    recommendations = recommend_fashion(data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)