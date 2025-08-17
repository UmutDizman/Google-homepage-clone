import requests
html = requests.get("https://getbootstrap.com/docs/5.3/examples/").text

with open(r"d:\PythonProject\bootstrapexamples\get.txt", "w") as file:
    file.write(html)
    file.close()


