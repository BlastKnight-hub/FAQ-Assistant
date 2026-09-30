# FAQ Rules
faq_rules= [
    (
        ["fee", "fees", "tuition", "payment"],
        "Please check the official portal or contact the administration for current fee and payment information."
    ),

    (
        ["admission", "eligibility", "apply", "application"],
        "Please check the official admission portal for eligibility requirements, application procedures, and deadlines."
    ),

    (
        ["library", "books", "timing", "hours"],
        "Please check your institution's official website or contact the library for current timings and book-related information."
    ),

    (
        ["hostel", "accommodation", "room"],
        "Please contact the accommodation or hostel office for availability, room details, and related policies."
    ),

    (
        ["attendance", "absent", "percentage"],
        "Attendance requirements depend on the institution's academic policy. Please check the official guidelines."
    ),

    (
        ["bus", "transport", "route", "commute"],
        "Please contact the transport office or check the official transport information for available routes and timings."
    ),

    (
        ["registration", "course", "subject", "enrollment"],
        "Please check the official registration portal for available courses, subjects, registration dates, and procedures."
    ),

    (
        ["exam", "test", "marks", "grading", "result", "cgpa"],
        "Please check the official academic portal for examination schedules, marks, results, and grading information."
    ),

    (
        ["contact", "help", "support", "office"],
        "Please contact the relevant administration or help desk for further assistance."
    ),

    (
        ["timing", "schedule", "hours", "open"],
        "Please check the official website or contact the relevant department for current timings."
    )
]


#1. Displaying the welcome screen
def welcome():
    print("-" * 75)
    print("                    Welcome to the FAQ Bot!")
    print("-" * 75)
    print("You can ask about:")
    print("fees, admission, library, hostel, transport, registration,")
    print("examinations, attendance, timings, or support.")
    print("Type 'exit' to stop the program.")
    print("-" * 75)


#2. Cleaning the user input
def clean(user_input):
    return user_input.lower().strip()


#3. Finding the matching answer
def ans(question):
    
    for keywords, response in faq_rules:

        
        for word in keywords:

            
            if word in question:
                return response

    #Fallback if no match is found
    return "Sorry, I could not understand your question. Please try again or contact the help desk."


#4. Main control flow
def start():
    welcome()

    while True:
        question=input("\nYou: ")

        cleaned_question=clean(question)

        
        if cleaned_question == "exit":
            print("Thank you for using the FAQ Bot!")
            break

        
        answer=ans(cleaned_question)
        print("Bot:", answer)


# Start the program
if __name__ == "__main__":
    start()
