from flask import Flask, jsonify, request, render_template
from models.Post import Post
from services.PostService import PostService
import os, json
from dotenv import load_dotenv

app = Flask(__name__)

post_service = PostService()

load_dotenv()
try:
    AVAILABLE_MODELS = json.loads(os.getenv('AVAILABLE_MODELS', '[]'))
except (json.JSONDecodeError, TypeError):
    AVAILABLE_MODELS = []

@app.route('/generator')
def article_generator():
    return render_template('index.html', 
                         title='AI Article Generator',
                         heading='AI Article Generator',
                         message='Welcome to AI Article Generator! Generate compelling articles on any topic using advanced AI models.',
                         available_models=AVAILABLE_MODELS)

@app.route('/create', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        model = data.get('model')
        topic = data.get('topic')
        
        if not model or not topic:
            return jsonify({'error': 'Both model and topic are required'}), 400
            
        post = Post(model, topic)
        result = post_service.create_post(post)
        
        return jsonify({
            'status': 'success', 
            'message': 'Post created successfully',
            'post': {
                'model': post.model,
                'topic': post.topic,
                'response': result
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500     

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)