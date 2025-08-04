from flask import Flask, request, jsonify
from flask_cors import CORS
from service import Service
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)

# 配置 CORS
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8081"}})  # 替换为你的前端地址

service = Service()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    history = data.get('history', [])
    
    response = service.answer(message, history)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=8080)
