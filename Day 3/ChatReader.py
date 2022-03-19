from ctypes import WinError
import socket
import re

twitchIrcServer = "irc.chat.twitch.tv"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((twitchIrcServer, 6667))
irc.setblocking(False)
irc.send("NICK justinfan12345\r\n".encode("utf-8"))
irc.send("JOIN #mrteathyme\n\r".encode('utf-8'))

while True:
    try:
        readBuffer = irc.recv(2048)
        msg = readBuffer.decode("utf-8")
        parsedMsg = re.search(r'(#mrteathyme :)(.*)', msg)[2]
        print(msg)
        print(parsedMsg)
    except BlockingIOError as exc:
        pass
    except Exception as exc:
        print(exc)

    #break