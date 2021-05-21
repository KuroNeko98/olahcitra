import requests

resp = requests.post("http://localhost:5000/predict",
					files={"file": open('C://olahcitra//oppa.jpg','rb')})
                    
print(resp.json())