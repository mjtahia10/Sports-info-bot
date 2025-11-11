import random
from colorama import Fore, Style, init


init(autoreset=True)

sports_facts = {
    "football": [
        "Football is the most popular sport in the world with over 4 billion fans.",
        "The first FIFA World Cup was held in 1930 in Uruguay.",
        "Cristiano Ronaldo and Lionel Messi are among the top goal scorers in history."
    ],
    "cricket": [
        "Cricket originated in England during the 16th century.",
        "Sachin Tendulkar is the only player to have scored 100 international centuries.",
        "The ICC Cricket World Cup is held every 4 years."
    ],
    "basketball": [
        "Basketball was invented by Dr. James Naismith in 1891.",
        "The NBA is the premier professional basketball league in the world.",
        "Michael Jordan is widely regarded as one of the greatest players of all time."
    ],
    "tennis": [
        "The oldest tennis tournament in the world is Wimbledon.",
        "Roger Federer, Rafael Nadal, and Novak Djokovic have dominated men’s tennis for two decades.",
        "Tennis can be played on grass, clay, or hard court surfaces."
    ],
    "hockey": [
        "Field hockey is India’s national sport.",
        "The modern game of ice hockey originated in Canada in the 19th century.",
        "Dhyan Chand is known as one of the greatest field hockey players ever."
    ]
}

motivational_quotes = [
    "Don’t practice until you get it right, practice until you can’t get it wrong.",
    "Champions keep playing until they get it right.",
    "It’s not whether you get knocked down; it’s whether you get up. — Vince Lombardi",
    "Winning isn’t everything, but wanting to win is. — Bear Bryant",
    "Hard work beats talent when talent doesn’t work hard."
]

def show_menu():
    print(Fore.CYAN + "\n==============================")
    print(Fore.CYAN + "🏆  Welcome to the Sports Info Bot 🏆")
    print(Fore.CYAN + "==============================")
    print(Fore.YELLOW + "\nOptions:")
    print(Fore.GREEN + "1. Get random sports fact")
    print(Fore.GREEN + "2. Get motivational quote")
    print(Fore.GREEN + "3. Chat freely with the bot")
    print(Fore.RED + "4. Exit\n")

def get_sports_fact():
    sport = input(Fore.YELLOW + "Enter a sport (football, cricket, basketball, tennis, hockey): ").lower()
    if sport in sports_facts:
        fact = random.choice(sports_facts[sport])
        print(Fore.MAGENTA + f"\n🏅 Fact about {sport.capitalize()}: " + Fore.CYAN + fact)
    else:
        print(Fore.RED + "Sorry, I don't have information on that sport yet.")

def random_quote():
    print(Fore.MAGENTA + "\n💭 " + random.choice(motivational_quotes))

def chat_freely():
    print(Fore.CYAN + "\nBot: You can chat with me about sports! Type 'back' to return to the menu.\n")
    
    responses = {
        "football": [
            "Football is life! ⚽ Do you support any team?",
            "Messi or Ronaldo — who’s your favorite? 😏",
            "Football matches bring so much energy!"
        ],
        "cricket": [
            "Cricket is such a strategic game! 🏏",
            "Who’s your favorite cricketer — Kohli, Babar, or Root?",
            "Did you know? A cricket match can last up to 5 days!"
        ],
        "basketball": [
            "Basketball is full of action 🏀!",
            "LeBron James is still dominating the NBA!",
            "Who’s your favorite team — Lakers or Bulls?"
        ],
        "tennis": [
            "Tennis requires incredible stamina 🎾",
            "Federer vs Nadal was one of the greatest rivalries ever!",
            "Do you follow Grand Slam tournaments?"
        ],
        "hockey": [
            "Hockey is fast and exciting! 🏑",
            "Did you know India has won 8 Olympic golds in hockey?",
            "Ice hockey and field hockey are both awesome in their own ways!"
        ],
        "motivation": [
            "Never give up! Every champion was once a beginner. 💪",
            "Consistency makes athletes great!",
            "Push your limits — that's how legends are made. 🏆"
        ],
        "default": [
            "That’s interesting! Tell me more about your favorite sport 😊",
            "Sports teach us teamwork and perseverance.",
            "Hmm, sounds cool! Want to hear a sports fact?"
        ]
    }

    while True:
        query = input(Fore.YELLOW + "You: ").lower().strip()

        if query == "back":
            print(Fore.CYAN + "Bot: Going back to the main menu... 🏁\n")
            break
        
        elif "football" in query:
            print(Fore.GREEN + "Bot: " + random.choice(responses["football"]))
        elif "cricket" in query:
            print(Fore.MAGENTA + "Bot: " + random.choice(responses["cricket"]))
        elif "basketball" in query:
            print(Fore.CYAN + "Bot: " + random.choice(responses["basketball"]))
        elif "tennis" in query:
            print(Fore.YELLOW + "Bot: " + random.choice(responses["tennis"]))
        elif "hockey" in query:
            print(Fore.GREEN + "Bot: " + random.choice(responses["hockey"]))
        elif "motivation" in query or "quote" in query:
            print(Fore.MAGENTA + "Bot: " + random.choice(responses["motivation"]))
            random_quote()
        else:
            print(Fore.CYAN + "Bot: " + random.choice(responses["default"]))

while True:
    show_menu()
    choice = input(Fore.YELLOW + "Enter your choice (1-4): ").strip()

    if choice == "1":
        get_sports_fact()
    elif choice == "2":
        random_quote()
    elif choice == "3":
        chat_freely()
    elif choice == "4":
        print(Fore.CYAN + "\n🏅 Goodbye! Keep playing and stay strong! 💪")
        break
    else:
        print(Fore.RED + "Invalid choice. Try again.")
