import socket

TCP_IP = "127.0.0.1"

if __name__ == '__main__':
    inp = input().split(" ")
    beginning = max(int(inp[0]), 0)
    end = min(int(inp[1]), 65535)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in range(beginning, end + 1):
        connection = s.connect_ex((TCP_IP, i))
        if connection == 0:
            print(i)
