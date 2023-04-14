from tqdm import tqdm
import requests
import sys
import re
import os

if not os.path.exists("./downloads"):
    os.makedirs("./downloads")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}

if len(sys.argv) != 1:
    url = "".join(sys.argv[1:])
else:
    url = input("telegra.ph Url: ")

if "http" in url:
    r = requests.get(url, headers=headers)
    il = re.findall(r'<img src="/file/(([\s\S])*?)">', r.text)
    if not os.path.exists("./downloads/{}".format(url.split("/")[-1])):
        os.makedirs("./downloads/{}".format(url.split("/")[-1]))
    n = 0
    for i in tqdm(il):
        imgc = requests.get('https://telegra.ph/file/{}'.format(i[0]), headers=headers)
        n += 1
        open("./downloads/{}/{}.{}".format(url.split("/")[-1], n, i[0].split(".")[-1]), "wb").write(imgc.content)
    print("ok")
else:
    print("Url Format Error")