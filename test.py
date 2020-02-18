import pandas as pd
from buzzutil import get_page

NONCE = "ff3b45d52b"
save = {
    "title":[],
    "url":[]
}
for i in range(10):
    page = i + 1
    print("頁數:", page)
    result = get_page(page, NONCE)
    if result == None:
        break
    else:
        for (t, url) in result:
            save["title"].append(t)
            save["url"].append(url)
df = pd.DataFrame(save, columns=["title", "url"])
df.to_csv("buzz.csv", encoding="utf-8", index=False)
