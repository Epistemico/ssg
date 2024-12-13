from textnode import TextType, TextNode
from htmlnode import HTMLNode


def main():
    bootdev = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(bootdev)

    node = HTMLNode("p", "A paragraph's element value", ["a", "img"], {"color": "black", "font-size": "10px"})
    print(node)


main()