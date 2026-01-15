
import random
import re

quotes = [
    "Code is like humor. When you have to explain it, it’s bad. – Cory House",
    "Fix the cause, not the symptom. – Steve McConnell",
    "Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck",
    "When to use iterative development? You should use iterative development only on projects that you want to succeed. – Martin Fowler",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Before software can be reusable it first has to be usable. – Ralph Johnson",
    "Make it work, make it right, make it fast. – Kent Beck",
    "Java is to JavaScript what car is to Carpet. – Chris Heilmann",
    "First, solve the problem. Then, write the code. – John Johnson",
    "Experience is the name everyone gives to their mistakes. – Oscar Wilde",
    "In order to be irreplaceable, one must always be different. – Coco Chanel",
    "Knowledge is power. – Francis Bacon",
    "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away. – Antoine de Saint-Exupery",
    "Code never lies, comments sometimes do. – Ron Jeffries",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Software is eating the world. – Marc Andreessen",
    "The only way to go fast, is to go well. - Robert C. Martin",
    "A user interface is like a joke. If you have to explain it, it's not that good.",
    "Deleted code is debugged code. – Jeff Sickel",
    "If debugging is the process of removing software bugs, then programming must be the process of putting them in. – Edsger Dijkstra"
]

def update_readme():
    try:
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()
        
        quote = random.choice(quotes)
        new_quote_section = f"<!-- QUOTE_START -->\n> 💡 **Random Dev Quote:**\n> \n> *\"{quote}\"*\n<!-- QUOTE_END -->"
        
        # Regex to find existing quote section and replace it
        pattern = r"<!-- QUOTE_START -->.*?<!-- QUOTE_END -->"
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, new_quote_section, content, flags=re.DOTALL)
        else:
            # Append if not found (though best to check where to insert, but user wants it added)
            # For robustness, let's assume the README already has the tags or we append them.
            # But the user *expects* me to format the README, so I will ensure the tags are there in the README write step.
            # Here we just replace.
             raise Exception("QUOTE placeholders not found in README.md")

        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(new_content)
            
        print(f"Updated quote to: {quote}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
