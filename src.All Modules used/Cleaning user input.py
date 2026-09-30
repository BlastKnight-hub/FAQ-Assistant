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

