

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
groq_client = Groq(api_key="")

agri_keywords = [
    "agriculture", "farmer", "farming",
    "crop", "crops", "cultivation",
    "soil", "fertilizer", "manure",
    "irrigation", "rain", "weather",
    "harvest", "yield", "seed", "seeds",
    "pesticide", "plant", "plants"
]


def is_agriculture_question(question):
    question = question.lower()
    return any(word in question for word in agri_keywords)


# ------------------ AUDIO TO TEXT ------------------
def transcribe_audio(filepath):
    with open(filepath, "rb") as f:
        response = groq_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=f,
        )
    return response.text


# ------------------ GET ANSWER ------------------
def get_answer(question):

    # 🚫 STRICT BLOCK for non-agriculture
    if not is_agriculture_question(question):
        return (
            "I am a farmer advisory assistant. "
            "I can answer only agriculture-related questions such as "
            "crops, soil, irrigation, and farming practices."
        )

    # ✅ ONLY agriculture questions reach the LLM
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        max_tokens=150,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a farmer advisory assistant. "
                    "Answer ONLY agriculture-related questions. "
                    "Give short, simple, practical answers. "
                    "Do NOT answer any other topics."
                )
            },
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content


# ------------------ TYPING EFFECT ------------------
def typing_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# ------------------ TEXT TO SPEECH ------------------
def text_to_speech(text, filename):
    tts = gTTS(text)
    output_path = f"{filename}.mp3"
    tts.save(output_path)
    return output_path


# ------------------ MAIN FUNCTION ------------------
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