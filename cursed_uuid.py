import uuid

# Function to convert UUID to octal
def uuid_to_octal(uuid_value):
    return oct(int(uuid_value.hex, 16))

# Function to map octal digits to emojis
def octal_to_emojis(octal_str):
    # Emoji mapping based on the provided list, with some assumed placeholders for demonstration
    emoji_map = {
        "00": "\U0001F60A",  # 😊
        "01": "\U0001F436",  # 🐶
        "02": "\U0001F431",  # 🐱
        "03": "\U0001F430",  # 🐰
        "04": "\U0001F98A",  # 🦊
        "05": "\U0001F43C",  # 🐼
        "06": "\U0001F428",  # 🐨
        "07": "\U0001F42F",  # 🐯
        "10": "\U0001F981",  # 🦁
        '10': '\U0001F42F',  # 🐯
        '11': '\U0001F43E',  # 🐾
        '12': '\U0001F42E',  # 🐮
        '13': '\U0001F437',  # 🐷
        '14': '\U0001F438',  # 🐸
        '15': '\U0001F414',  # 🐔
        '16': '\U0001F427',  # 🐧
        '17': '\U0001F426',  # 🐦
        '20': '\U0001F424',  # 🐤
        '21': '\U0001F41D',  # 🐝
        '22': '\U0001F41E',  # 🐜
        '23': '\U0001F98B',  # 🦋
        '24': '\U0001F33A',  # 🌺
        '25': '\U0001F338',  # 🌸
        '26': '\U0001F33C',  # 🌼
        '27': '\U0001F344',  # 🍄
        '30': '\U0001F308',  # 🌈
        '31': '\U0001F352',  # 🍒
        '32': '\U0001F349',  # 🍉
        '33': '\U0001F34D',  # 🍍
        '34': '\U0001F965',  # 🥥
        '35': '\U0001F9F8',  # 🧸
        '36': '\U0001F36B',  # 🍫
        '37': '\U0001F380',  # 🎀
        '40': '\U0001F388',  # 🎈
        '41': '\U0001F9C1',  # 🧁
        '42': '\U0001F369',  # 🍩
        '43': '\U0001F36A',  # 🍪
        '44': '\U0001F370',  # 🍰
        '45': '\U0001F36C',  # 🍬
        '46': '\U0001F36D',  # 🍭
        '47': '\U0001F36E',  # 🍮
        '50': '\U0001F36F',  # 🍯
        '51': '\U0001F37C',  # 🍼
        '52': '\U0001F351',   # 🍑
        '53': '\U0001F34E',  # 🍎
        '54': '\U0001F375',  # 🍵
        '55': '\U0001F964',  # 🥤
        '56': '\U0001F376',  # 🍶
        '57': '\U0001F37F',  # 🍿
        '60': '\U0001F35C',  # 🍜
        '61': '\U0001F35D',  # 🍝
        '62': '\U0001F355',  # 🍕
        '63': '\U0001F354',  # 🍔
        '64': '\U0001F35F',  # 🍟
        '65': '\U0001F32D',  # 🌭
        '66': '\U0001F953',  # 🥓
        '67': '\U0001F95A',  # 🥚
        '70': '\U0001F373',  # 🍳
        '71': '\U0001F951',  #🍳
        '72': '\U0001F366',  # 🍳
        '73': '\U0001F373',  # 🍳
        '74': '\U0001F9C0',  # 🧀
        '75': '\U0001F9C2',  # 🧂
        '76': '\U0001F9C3',  # 🧃
        '77': '\U0001F9C4',  # 🧄


        # Placeholder for unspecified mappings
        # Assuming "\U0001F600" (😀) for demonstration purposes
    }

    # Default emoji for unspecified mappings
    default_emoji = "\U0001F600"  # 😀

    # Convert octal string to two-digit groups, skipping the "0o" prefix
    octal_digits = octal_str[2:]
    emojis = ""
    for i in range(0, len(octal_digits), 2):
        two_digit = octal_digits[i:i+2]
        emojis += emoji_map.get(two_digit, default_emoji)
    
    return emojis

# Main function to generate emoji string from UUID
def generate_emoji_string():
    # Generate a UUID
    my_uuid = uuid.uuid4()
    
    # Convert the UUID to octal
    octal_uuid = uuid_to_octal(my_uuid)
    
    # Convert octal digits to emojis
    emoji_str = octal_to_emojis(octal_uuid)
    
    return my_uuid,emoji_str

# Generate and print the emoji string
print(generate_emoji_string())
