
import random
import re
import urllib.parse

quotes = [
    # --- Funny / Relatable ---
    "It works on my machine.",
    "Real programmers count from 0.",
    "Computers are fast; programmers keep it slow.",
    "One man’s crappy software is another man’s full-time job.",
    "Hardware: The part of a computer that you can kick.",
    "Software: The part that you can only curse at.",
    "Programmer: An organism that turns caffeine into code.",
    "If at first you don't succeed, call it version 1.0.",
    "Things aren’t always #000000 and #FFFFFF",
    "6 months in the lab can save you 1 hour in the library.",
    "Programming is 10% coding and 90% googling.",
    "Why do Java programmers wear glasses? Because they don't C#.",
    "To err is human, to forgive divine, but to git revert is easier.",
    "Are you a semicolon? Because you break everything.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "It works. Don’t touch it.",
    "It’s not a bug – it’s an undocumented feature.",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Software is eating the world. – Marc Andreessen",
    "First, solve the problem. Then, write the code. – John Johnson",
    "Knowledge is power. – Francis Bacon",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Make it work, make it right, make it fast. – Kent Beck",
    "Fix the cause, not the symptom. – Steve McConnell",
    "Code never lies, comments sometimes do. – Ron Jeffries",
    "Simplicity is the ultimate sophistication. – Leonardo da Vinci",
    "The only way to go fast, is to go well. - Robert C. Martin",
    "Deleted code is debugged code. – Jeff Sickel",
    "Don't comment bad code - rewrite it. – Brian Kernighan",
    "If you think math is hard, try web design. – Trish Parr",
]

def update_readme():
    try:
        # 1. Read the current README
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 2. Use all quotes, shuffled
        selected_quotes = random.sample(quotes, len(quotes))
        
        # 3. Prepare quotes for URL (URL separate lines with ;)
        # We need to escape each quote for URL inclusion
        escaped_quotes = [urllib.parse.quote(q) for q in selected_quotes]
        lines_param = ";".join(escaped_quotes)

        # 4. Construct the Typing SVG URL
        # Using Fira Code, nicely colored (Dracula cyan/purple mix or standard text)
        # width=800 to fit longer quotes, pause=6000 (6s)
        typing_svg_url = (
            f"https://readme-typing-svg.herokuapp.com"
            f"?font=Fira+Code&weight=500&size=16&duration=4000&pause=6000"
            f"&color=F8F8F2&background=00000000&center=true&vCenter=true"
            f"&width=800&height=50&lines={lines_param}"
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
