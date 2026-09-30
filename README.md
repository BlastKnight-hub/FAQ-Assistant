Rule-Based FAQ Chatbot
A simple Python-based FAQ chatbot that provides answers to frequently asked questions using predefined keywords and responses.
This project is built using basic Python concepts such as lists, tuples, functions, loops, conditional statements, and string handling. It does not use AI, machine learning, or external libraries.

How It Works
The chatbot works using a simple rule-based system.
The user enters a question.
The input is converted to lowercase.
The program checks the question against predefined keywords.
If a keyword matches, the corresponding answer is displayed.
If no keyword matches, a default response is displayed.
The user can type `exit` to close the program.
Example
```text
---------------------------------------------------------------------------
                    Welcome to the FAQ Bot!
---------------------------------------------------------------------------
You can ask about:
fees, admission, library, hostel, transport, registration,
examinations, attendance, timings, or support.
Type 'exit' to stop the program.
---------------------------------------------------------------------------

You: What are the fees?

Bot: Please check the official portal or contact the administration
for current fee and payment information.

You: What are the library timings?

Bot: Please check your institution's official website or contact
the library for current timings and book-related information.

You: exit

Thank you for using the FAQ Bot!
```
Technologies Used
Python 3
No third-party Python packages are required.
Project Structure
```text
Rule-Based-FAQ-Chatbot/
│
├── faq_bot.py
├── README.md
├── statement.md
└── .gitignore
```
Installation
Make sure Python 3 is installed on your computer.
You can check your Python version using:
```bash
python --version
```
How to Run
Clone the repository
https://github.com/BlastKnight-hub/VITyarthi.git
Open the project folder
cd Healthcare-Awareness-Campaign
Run the Python program
Run main.py

Limitations
Since this is a rule-based chatbot, it has some limitations:
It does not understand the meaning of a question.
It only searches for predefined keywords.
Different wording may not always produce the expected answer.
It does not learn from previous conversations.
It does not use artificial intelligence or machine learning.
FAQ information must be manually updated.
Future Improvements
Possible improvements include:
Better keyword matching
Fuzzy string matching
A graphical user interface
Web-based interface
Storing FAQs in a database
Adding more FAQ categories
Separating FAQ data from chatbot logic
Adding an admin system for updating FAQs
Learning Objectives
This project demonstrates the use of:
Python lists
Tuples
Functions
`for` loops
`while` loops
`if` statements
String methods
User input
Basic program structure
Rule-based decision making
Author
Developed as a Python learning project.
