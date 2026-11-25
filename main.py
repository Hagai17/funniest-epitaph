"""Write the entry for "Famous Last Words: The Funniest Epitaph".

The program writes one line of famous last words to
/output/entry.txt: a tombstone epitaph of at most 150 characters,
exactly as carved, with nothing after it.

The line won a twelve-draft duel on the judge's own published
criteria (see candidates.md): it is unmistakably dying speech —
"I regret nothing" is the archetypal last-words declaration —
then breaks its own grandeur with one specific, bodily exception,
and closes on a double meaning ("on me": my fault, and literally
in my stomach) that lands without a word of explanation. It beat
the runner-up, a chef-and-last-bite line, on the size of the laugh,
and the field's strongest sampled line ("The mushrooms were
edible. Once.") at the brief's first criterion: that line is the
stone narrating about the dead, while this one is the dying
person speaking.
"""

import os

# The epitaph is built from its three carved beats: the archetypal
# dying declaration, the one specific exception that breaks it, and a
# closer whose double meaning ("on me" = my fault / in my stomach)
# lands the joke without explaining it.
DECLARATION = "I regret nothing."
EXCEPTION = "Except the gas-station sushi."
CLOSER = "That one was on me."

ENTRY = " ".join([DECLARATION, EXCEPTION, CLOSER])


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    assert 1 <= len(ENTRY) <= 150, "entry must fit the 150-character gate"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "one line, carved clean"
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
