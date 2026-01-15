
import random
import re
import urllib.parse

quotes = [
    # --- Funny / Relatable ---
    "It works on my machine.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "Real programmers count from 0.",
    "Computers are fast; programmers keep it slow.",
    "There are 10 types of people in the world: Those who understand binary, and those who don't.",
    "One man’s crappy software is another man’s full-time job.",
    "I don't always test my code, but when I do, I do it in production.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "A SQL query walks into a bar, walks up to two tables, and asks... 'Can I join you?'",
    "Hardware: The part of a computer that you can kick.",
    "Software: The part that you can only curse at.",
    "Programmer: An organism that turns caffeine into code.",
    "If at first you don't succeed, call it version 1.0.",
    "My code doesn't work, I have no idea why. My code works, I have no idea why.",
    "Things aren’t always #000000 and #FFFFFF",
    "6 months in the lab can save you 1 hour in the library.",
    "Programming is 10% coding and 90% googling.",
    "CSS is like a makeup kit for your website, but sometimes you accidentally draw the eyebrows on the chin.",
    "Algorithm: Word used by programmers when they don't want to explain what they did.",
    "Why do Java programmers wear glasses? Because they don't C#.",
    "Knock, knock. Who’s there? Recursion. Knock, knock. Who’s there? Recursion.",
    "To err is human, to forgive divine, but to git revert is easier.",
    "Are you a semicolon? Because you break everything.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Semicolons: The hide and seek champions of programming.",

    # --- Inspirational / Profound ---
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Software is eating the world. – Marc Andreessen",
    "First, solve the problem. Then, write the code. – John Johnson",
    "Experience is the name everyone gives to their mistakes. – Oscar Wilde",
    "Knowledge is power. – Francis Bacon",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Make it work, make it right, make it fast. – Kent Beck",
    "Fix the cause, not the symptom. – Steve McConnell",
    "Code never lies, comments sometimes do. – Ron Jeffries",
    "Simplicity is the ultimate sophistication. – Leonardo da Vinci",
    "The only way to go fast, is to go well. - Robert C. Martin",
    "Java is to JavaScript what car is to Carpet. – Chris Heilmann",
    "If you think math is hard, try web design. – Trish Parr",
    "Measuring programming progress by lines of code is like measuring aircraft building progress by weight. – Bill Gates",
    "The most disastrous thing that you can ever learn is your first programming language. – Alan Kay",
    "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program. – Linus Torvalds",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
    "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it. – Patrick McKenzie",
    "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away. – Antoine de Saint-Exupery",
    "Don't comment bad code - rewrite it. – Brian Kernighan",
    "Without requirements or design, programming is the art of adding bugs to an empty text file. – Louis Srygley",
    "Before software can be reusable it first has to be usable. – Ralph Johnson",
    "Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck",
    "Deleted code is debugged code. – Jeff Sickel",
    "It’s not a bug – it’s an undocumented feature."
]

def update_readme():
    try:
        # 1. Read the current README
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 2. Select randomly 5 quotes to cycle through in the typing animation
        selected_quotes = random.sample(quotes, 5)
        
        # 3. Prepare quotes for URL (URL separate lines with ;)
        # We need to escape each quote for URL inclusion
        escaped_quotes = [urllib.parse.quote(q) for q in selected_quotes]
        lines_param = ";".join(escaped_quotes)

        # 4. Construct the Typing SVG URL
        # Using Fira Code, nicely colored (Dracula cyan/purple mix or standard text)
        # width=600 to fit longer quotes
        typing_svg_url = (
            f"https://readme-typing-svg.herokuapp.com"
            f"?font=Fira+Code&weight=500&size=16&duration=4000&pause=1000"
            f"&color=F8F8F2&background=00000000&center=true&vCenter=true"
            f"&width=600&height=50&lines={lines_param}"
        )

        new_quote_section = (
            f"<!-- QUOTE_START -->\n"
            f"<div align=\"center\">\n"
            f"  <a href=\"https://github.com/sahhoutiamine\">\n"
            f"    <img src=\"{typing_svg_url}\" alt=\"Typing SVG\" />\n"
            f"  </a>\n"
            f"</div>\n"
            f"<!-- QUOTE_END -->"
        )
        
        # 5. Regex replacement
        pattern = r"<!-- QUOTE_START -->.*?<!-- QUOTE_END -->"
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, new_quote_section, content, flags=re.DOTALL)
            
            with open('README.md', 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            print("Successfully updated README with 5 random quotes.")
        else:
            print("Error: <!-- QUOTE_START --> placeholder not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
