import requests
import clipboard

strong_url= "http://www.dinopass.com/password/strong"

strongPass = requests.get(strong_url)

clipboard.copy(str(strongPass.text))

print(str(strongPass.text))