from utils import clear_screen
from stats import Stats
try:
    from memory_game import play_memory
    from reaction_game import play_reaction
except Exception as e:
    print("Error importing games:", e)
    raise

def print_menu():
    clear_screen()
    print("="*40)
    print("   🧠 Brain Training — CLI Launcher")
    print("="*40)
    print("1) Memory Game (Number Memory)")
    print("2) Reaction Time Game")
    print("3) View Stats")
    print("4) Reset Stats")
    print("0) Exit")
    print("="*40)

def main():
    stats = Stats('data/scores.json')
    while True:
        print_menu()
        choice = input("Choose (0-4): ").strip()
        if choice == '1':
            result = play_memory()
            stats.update('memory_game', result)
            input('\nPress Enter to return to menu...')
        elif choice == '2':
            result = play_reaction()
            stats.update('reaction_game', result)
            input('\nPress Enter to return to menu...')
        elif choice == '3':
            clear_screen()
            print(stats)
            input('\nPress Enter to return to menu...')
        elif choice == '4':
            confirm = input('Reset all stats? (y/N): ').strip().lower()
            if confirm == 'y':
                stats.reset()
                print('Stats reset.')
                input('\nPress Enter to return to menu...')
        elif choice == '0':
            print('Goodbye — keep training that brain! 🧠')
            break
        else:
            print('Invalid choice — try again.')

if __name__ == '__main__':
    main()