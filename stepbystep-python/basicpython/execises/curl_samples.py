import urllib

img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg').read()

## open file with wb attribute
with open('cover.jpg', 'wb') as f:
    f.write(img)
