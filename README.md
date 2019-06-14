# CRIME Attack
Assume a server can simulate the CRIME attack.
We know the secret is 16 characters. Try CRIME (Compression Ratio Info-leak Made Easy) attack.

## Execute

```bash
$ python main.py
```

## Method
1. If we want know secret web cookies from the HTTP header, We can send a message and try all possible characters after the header "Cookie: secret=". Then, send it to the server.
2. According to TLS compression (Before TLS Protocol version 1.2), if we guess the right answer of the first character, the compressed message we receive from the server will be shorter than other results.
3. However, sometimes we will get multiple characters by finding the shortest received messages if we use exhaustion(窮舉) method.
4. If we meet this problem, we can drop the first character of the header.
5. Finish repeating 2-4 steps until we find the only answer.
6. Then, try the second character and so on. We can stop until we get the last character (16 characters in this case) we want.
7. The header is below.

```
"POST / HTTP/1.1\r\n"
"Host: thebankserver.com\r\n"
"Connection: keep−alive \r\n"
"User−Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) "
"AppleWebKit/537.1 (KHTML, like Gecko) "
"Chrome/22.0.1207.1 Safari/537.1\r\n"
"Accept: */*\r\n"
"Referer: https://thebankserver.com/\r\n"
"Cookie: secret="
```

8. The header I tried is below.

```
"User−Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) "
"AppleWebKit/537.1 (KHTML, like Gecko) "
"Chrome/22.0.1207.1 Safari/537.1\r\n"
"Accept: */*\r\n"
"Referer: https://thebankserver.com/\r\n"
"Cookie: secret="
```

## Server
- IP: 140.122.185.174
- Port: 8081
- You can send a string to the server and the server will append your string to the following string. Then compress it, encrypt it and send the result back.


### Execute log and result

```
Answer of first 1 bytes: secret=6
Answer of first 2 bytes: secret=6I
Answer of first 3 bytes: secret=6Iv
Answer of first 4 bytes: secret=6IvT
Answer of first 5 bytes: secret=6IvT8
Answer of first 6 bytes: secret=6IvT83
Answer of first 7 bytes: secret=6IvT832
Answer of first 8 bytes: secret=6IvT8329
Answer of first 9 bytes: secret=6IvT8329s
Answer of first 10 bytes: secret=6IvT8329s8
Answer of first 11 bytes: secret=6IvT8329s8B
Answer of first 12 bytes: secret=6IvT8329s8BY
Answer of first 13 bytes: secret=6IvT8329s8BYN
Answer of first 14 bytes: secret=6IvT8329s8BYN4
Answer of first 15 bytes: secret=6IvT8329s8BYN45
Answer of first 16 bytes: secret=6IvT8329s8BYN454

Final result: secret=6IvT8329s8BYN454
```

## Reference
- http://securityalley.blogspot.com/2014/07/ssltls-crime.html
