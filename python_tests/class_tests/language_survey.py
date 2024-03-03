#!/usr/bin/python3

from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you speak first?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_responses(response)

# Show results
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()