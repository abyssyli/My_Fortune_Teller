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

# Session log file
today_str = datetime.now().strftime("%Y-%m-%d")
log_file = f"divination_9grid_{today_str}.txt"

def draw_nine_and_extra(question: str):
    # 3x3 grid
    cards = random.sample(lenormand_deck, 9)
    grid = [cards[i:i+3] for i in range(0, 9, 3)]

    # 5 extra cards not already drawn
    extra_cards = random.sample([c for c in lenormand_deck if c not in cards], 5)

    # Print
    print(f"\n✨ Your question: {question}")
    print("🃏 3x3 Grid:")
    for row in grid:
        print(" | ".join(row))
    print("\n🧩 Extra 5 Cards:")
    print(" | ".join(extra_cards))

    # Save to log
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n=== {datetime.now().isoformat()} ===\n")
        f.write(f"Question: {question}\n")
        f.write("3x3 Grid:\n")
        for row in grid:
            f.write(" | ".join(row) + "\n")
        f.write("Extra 5 Cards:\n")
        f.write(" | ".join(extra_cards) + "\n\n")

if __name__ == "__main__":
    print("🔮 Welcome to Lenormand 9-Grid Divination\n")

    while True:
        question = input("📝 What is your question?\n> ").strip()
        if not question:
            continue

        draw_nine_and_extra(question)

        while True:
            choice = input("💬 Ask another question? (y/n): ").strip().lower()
            if choice == "y":
                break
            elif choice == "n":
                print("\n🌟 The cards are silent now, but your will speaks louder. Keep going.\n")
                exit()
            else:
                print("⚠️ Please type 'y' to continue or 'n' to exit.")

