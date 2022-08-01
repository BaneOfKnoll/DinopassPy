import requests
import clipboard

multiple = input("Do you want more than 1? (y/n)")

if multiple == "y":
    amount = input("How many?")
    for x in range(int(amount)):
        strong_url= "http://www.dinopass.com/password/strong"
        strongPass = requests.get(strong_url)
        print(str(strongPass.text))
else:
    strong_url= "http://www.dinopass.com/password/strong"
    strongPass = requests.get(strong_url)
    print(str(strongPass.text))
    clipboard.copy(str(strongPass.text))