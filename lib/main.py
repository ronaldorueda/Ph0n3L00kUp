#created and coded by ronaldorueda aka setin07
#main will get phone number and access json files

import requests

#everything is separate depending on API requirements
nationCode = input("Enter national code number: +")
phoneNum = input("Enter phone number: ")
phone = nationCode + phoneNum

print("\n")

print(phone)

print("\n")

#will quit program
exit = input ("Press enter to exit.")