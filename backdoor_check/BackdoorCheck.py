import requests as req


def main():
    print("*" * 40)
    server = input("Enter IP/Host to scan: ")
    print(f'Scanning: {server} for known backdoor webpages.')
    print("*" * 40)
    with open('BackdoorList.txt', encoding='utf8', errors='ignore') as f:
        for x in f.readlines():
            x = x.strip('\n\t\r')
            resp = req.request('GET', f'https://{server}/{x}')
            if resp.status_code == 200:
                print(f"{x}: Found on {server} @ {server}/{x}")


main()
