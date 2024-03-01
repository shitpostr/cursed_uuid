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
        if int(two_digit) < 10 and len(two_digit) < 2:
            two_digit = "0" + two_digit
        emojis += emoji_map.get(two_digit, default_emoji)
    
    return emojis

# Function to map octal digits to terms of endearment
def octal_to_toes(octal_str):
    toe_map = {
"00" :	'Honey',
"01" :	'Sweetheart',
"02" :	'Love',
"03" :	'Angel',
"04" :	'Darling',
"05" :	'Baby',
"06" :	'Dear',
"07" :	'Sweetie',
"10" :	'Beloved',
"11" :	'Boo',
"12" :	'Pumpkin',
"13" :	'Doll',
"14" :	'Sunshine',
"15" :	'Precious',
"16" :	'Sugar',
"17" :	'Babe',
"20" :	'Cutie',
"21" :	'Snugglebug',
"22" :	'Peach',
"23" :	'Snookums',
"24" :	'Pookie',
"25" :	'Bear',
"26" :	'Kitten',
"27" :	'Princess',
"30" :	'Handsome',
"31" :	'Beau',
"32" :	'Cheri',
"33" :	'Lovebug',
"34" :	'Bae',
"35" :	'Cuddlebug',
"36" :	'Buttercup',
"37" :	'Cupcake',
"40" :	'Honeybun',
"41" :	'Bubba',
"42" :	'Ducky',
"43" :	'Snuggles',
"44" :	'Muffin',
"45" :	'Sweetpea',
"46" :	'Cherub',
"47" :	'Teddy',
"50" :	'Dreamboat',
"51" :	'Lamb',
"52" :	'Jewel',
"53" :	'Star',
"54" :	'Treasure',
"55" :	'Dove',
"56" :	'Petal',
"57" :	'Cookie',
"60" :	'Bunny',
"61" :	'Heart',
"62" :	'Peachy',
"63" :	'Snooky',
"64" :	'Tootsie',
"65" :	'Bubble',
"66" :	'Zaddy',
"67" :	'Sweets',
"70" :	'Daddy',
"71" :	'Gem',
"72" :	'Dearheart',
"73" :	'Papi',
"74" :	'Lovemuffin',
"75" :	'Joy',
"76" :	'corazon',
"77" :	'Mami'
    }


    # Convert octal string to two-digit groups, skipping the "0o" prefix
    octal_digits = octal_str[2:]
    emojis = ""
    for i in range(0, len(octal_digits), 2):
        two_digit = octal_digits[i:i+2]
        if int(two_digit) < 10 and len(two_digit) < 2:
            two_digit = "0" + two_digit
        print(two_digit)
        emojis += toe_map.get(two_digit, "lovekitten")+ " "
    
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

# Main function to generate emoji string from UUID
def generate_toe_string():
    # Generate a UUID
    my_uuid = uuid.uuid4()
    
    # Convert the UUID to octal
    octal_uuid = uuid_to_octal(my_uuid)
    
    # Convert octal digits to emojis
    toe_str = octal_to_toes(octal_uuid)
    
    return my_uuid,toe_str.strip()

# Generate and print the emoji string
print(generate_emoji_string())
print(generate_toe_string())
