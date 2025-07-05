import random

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

# Define keywords
negative_keywords = ["Scythe", "Coffin", "Tower", "Whip", "Snake", "Crossroads"]
good_ending_keywords = ["Heart", "Ring", "House", "Anchor"]

def draw_lenormand(n=5):
    question = input("🔮 What is your question? (in English): ")
    print(f"\n✨ Your question: \"{question}\"\n")

    cards = random.sample(lenormand_deck, n)
    print("🃏 Your cards:")
    for card in cards:
        print(f" - {card}")

    # Extract only card names (without number or emoji)
    card_names = [card.split(". ")[1].split(" ")[0] for card in cards]

    # Final card logic (priority 1)
    last_card = card_names[-1]
    if last_card == "Fish" or last_card in negative_keywords:
        print("\n❌ No, this will not succeed.")
        return

    # Scythe combo logic (priority 2)
    if "Scythe" in card_names:
        idx = card_names.index("Scythe")
        if idx > 0 and card_names[idx - 1] in good_ending_keywords:
            print("\n💥 Damn it.")
            return

    # Positive ending (priority 3)
    if last_card in good_ending_keywords:
        print("\n✅ Where there's a will, there's a way.")
        return

    # Default neutral interpretation
    print("\n🌈 The outlook is uncertain, but not hopeless.")

if __name__ == "__main__":
    draw_lenormand()
