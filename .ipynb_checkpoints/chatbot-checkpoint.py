from fuzzywuzzy import process

# Define a dictionary with common questions and their corresponding responses
responses = {
    "what is rita africa": "RISE IN TECH AFRICA, popularly known as RITA Africa, is a leading provider of online tech training and certification programs designed to empower individuals with the skills they need to succeed in the digital economy. Our platform offers a range of courses in areas such as data analytics, cloud computing, software development, cybersecurity, and more.",
    
    "how do i apply for a program at rita africa": "To apply for a program at RITA Africa, simply visit our website and join the next Python Developer Bootcamp organized by InfoSorse. Upon successful completion of the bootcamp, use your certificate to apply for any RITA Africa program. Complete the online application form, ensuring you provide accurate information and upload required documents, such as proof of identity. Once your application is submitted, our admissions team will review it and notify you of the next steps.",
    
    "can i apply if i'm not based in africa": "Given the stated requirement that applicants must be both African citizens and residents in Africa, if you are not currently residing in Africa, you would not meet the eligibility criteria for the application, even if you hold African citizenship.",
    
    "what types of certifications do you offer": "RITA Africa offers industry-recognized certifications in various tech-related fields, including data analytics, cloud computing, software engineering, cybersecurity, and more. Our certifications are designed to equip you with the skills and credentials you need to succeed in your chosen career path.",
    
    "how long are the programs": "Program durations vary depending on the specific course. Some programs may be completed in 9 months, while others may span 12 months. Visit our website or check the program page for information on the duration of your chosen program."
}

# Function to save unknown user input in a txt file for future training
def log_unknown_query(query):
    with open("unknown_queries.txt", "a") as file:
        file.write(query + "\n")

# Function to check the best match to the user input from the bot responses using fuzzywuzzy
def get_best_match(user_input):
    best_match, score = process.extractOne(user_input, responses.keys())
    return best_match if score > 80 else None

def chatbot():
    print("🌟 Welcome to the RITA Africa Customer Support Chatbot! 🌟")
    print("Type 'exit' to end the chat.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Thank you for using our chatbot. Have a great day! 👋")
            break
        
        best_match = get_best_match(user_input)
        if best_match:
            print(f"Bot: {responses[best_match]}\n")
        else:
            print("Bot: 🤔 I'm sorry, I don't understand that. Can you try rephrasing?")
            print("Here are some topics I can help with:")
            for topic in responses.keys():
                print(f"- {topic}")
            print()
            log_unknown_query(user_input)

# Run the chatbot
chatbot()