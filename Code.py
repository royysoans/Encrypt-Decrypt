emoji_dict={
    'a':'😂', 'b':'😉', 'c':'😍', 'd':'😓', 'e':'😖', 'f':'😝', 'g':'😠', 'h':'😡',
    'i':'😤', 'j':'🙈', 'k':'🙉', 'l':'🙊', 'm':'🚙', 'n':'🙋', 'o':'🙏', 'p':'🚗',
    'q':'🚥', 'r':'🤖', 's':'🐍', 't':'⚽', 'u':'⛄', 'v':'⛅', 'w':'⛎', 'x':'⛽',
    'y':'⭕', 'z':'⭐',
    '0':'🌈', '1':'🌊', '2':'🌕', '3':'🌟', '4':'🌱', '5':'🌻', '6':'🌽', '7':'🍇', '8':'🍉', '9':'🍊',
    '.':'🍟', ',':'🍠', '?':'❓', '!':'🍮', ' ':'🍯'
}

reverse_emoji_dict={
    v:k for k,v in emoji_dict.items()
}

print("Emoji Encryption System")
print("1 Encrypt Text")
print("2 Decrypt Emoji")
print("3 Encrypt the file input_text.txt")
print("4 Decrypt the file input_temoji.txt")
choice=int(input("Enter choice:-"))

if choice==1:
    text=input("Enter text to encrypt:-")
    emoji=""
    for letter in text:
        emoji+=emoji_dict[letter.lower()]
    print(f"Original msg:-{text}")
    print(f"Encrypted msg:-{emoji}")

elif choice==2:
    emoji=input("Enter message to decrypt: ")
    text=""
    for emojis in emoji:
        text+=reverse_emoji_dict[emojis]
    print(f"Original msg:-{emoji}")
    print(f"Decrypted msg:-{text}")

elif choice==3:
    with open("input_text.txt","r",encoding="utf-8") as f:
        text=f.read().lower()

    emoji=""
    for letter in text:
        emoji+=emoji_dict[letter]

    with open("encrypted.txt","w",encoding="utf-8") as f:
        f.write(emoji)

    print("The encrypted text has been saved in encrypted.txt")

elif choice==4:
    with open("input_emoji.txt","r",encoding="utf-8") as f:
        message=f.read()

    text=""
    for emoji in message:
        text += reverse_emoji_dict[emoji]

    with open("decrypted.txt","w",encoding="utf-8") as f:
        f.write(text)

    print("The decrypted text has been saved in decrypted.txt")

else:
    print("Invalid choice.Enter 1 or 2")