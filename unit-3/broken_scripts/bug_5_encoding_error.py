# BUG: Reading file containing emojis/unicode characters without specifying encoding='utf-8'
unicode_content = "AI welcomes you to 💻 Python class! 🚀 Sparkle: ✨"
with open("temp_emoji.txt", "w", encoding="utf-8") as f:
    f.write(unicode_content)

# Reading it back without encoding parameter (fails on some default windows/ascii encodings)
try:
    with open("temp_emoji.txt", "r") as f:
        print("Read Content:", f.read())
except UnicodeDecodeError as e:
    print("Encoding Error Caught:", e)
