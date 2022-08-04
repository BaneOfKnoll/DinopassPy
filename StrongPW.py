import requests
import clipboard

multiple = input("Do you want more than 1? (y/n)")
strong_url= "http://www.dinopass.com/password/strong"


if multiple == "y":
    amount = input("How many?")
    for x in range(int(amount)):
        strongPass = requests.get(strong_url)
        print(str(strongPass.text))
else:
    strongPass = requests.get(strong_url)
    print(str(strongPass.text))
    clipboard.copy(str(strongPass.text))