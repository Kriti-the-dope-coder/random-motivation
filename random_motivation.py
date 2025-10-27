import random

print("Welcome to the Random Motivation Generator!\n")
print("Here are the categories you can choose from:\n")
print("A. 🏋️ Fitness & Gym \n")
print("B. ✨ Education, Career & Success\n")
print("C. 🌱 Personal Growth & Mindset \n")
print("D. 🔥 Overcoming Challenges \n")

# Display category menu and ask for input
category = input("Enter your category (A-D): ")

# Remove spaces and convert to uppercase
category = category.strip().upper()

#Store the category names in user input
categories = {
  "A": "Fitness & Gym",
  "B": "Education, Career & Success",
  "C": "Personal Growth & Mindset",
  "D": "Overcoming Challenges",
}

# Store motivational quotes for each category
quotes = {
    "A": [
        "Don't stop when you're tired. Stop when you're done. - Unknown",
        "The only bad workout is the one you skip. - Unknown",
        "The pain you feel today is the progress you make tomorrow. - Unknown",
        "Push harder than yesterday if you want a different tomorrow. - Unknown",
        "When you feel like quitting, think about why you started. - Unknown",
        "Great things never come from comfort zones. - Unknown"
    ],
    
    "B": [
        "The earlier you start working on something, the earlier you will see results. - Unknown",
        "You don’t have to be great to start. But you have to start to be great. - Unknown",
        "Every morning you have two choices: continue to sleep with your dreams, or wake up and chase them. - Unknown",
        "Work as hard as you can and be happy knowing you gave your best. - Unknown",
        "You have three choices: give up, give in, or give it everything you have got. - Unknown",
        "Successful people aren’t gifted; they work hard and succeed on purpose. - Unknown",
        "What we truly need to do is often what we most feel like avoiding. - Unknown"
        ],
    
    "C": [
        "All the water in the sea can’t sink a ship unless it gets inside. Similarly, negativity can’t bring you down unless you let it. - Unknown",
        "When it rains, look for rainbows. When it’s dark, look for stars. - Unknown",
        "Worrying doesn’t take away tomorrow’s troubles; it takes away today’s peace. - Unknown",
        "FEAR – Forget Everything And Run, or Face Everything And Rise. It’s your choice. - Unknown",
        "To overcome fear, you must go through it, not around it. - Unknown"
        ],
    "D": [
        "Let your excitement for success be greater than your fear of failure. - Unknown",
        "Be strong; things will get better. It may be stormy now, but it never rains forever. - Unknown",
        "Do what is right, not what is easy. - Unknown",
        "Many of life’s failures are people who did not realise how close they were to success when they gave up. - Thomas Edison",
        "Success is not final, failure is not fatal; it is the courage to continue that counts. - Unknown",
        "No one reaches the top of the mountain by accident. - Unknown"
        ]
}

# Only accept letters A-D
if category in ["A", "B", "C", "D"]:
    print("You chose:", categories[category])
    random_quote = random.choice(quotes[category])
    print("\nHere's your motivational quote:\n",random_quote)
else:
    print("Please choose from the given categories")
