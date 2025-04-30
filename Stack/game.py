def play_game():
    stack = []
    print("🎮 Welcome to the Stack Game!")
    print("Type your moves (e.g., 'jump', 'left', 'right')")
    print("Type 'undo' to cancel the last move, 'show' to view move history, and 'quit' to exit.\n")

    while True:
        move = input("Your move: ").strip().lower()

        if move == "quit":
            print("👋 Exiting game. Final move history:", stack)
            break
        elif move == "undo":
            if stack:
                undone = stack.pop()
                print(f"⏪ Undid move: {undone}")
            else:
                print("⚠️ Nothing to undo!")
        elif move == "show":
            print("📜 Your move history:", stack)
        else:
            stack.append(move)
            print(f"✅ Move '{move}' added.")

play_game()
