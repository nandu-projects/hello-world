import sys
from datetime import datetime

def get_greeting(name: str = "World") -> str:
    cleaned = name.strip() if name and name.strip() else "World"
    return f"Hello, {cleaned}!"

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    greeting = get_greeting(name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {greeting}")

if __name__ == "__main__":
    main()
