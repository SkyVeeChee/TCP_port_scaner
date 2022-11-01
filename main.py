import socket

if __name__ == '__main__':
    inp = input().split(" ")
    beginning = max(int(inp[0]), 0)
    end = min(int(inp[1]), 65535)
    IP_address = inp[2]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in range(beginning, end + 1):
        connection = s.connect_ex((IP_address, i))
        if connection == 0:
            print(i)
