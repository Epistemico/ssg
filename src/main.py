from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode


def main():
    bootdev = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(bootdev)

    node = HTMLNode("p", "A paragraph's element value", ["a", "img"], {"color": "black", "font-size": "10px"})
    print(node)

    leaf = LeafNode("b", "bold text", {"font-size": "10px"})
    print(leaf)


main()