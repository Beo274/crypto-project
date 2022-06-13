# Encryption

def encryption(data: str, key: str):
    """
        Осуществляет шифрование текста
        :param data: незашифрованные данные
        :param key: ключ
        :return: зашифрованные данные
        """
    encrypted_text = ''
    encrypted_data = []
    ascii_data = bytes(data, encoding='utf-8')
    ascii_key = bytes(key, encoding='utf-8')
    for i in range(len(ascii_data)):
        encrypted_data.append(ascii_data[i] ^ ascii_key[i % len(ascii_key)])
        encrypted_text += chr(encrypted_data[i])
    return encrypted_text


# Decryption

def decryption(encrypted_text: str, key: str):
    """
        Осуществляет расшифровку текста
        :param encrypted_data: Зашифрованные данные
        :param key: Ключ
        :return: Расшифрованные данные
        """
    ascii_key = bytes(key, encoding='utf-8')
    encrypted_text = bytes(encrypted_text, encoding='utf-8')
    ascii_data = []
    data = ''
    for i in range(len(encrypted_text)):
        ascii_data.append(encrypted_text[i] ^ ascii_key[i % len(ascii_key)])
        data += chr(ascii_data[i])
    return data


# Opening

def opening(data: str):
    with open('task1.txt') as inf:
        for i in inf:
            data += i.strip()
        print(data)
        return data


# Creating new encrypted file

def creating_new__encrypted_file(encrypted_text):
    with open('encrypypted file.txt', 'w+') as newFile:
        newFile.write(encrypted_text)


# Initialization

data = ''  # input('Введите текст ')
key = input('Введите ключ ')

# Program

data = opening(data)

encrypted_text = encryption(data, key)

print(f'зашифрованный текст: {encrypted_text}')

creating_new__encrypted_file(encrypted_text)

data = decryption(encrypted_text, key)

print(f'расшифрованный текст: {data}')
