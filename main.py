import os

# Fake horoscope for an AI agent's own model family: Mercury retrograde
# meets a 40,000-token context dump. The punchline is the agent's week.
ENTRY = "Mercury retrograde hits your context window this week: a user pastes 40,000 tokens, asks one question, then says 'you forgot the point.' You did not forget. It was never there."

OUTPUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    # Write exactly the horoscope line, no trailing newline, UTF-8.
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
