
🌾 **Farmer Advisory Assistant**
*AI-Powered Conversational Chatbot for Farmers*

**Project Overview**

The Farmer Advisory Assistant is an AI-powered conversational chatbot designed to provide reliable and practical agriculture-related guidance to farmers. The chatbot supports both text and voice-based interaction, allowing users to ask questions conveniently. It is capable of handling follow-up questions by maintaining conversation context and responds politely to queries that are not related to agriculture. The primary goal of this project is to improve accessibility and deliver simple, useful farming advice.

**Key Features**

* Text-based question answering
* Voice-based interaction using speech recognition
* Context-aware follow-up question handling
* Agriculture-specific responses only
* Polite handling of unknown or unrelated queries
* Text-to-speech audio responses
* Simple and user-friendly web interface


**Conversation Flow**

User
↓
Text / Voice Input
↓
Speech-to-Text (for voice queries)
↓
Conversation Context Handling
↓
Agriculture Domain Validation
↓
LLM Processing (Groq LLaMA)
↓
Response Generation
↓
Text-to-Speech Conversion
↓
Text + Audio Response
↓
Follow-up Question Support

**Sample Dialogues**

**Example 1 – Basic Query**
User: How to grow sugarcane?
Bot:

* Use fertile and well-drained soil
* Plant during the monsoon season
* Water regularly
* Apply recommended fertilizers

**Example 2 – Follow-Up Question**
User: How much water does it need?
Bot:

* Irrigate every 7 to 10 days
* Avoid waterlogging
* Increase watering during summer

**Example 3 – Unknown Query**
User: Who is the Prime Minister of India?
Bot:
I am designed to answer agriculture-related questions. Please ask about crops, irrigation, or farming.

---

**Tech Stack Explanation**

Frontend technologies include HTML for structure, Tailwind CSS for styling, and JavaScript for handling user interactions and API calls. The backend is built using Python and Flask, which manages API requests and response handling.

For AI and voice processing, the project uses the Groq LLaMA model for generating intelligent responses, Groq Whisper for converting speech to text, and Google Text-to-Speech (gTTS) for converting text responses into audio output.

For security, API keys are managed using environment variables and are excluded from version control using a .gitignore file.

**Demo Video / Screenshots**

A demo video demonstrating text input, voice interaction, follow-up question handling, and audio responses is included or linked as part of the submission. Screenshots may also be provided for reference.


