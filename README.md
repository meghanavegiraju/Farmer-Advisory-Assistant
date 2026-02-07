
🌾 **Farmer Advisory Assistant**
*AI-Powered Conversational Chatbot for Farmers*

**Project Overview**

The Farmer Advisory Assistant is an AI-powered conversational chatbot designed to provide reliable and practical agriculture-related guidance to farmers. The chatbot supports both text and voice-based interaction, allowing users to ask questions conveniently. It is capable of handling follow-up questions by maintaining conversation context and responds politely to queries that are not related to agriculture. The primary goal of this project is to improve accessibility and deliver simple, useful farming advice.



**Demo Video**
https://drive.google.com/file/d/1D-YlGwue4foSNCqPqrH_lr1S0njkf_0o/view?usp=sharing

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


**Dialogue 1 – Agriculture Query**

**User:** How to grow sugarcane?

**Bot:**
Here are 4 steps to grow sugarcane:
 • Planting: Plant sugarcane cuttings in a well-prepared soil bed, typically in the rainy season. 
• Irrigation: Provide adequate water supply, especially during the germination and vegetative growth stages. 
• Fertilization: Apply fertilizers to promote healthy growth and maximize yield. 
• Harvesting: Harvest sugarcane stalks when they reach maturity, typically between 10-12 months after planting.



**Dialogue 2 – Follow-Up Question**

**User:** How much water does it need?

**Bot:**
Here are 4 key facts about water requirements for sugarcane:
 • Average of 2,000-3,000 mm: Sugarcane needs an average of 2,000-3,000 mm of water per year.
 • High water requirements: Sugarcane requires high amounts of water, especially during the vegetative growth stage.
 • Watering needs to be consistent: Consistent watering is necessary to promote healthy growth and maximize yield.
 • Water storage is crucial: Adequate water storage is crucial to support sugarcane cultivation, particularly during dry periods.

 
**Dialogue 3 – Voice Interaction**

**User (Voice):** Which states grow rice in India?

**Bot:**
•	West Bengal
•	Punjab
•	Andhra Pradesh
•	Uttar Pradesh


**Dialogue 4 – Unknown / Unrelated Query**

**User:** Which sport requires the most endurance?

**Bot:**
I'm a farming advisory Assistant, I don't have information about sports

**Tech Stack Explanation**

Frontend technologies include HTML for structure, Tailwind CSS for styling, and JavaScript for handling user interactions and API calls. The backend is built using Python and Flask, which manages API requests and response handling.

For AI and voice processing, the project uses the Groq LLaMA model for generating intelligent responses, Groq Whisper for converting speech to text, and Google Text-to-Speech (gTTS) for converting text responses into audio output.






