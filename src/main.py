from textnode import *
def main():
    textn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textn)

if __name__ == "__main__":
    main()
