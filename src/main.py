from textnode import *


def main():
    bootdev = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    b2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    b3 = TextNode("This is a text node", TextType.ITALIC)

    print(bootdev)
    print(b2)
    print(b3)

    if bootdev.__eq__(b2):
        print("Both objects are equal")
    else:
        print("Objedts are not equal")


main()