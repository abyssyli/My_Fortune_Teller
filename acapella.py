import random
from datetime import datetime

# Lenormand card deck
lenormand_deck = [
    "1. Rider 🐎", "2. Clover 🍀", "3. Ship ⛵", "4. House 🏠", "5. Tree 🌳", "6. Clouds ☁️",
    "7. Snake 🐍", "8. Coffin ⚰️", "9. Bouquet 🌸", "10. Scythe 🔪", "11. Whip 🥊", "12. Birds 🐦",
    "13. Child 👶", "14. Fox 🦊", "15. Bear 🐻", "16. Stars ✨", "17. Stork 🕊️", "18. Dog 🐶",
    "19. Tower 🗼", "20. Garden 🌼", "21. Mountain ⛰️", "22. Crossroads 🛣️", "23. Mice 🐭",
    "24. Heart ❤️", "25. Ring 💍", "26. Book 📖", "27. Letter ✉️", "28. Man 👨", "29. Woman 👩",
    "30. Lily 🌺", "31. Sun ☀️", "32. Moon 🌙", "33. Key 🔑", "34. Fish 🐟", "35. Anchor ⚓",
    "36. Cross ✝️"
]

negative_keywords = ["Scythe", "Coffin", "Tower", "Whip", "Snake", "Crossroads"]
good_ending_keywords = ["Heart", "Ring", "House", "Anchor"]

# Generate log file name
today_str = datetime.now().strftime("%Y-%m-%d")
log_file = f"divination_log_{today_str}.txt"

def draw_lenormand(n=5):
    while True:
        question = input("🔮 What is your question?\n> ").strip()
        if not question:
            continue

        print(f"\n✨ Your question: \"{question}\"\n")

        cards = random.sample(lenormand_deck, n)
        print("🃏 Your cards:")
        for card in cards:
            print(f" - {card}")

        card_names = [card.split(". ")[1].split(" ")[0] for card in cards]
        last_card = card_names[-1]
        result = ""

        # Rule-based interpretation
        if last_card == "Fish" or last_card in negative_keywords:
            result = "No, this will not succeed."
        elif "Scythe" in card_names:
            idx = card_names.index("Scythe")
            if idx > 0 and card_names[idx - 1] in good_ending_keywords:
                result = "Damn it."
            else:
                result = "The outlook is uncertain, but not hopeless."
        elif last_card in good_ending_keywords:
            result = "Where there's a will, there's a way."
        else:
            result = "The outlook is uncertain, but not hopeless."

        print(f"\n🔍 Interpretation: {result}")
        print(f"📄 Result saved to: {log_file}\n")

        # Write to log file
        with open(log_file, mode="a", encoding="utf-8") as f:
            f.write(f"=== {datetime.now().isoformat()} ===\n")
            f.write(f"Question: {question}\n")
            f.write(f"Cards: {', '.join(card_names)}\n")
            f.write(f"Result: {result}\n\n")

        # Ask if user wants another round
        while True:
            choice = input("💬 Ask another question? (y/n): ").strip().lower()
            if choice == "y":
                break
            elif choice == "n":
                print("\n🌟 The cards are silent now, but your will speaks louder. Keep going.\n")
                return
            else:
                print("⚠️ Please type 'y' to continue or 'n' to exit.")

if __name__ == "__main__":
    draw_lenormand()


