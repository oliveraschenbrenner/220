# Add your encryption methods here
def encode(message, key):
    acc = ""
    for i in message:
        j = ord(i)
        j = j + key
        i = chr(j)
        acc = acc + i
    return acc


def encode_better(message, key):
    acc = ""
    for i in range(len(message)):
        c = message[i]
        keyword = key[i % len(key)]
        c_value = ord(c)
        keyword_value = ord(keyword) - 97
        j = c_value + keyword_value
        k = chr(j)
        acc = acc + k
    return acc
