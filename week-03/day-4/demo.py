import urllib.request

while True:
    try:
        inp = input('Enter URL: ')
        req = urllib.request.Request(inp)
        with urllib.request.urlopen(req) as f:
            print(f.read(300))
        print('Valid')
    except:
        print('Invalid')
