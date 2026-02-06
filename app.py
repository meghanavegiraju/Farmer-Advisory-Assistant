
import os
import random
import string
from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
from gtts import gTTS
from groq import Groq

# ---------------- CONFIG ---------------- #
chat_history = []

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'webm', 'wav', 'mp3', 'm4a'}

# Load API key safely
groq_client = Groq(api_key="YOUR_GROQ_API_KEY")

# ---------------- UTIL FUNCTIONS ---------------- #

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def generate_filename():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def format_response(answer):
    """Clean bullet formatting"""
    lines = answer.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()

        if line.startswith("*") or line.startswith("-"):
            line = "• " + line[1:].strip()

        line = line.replace("**", "")

        cleaned.append(line)

    return "\n".join(cleaned)


# ---------------- AI FUNCTIONS ---------------- #

def transcribe_audio(filepath):
    try:
        with open(filepath, "rb") as f:
            response = groq_client.audio.transcriptions.create(
                model="whisper-large-v3-turbo",
                file=f,
            )
        return response.text
    except Exception as e:
        return "Error in transcription."


# def get_answer(question):
#     try:
#         response = groq_client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             max_tokens=200,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "You are a farmer advisory assistant. "
#                         "Give very short and simple answers suitable for farmers. "
#                         "Use maximum 4 bullet points. "
#                         "Avoid technical jargon. "
#                         "Give practical farming tips only."
#                     )
#                 },
#                 {"role": "user", "content": question}
#             ]
#         )

#         answer = response.choices[0].message.content
#         return format_response(answer)

#     except Exception:
#         return "Sorry, I couldn't process your request."
def get_answer(question):

    global chat_history

    try:
        # Add user question to history
        chat_history.append({
            "role": "user",
            "content": question
        })

        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=200,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a farmer advisory assistant. "
                        "Give very short and simple answers suitable for farmers. "
                        "Use maximum 4 bullet points. "
                        "Avoid technical jargon. "
                        "Give practical farming tips only."
                    )
                }
            ] + chat_history
        )

        answer = response.choices[0].message.content

        # Store assistant response
        chat_history.append({
            "role": "assistant",
            "content": answer
        })

        # OPTIONAL: Limit memory size (prevents overload)
        if len(chat_history) > 10:
            chat_history.pop(0)

        return format_response(answer)

    except Exception:
        return "Sorry, I couldn't process your request."


def text_to_audio(text, filename):
    try:
        audio_path = os.path.join("static/audio", f"{filename}.mp3")
        gTTS(text).save(audio_path)
        return audio_path
    except Exception:
        return None


# ---------------- ROUTES ---------------- #

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():

    # ---------- AUDIO INPUT ----------
    if 'audio' in request.files:

        audio = request.files['audio']

        if audio and allowed_file(audio.filename):

            filename = secure_filename(generate_filename() + ".webm")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            audio.save(filepath)

            transcription = transcribe_audio(filepath)
            answer = get_answer(transcription)

            voice_filename = generate_filename()
            text_to_audio(answer, voice_filename)

            return jsonify({
                'text': f"🎤 Transcribed: {transcription}\n\n🤖 Answer:\n{answer}",
                'voice': url_for('static', filename=f'audio/{voice_filename}.mp3')
            })

    # ---------- TEXT INPUT ----------
    elif 'text' in request.form:

        question = request.form['text']
        answer = get_answer(question)

        voice_filename = generate_filename()
        text_to_audio(answer, voice_filename)

        return jsonify({
            'text': answer,
            'voice': url_for('static', filename=f'audio/{voice_filename}.mp3')
        })

    return jsonify({'text': 'Invalid input.'}), 400


# ---------------- START SERVER ---------------- #

if __name__ == '__main__':

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static/audio", exist_ok=True)

    app.run(debug=True)
