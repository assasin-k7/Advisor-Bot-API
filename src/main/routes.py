from flask import Blueprint, request, jsonify, Response
from .gpt_client import stream_gpt_response

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/advisor', methods=['POST'])
def advisor():
    user_input = request.json.get('query')
    
    if not user_input:
        return jsonify({"error": "Query is required"}), 400

    def generate():
        for chunk in stream_gpt_response(user_input):
            yield chunk
    
    return Response(generate(), content_type='text/event-stream')