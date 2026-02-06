

import os
import time
from groq import Groq
from gtts import gTTS

def format_response(answer):
    lines = answer.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # Replace bullet stars
        if line.startswith("*") or line.startswith("-"):
            line = "• " + line[1:].strip()

        # Remove bold markdown **
        line = line.replace("**", "")

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)

# ✅ Use environment variable (SECURE)
groq_client = Groq(api_key="YOUR_GROQ_API_KEY")


# ✅ Agriculture keywords
agri_keywords = [
    "crop", "farming", "fertilizer", "soil", "irrigation",
    "rain", "weather", "harvest", "seed", "agriculture",
    "farmer", "pesticide", "plant", "yield",
    "rice", "wheat", "maize", "cotton", "barley",
    "crop production", "farming state", "agriculture state"
]



def is_agriculture_question(question):
    question = question.lower()
    return any(word in question for word in agri_keywords)


def transcribe_audio(filepath):
    with open(filepath, "rb") as f:
        response = groq_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=f,
        )
    return response.text


def get_answer(question):

    # ✅ Filter non agriculture questions
    if not is_agriculture_question(question):
        return "I am designed to answer agriculture-related questions. Please ask about crops, fertilizers, irrigation, or farming."

    # ✅ Send valid questions to Groq
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful agriculture chatbot for Indian farmers."
             " Give short, simple, and practical answers."
              "Focus only on agriculture-related guidance."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content


def typing_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def text_to_speech(text, filename):
    tts = gTTS(text)
    output_path = f"{filename}.mp3"
    tts.save(output_path)
    return output_path


def main():

    mode = input("Choose input type ('text' or 'audio'): ").strip().lower()

    if mode == 'text':
        question = input("Enter your question: ").strip()

    elif mode == 'audio':
        filepath = input("Enter the path to your audio file: ").strip()

        if not os.path.exists(filepath):
            print("❌ File not found.")
            return

        print("🎤 Transcribing audio...")
        question = transcribe_audio(filepath)
        print(f"📝 Transcribed Text: {question}")

    else:
        print("❌ Invalid input type.")
        return

    print("🤖 Getting response from LLM...")
    answer = get_answer(question)

    print("\n✅ Answer:")
    typing_effect(answer)

    print("\n🔊 Converting answer to speech...")
    audio_file = text_to_speech(answer, "response_audio")
    print(f"🎧 Voice saved to: {audio_file}")


if __name__ == "__main__":
    main()
