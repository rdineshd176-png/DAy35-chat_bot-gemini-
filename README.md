# Day 35 – Chatbot (Gemini 2.5 Flash) 🤖

This project is part of my **100 Days, 100 Python Projects** challenge.  

## 🎯 Goal  
Create an intelligent **AI Chatbot** using **Google’s Gemini 2.5 Flash** model through the official `google-genai` Python SDK.  
This chatbot can have real-time conversations and generate smart, human-like replies 💬  

---

## 💻 Features
- ⚡ Powered by **Gemini 2.5 Flash** – fast and context-aware.  
- 🔑 API key handled directly inside the script (for quick testing).  
- 💬 Continuous chat loop for easy interaction.  
- 🧠 Can be expanded into a voice assistant or GUI app later.

---

## 🧩 How It Works
1. The user enters a message.  
2. The chatbot sends it to Gemini API.  
3. The model generates a natural, AI-powered response.  
4. The chat continues until the user types `exit`.

---
⚙️ Installation
pip install -U google-genai

🚀 Run the Project

Replace "YOUR_API_KEY_HERE" with your actual Gemini API key.

Save the file as chatbot.py

Run the chatbot:

python chatbot.py

🧠 Key Learnings

Working with the Gemini SDK (google-genai)

Sending content to the Gemini model and reading its responses

Handling loops and user input in a chatbot

Understanding the basics of API integration in Python

## Example 
🤖 Gemini Chatbot – type 'exit' to quit

You: hi
Chatbot: Hello! How can I assist you today?
You: what is ai
Chatbot: **Artificial Intelligence (AI)** is a broad branch of computer science that aims to create machines that can perform tasks that typically require human intelligence.

In essence, AI tries to simulate human cognitive functions in machines. This includes things like:

*   **Learning:** Acquiring information and rules for using the information.
*   **Reasoning:** Using rules to reach approximate or definite conclusions.
*   **Problem-solving:** Figuring out how to achieve a goal.
*   **Perception:** Using sensory input (like vision or hearing) to understand the world.
*   **Language Understanding:** Comprehending and generating human language.

### Key Characteristics & Concepts:

1.  **Learning from Data:** Most modern AI, especially Machine Learning (ML) and Deep Learning (DL), learns patterns and rules directly from large datasets rather than being explicitly programmed for every possible scenario. This allows them to adapt and improve over time.

2.  **Algorithms:** AI systems are powered by complex algorithms – sets of rules and instructions that tell the computer how to process information, make decisions, and learn.

3.  **Autonomy:** AI systems can often operate with a degree of independence, making decisions or taking actions without constant human oversight (e.g., self-driving cars, automated trading systems).

4.  **Adaptability:** A good AI system can adjust its behavior based on new data or changing conditions.

### Types of AI:

It's helpful to categorize AI based on its capabilities:

1.  **Narrow AI (Weak AI):**
    *   This is the *only type of AI that exists today*.
    *   It's designed and trained for a **specific task** (e.g., playing chess, facial recognition, language translation, recommending products).
    *   It can perform its task very well, often better than humans, but it has no general intelligence or consciousness.  
    *   **Examples:** Siri, Google Assistant, recommendation engines (Netflix, Amazon), spam filters, self-driving car systems, medical diagnostic tools.

2.  **General AI (Strong AI or AGI - Artificial General Intelligence):**
    *   This is a **hypothetical type of AI** that would possess human-level cognitive abilities across a wide range of tasks, not just one.
    *   It would be able to understand, learn, and apply intelligence to any intellectual task that a human being can.     
    *   **Examples:** We don't have any yet, but think of characters like Data from Star Trek or C-3PO from Star Wars.     

3.  **Superintelligence:**
    *   Another **hypothetical type of AI** that would surpass human intelligence in virtually every field, including creativity, general wisdom, and problem-solving.
    *   **Examples:** Skynet from The Terminator, HAL 9000 from 2001: A Space Odyssey.

### Major Subfields of AI:

*   **Machine Learning (ML):** A core subset of AI where systems learn from data to identify patterns and make predictions 
or decisions without being explicitly programmed.
    *   **Deep Learning (DL):** A subset of ML that uses artificial neural networks with multiple layers (hence "deep") to 
learn complex patterns, especially effective for images, speech, and text.
*   **Natural Language Processing (NLP):** Enables computers to understand, interpret, and generate human language. (e.g., 
chatbots, language translation, sentiment analysis).
*   **Computer Vision (CV):** Allows computers to "see" and interpret visual information from the world (e.g., facial recognition, object detection, medical image analysis).
*   **Robotics:** Deals with the design, construction, operation, and use of robots. AI often provides the "brain" for intelligent robots.
*   **Expert Systems:** Older AI systems that use a knowledge base and inference engine to provide expert-level advice in a specific domain.
*   **Reinforcement Learning:** An ML paradigm where an agent learns to make decisions by performing actions in an environment and receiving rewards or penalties.

### Why is AI important?

AI is rapidly transforming industries and daily life by:

*   **Automating tasks:** Increasing efficiency and reducing human error.
*   **Providing insights:** Analyzing vast amounts of data to uncover patterns and make better predictions.
*   **Enhancing decision-making:** Supporting humans with intelligent recommendations.
*   **Enabling new capabilities:** Creating products and services that were previously impossible.

In summary, AI is about building intelligent machines that can perceive, reason, learn, and act, bringing us closer to a future where technology can augment and even replicate aspects of human thought.
You: exit
