import requests


url = "https://captcha-generator.p.rapidapi.com/"

querystring = {"noise_number":"10","fontname":"sora"}

headers = {
    "X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
    "X-RapidAPI-Host": "captcha-generator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


solution = response.json().get('solution')
print(solution)
img_url = response.json().get('image_url')
print(img_url)