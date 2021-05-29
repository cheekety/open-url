import os
import webbrowser

url = ["https://github.com/yeock", "https://www.youtube.com", "https://mail.google.com"]

webbrowser.register(
    "firefox",
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox")
)

def run():
    for i in range(len(url)):
        webbrowser.get("firefox").open(url[i])

run()
