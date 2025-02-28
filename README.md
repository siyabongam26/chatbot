RITA Africa Chatbot
Overview
The RITA Africa Chatbot is a customer support chatbot designed to assist users with common questions about RITA Africa's programs, certifications, and application processes. The chatbot uses fuzzy matching to understand variations in user queries, providing accurate and relevant responses. It can be run as a command-line application, a desktop application with a GUI, or deployed as a web application.

Features
Fuzzy Matching: Understands variations in user queries using the fuzzywuzzy library.

Interactive Interface: Provides a user-friendly interface for seamless interaction.

Logging Unknown Queries: Logs unrecognized queries for future analysis and training.

Multiple Deployment Options:

Command-line interface (CLI)

Desktop application (using tkinter)

Web application (using Flask)

Installation
Prerequisites
Python 3.7 or higher

fuzzywuzzy library

python-Levenshtein (for faster fuzzy matching)

Flask (for web application deployment)

tkinter (for desktop GUI, usually comes pre-installed with Python)

Steps
Clone the repository:

bash
Copy
git clone https://github.com/siyabongam26/chatbot.git
cd rita-africa-chatbot
Install the required libraries:

bash
Copy
pip install -r requirements.txt
(Optional) Install python-Levenshtein for faster fuzzy matching:

bash
Copy
pip install python-Levenshtein
