from aiogram.types import Message
import requests

solution = None  # Global o'zgaruvchi

async def startCommandAnswer(message: Message): 
    global solution  # Global o'zgaruvchi
    url = "https://captcha-generator.p.rapidapi.com/"
    querystring = {"noise_number": "10", "fontname": "sora"}
    headers = {
        "X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
        "X-RapidAPI-Host": "captcha-generator.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    solution = response.json().get('solution')
    img_url = response.json().get('image_url')
    print(type(solution))
    
    await message.answer_photo(photo=img_url, caption="Shu rasmdagi so'zni yozing")
    print(solution)

async def userInputMessage(message: Message):
    global solution  # Global o'zgaruvchi
    text = message.text
    print(type(text))
    print(solution)
    if text == solution:
        await message.answer("Tog'ri kiritdingiz ☑")
    else:
        await message.answer('Xato kiritdingiz ❌')
