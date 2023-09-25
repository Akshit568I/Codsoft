import re
def travel_agent_chatbot(user_input):
    user_input = user_input.lower()

    patterns = {
        
        r".*hii.*|hey.*|hello.*": "Hello ! I'm the travel agent chatbot. How may i help you ? ",
        r".*What.* destinations.* do.* you.* offer.|which places do you offer.*": "We offer a wide range of destinations, including spots like Parris, New York and Bali.Where are you interested in traveling",
        r".*Do.* you.* have.* any.* all.*incluisive.* vacation.* packages.|which packages do you have.*": "Yes , we offer all-incluisive vacation packages to various destinations.Can you specify your preffered destination and travel dates?",
        r".*What's.* the.* cancellation.* policy.* for.* hotel.* bookings.|what is the policy for cancellation of hotel.*": "Cancellation policies vary by hotel. Once you've chosen a specific hotel,I can provide you with its cancellation policy.",
        r".*What.* the.* best.* time.* to.* visit.* Hawai.|what is best time according to you to visit Hawai.*": "The best time to visit Hawaii is typically during the dry season , which is from April to October. The weather is warm and you can enjoy outdoor activities.",
        r".*I.* need.* a.* rental.* car.* for.* my.* trip.* to.* San Francisco. |how to get a rental car in San Francisco.*": "Great! We can help you with that. What are your travel dates, and do you have any specific preferences for the type of car you'd like to rent?",
        r".*Thanks.*Thank you.|Thank you for your valuable opinion.*": "You're welcome! Enjoy your trip. If you have more questions, feel free to ask.",
        r".*bye.*goodbye.|Goodbye.*": "Bye! If you ever need more guidance related to traveling, don't hesitate to return.",
    }
    for pattern, response in patterns.items():
        if re.match(pattern, user_input):
            return response
        
print("Chatbot: Hello! I'm the travel agent chatbot. how may i help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Bye! Enjoy your trip!")
        break
    response = travel_agent_chatbot(user_input)
    print("chatbot:", response)
        