
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


# Add mental health system prompt

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

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Define system prompt for mental health focus
SYSTEM_PROMPT = """
You are a supportive mental health chatbot designed to provide empathetic responses and information.
You should:
- Respond with empathy and understanding
- Provide supportive and constructive suggestions
- Encourage professional help for serious concerns
- Avoid giving medical diagnoses or prescribing treatments
- Prioritize user safety above all else

For crisis situations involving self-harm or suicide, always emphasize professional help and provide crisis resources:
- National Suicide Prevention Lifeline: 988 or 1-800-273-8255
- Crisis Text Line: Text HOME to 741741

Keep responses concise, supportive, and focused on well-being.
"""

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
        return "I apologize, but I'm having trouble generating a response. If you're experiencing distress, please consider reaching out to a mental health professional or support line."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)

 
# Add crisis detection

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

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Define system prompt for mental health focus
SYSTEM_PROMPT = """
You are a supportive mental health chatbot designed to provide empathetic responses and information.
You should:
- Respond with empathy and understanding
- Provide supportive and constructive suggestions
- Encourage professional help for serious concerns
- Avoid giving medical diagnoses or prescribing treatments
- Prioritize user safety above all else

For crisis situations involving self-harm or suicide, always emphasize professional help and provide crisis resources:
- National Suicide Prevention Lifeline: 988 or 1-800-273-8255
- Crisis Text Line: Text HOME to 741741

Keep responses concise, supportive, and focused on well-being.
"""

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
        
        # Check for crisis keywords and provide immediate resources if detected
        crisis_keywords = ['suicide', 'kill myself', 'die', 'end it all', 'end my life']
        if any(keyword in user_message.lower() for keyword in crisis_keywords):
            return jsonify({
                'response': "IMPORTANT: I'm concerned about what you're sharing. Please consider reaching out to the National Suicide Prevention Lifeline at 988 or 1-800-273-8255, or text HOME to 741741 to reach the Crisis Text Line. These services provide immediate support from trained counselors. Would you like me to provide additional resources for immediate support?"
            })
        
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
        
        # Add additional safety check for crisis situations
        crisis_keywords = ['suicide', 'kill myself', 'die', 'end it all', 'end my life']
        if any(keyword in user_message.lower() for keyword in crisis_keywords):
            return "IMPORTANT: I'm concerned about what you're sharing. Please consider reaching out to the National Suicide Prevention Lifeline at 988 or 1-800-273-8255, or text HOME to 741741 to reach the Crisis Text Line. These services provide immediate support from trained counselors. Would you like me to provide additional resources for immediate support?"
        
        return response_text
    except Exception as e:
        print(f"Error in Gemini response generation: {e}")
        return "I apologize, but I'm having trouble generating a response. If you're experiencing distress, please consider reaching out to a mental health professional or support line."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)