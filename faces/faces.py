def convert(sentence):
    emoticons = ':)'
    sentence = sentence+" "+emoticons
    return sentence

def main():
    sentence = input()
    print(convert(sentence))
    

x = main()