# Chatbot Project – Online Food Delivery Assistant
A modern, conversational AI chatbot designed to streamline the online food ordering experience. Built with FastAPI for backend logic and Google Dialogflow for natural language understanding, this project demonstrates end-to-end chatbot development—from intent recognition to order processing and real-time order tracking.

## Key Features
### Conversational Ordering:
Supports placing new food orders and tracking existing orders through natural language interactions.

### Dialogflow Integration:
Utilises Google Dialogflow for advanced intent detection and entity extraction.

### FastAPI Backend:
Handles backend business logic, order management, and API integrations efficiently.

### Context Management:
Manages user sessions and context to provide a seamless, multi-turn conversation flow.

### Modular Architecture:
Clean separation between frontend chatbot, NLP (Dialogflow), and backend (FastAPI) components.

## Tech Stack
- Python
- FastAPI (for backend Server Api to handle Dialogflow webshook API)
- Dialogflow (Google Cloud)
- Uvicorn
- ngrok.exe (to make web url from http to https)
- MySQL
- Regex
- Natural Language Processing (NLP) 
- HTML, CSS, JavaScript (For Developing website Frontend to integrate Chatbot agent)
- Github

## This project highlights my skills in:

- **Conversational AI development**
- **API design with FastAPI**
- **Natural Language Processing (NLP)**
- **Cloud-based chatbot solutions**
- **Software engineering best practices (version control, branching, modular code)**


Directory structure
===================
- Frontend: Contains frontend website code and images where integrated chatbot
- db\indian_eatery.sql: contains the dump of the database. you need to import this into your MySQL db by using MySQL workbench tool
- db\db_helper.py : Contains python code to handle database function
- dialogflow_training_assest: this has training phrases etc. for our intents
- main.py : It main app file for fast API where dialogflow webhook api call handles
- requirement.txt: contain package requirement to run this project

Install these modules
======================

pip install mysql-connector
pip install "fastapi[all]"

OR just run pip install -r requirements.txt to install both in one shot

To start fastapi backend server
================================
1. Go to main directory of your project in your command prompt or terminal
2. Run this command: uvicorn main:app --reload

ngrok for https tunneling
================================
1. To install ngrok, go to https://ngrok.com/download and install ngrok version that is suitable for your OS
2. Extract the zip file and place ngrok.exe in a folder.
3. Open windows command prompt, go to that folder and run this command: ngrok http 80000

NOTE: ngrok can timeout. you need to restart the session if you see session expired message.
