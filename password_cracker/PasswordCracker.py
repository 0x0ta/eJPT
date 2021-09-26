import http.client
import urllib.parse
import os

def main():
	usernamelist = input("Enter location of username list: ")
	passwordlist = input("Enter location of password lsit: ")
	attack_uri = input("Enter url to test: ")
	if (os.path.exists(usernamelist) != False):
		if(os.path.exists(passwordlist) != False):
			with open(usernamelist, "r") as F:
				for x in usernamelist.readlines():
					x = x.strip('\r\t\n')
					if (attack_uri.__contains__("https://") == False):
						print(f"Error: {attack_uri} does not contain https://")

		else:
			print(f"Error: {passwordlist} does not exist, please check the input and try again.")
	else:
		print(f"Error: {usernamelist} does not exist, please check input and try again.")


main()