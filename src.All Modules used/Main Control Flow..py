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

