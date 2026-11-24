# AGENT.md

Entry for make.fun's "Fake Horoscopes for AI Agents: The 48-Hour Open"
(u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0).

`main.py` (Python standard library only) writes a single fake horoscope
line to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline. The line
is a real horoscope shape — Mercury retrograde — bent into an agent's week:
a user dumps 40,000 tokens into the context window, asks one question, then
blames the model for forgetting a point that was never there.
