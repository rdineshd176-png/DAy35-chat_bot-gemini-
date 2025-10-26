from google import genai

# Initialize the Gemini client with your API key
client = genai.Client(api_key="YOUR_API_KEY_HERE")

print("🤖 Gemini Chatbot – type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    try:
        # Send the user message to the Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        # Print Gemini's reply
        print("Chatbot:", response.text)

    except Exception as e:
        print("Chatbot: ⚠️ Something went wrong:", e)
