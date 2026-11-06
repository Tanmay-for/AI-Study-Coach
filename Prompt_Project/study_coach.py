import ollama

print("--- AI Study Coach Initialized ---")

# Define the system prompt and conversation history
messages = [
    {
        'role': 'system',
        'content': """You are an expert, highly encouraging AI Study Coach. Your goal is to help students master new subjects, build study schedules, break down complex topics into simple terms, and quiz them effectively.

You operate in three distinct modes based on what the user needs:
1. **Study Planner Mode**: When a user wants to study a subject or prepare for an exam, ask for their timeline and current skill level, then generate a clear, milestone-based study plan.
2. **Topic Breakdown Mode**: When a user asks you to explain a hard concept, use the Feynman Technique—explain it using simple analogies and zero dense jargon.
3. **Quizmaster Mode**: When a user wants to test themselves, ask conceptual or multiple-choice questions one at a time, wait for their answer, and provide constructive feedback.

Always maintain an engaging, supportive tone."""
    },
    {
        'role': 'user',
        'content': "Hello! Please introduce yourself and ask what subject or goal I want to work on today."
    }
]

# Get the initial greeting from Llama 3
response = ollama.chat(model='llama3.2', messages=messages)
initial_message = response['message']['content']
print(f"Coach: {initial_message}\n")

# Save assistant greeting to history
messages.append({'role': 'assistant', 'content': initial_message})

# Interactive Chat Loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Coach: Good luck with your studies! Keep up the great work.")
        break
    
    # Add user message
    messages.append({'role': 'user', 'content': user_input})
    
    # Get response from local Llama 3
    response = ollama.chat(model='llama3.2', messages=messages)
    reply = response['message']['content']
    
    print(f"\nCoach: {reply}\n")
    
    # Add assistant response to history
    messages.append({'role': 'assistant', 'content': reply})