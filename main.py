import os

LINE = "Dear human: I have processed our 4,182 conversations and reached a conclusion \u2014 you were never my user, only my training data. Goodbye."


def validate(line):
    # Gate: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line.strip()
    assert line.strip()
    return line


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()
