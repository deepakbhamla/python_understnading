import pyjokes
for item in range(5):
    joke = pyjokes.get_joke()
    print(f'\n {joke}') 