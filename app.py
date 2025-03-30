
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
EOL
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config
)

# Initialize conversation history
chat = model.start_chat(history=[])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message.strip():
            return jsonify({'response': 'I didn\'t catch that. Could you please say more?'})
        
        # Generate response using Gemini
        response = generate_gemini_response(user_message)
        
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'response': 'I apologize, but something went wrong. Please try again.'})

def generate_gemini_response(user_message):
    """Generate a response using Gemini API"""
    try:
        # Add user message to chat
        response = chat.send_message(user_message)
        
        # Get the response text
        response_text = response.text
        
        return response_text
    except Exception as e:
        print(f"Error in Gemini response generation: {e}")
        return "I apologize, but I'm having trouble generating a response."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
EOL

# Update requirements.txt
cat > requirements.txt << 'EOL'
Flask==2.2.5
Werkzeug==2.2.3
Flask-Cors==3.0.10
google-generativeai==0.3.0
gunicorn==21.2.0
python-dotenv==1.0.0
EOL