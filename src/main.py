from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    text = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text)

    html = HTMLNode("p", "A paragraph's element value", ["a", "img"], {"color": "black", "font-size": "10px"})
    print(html)

    leaf = LeafNode("b", "bold text", {"font-size": "10px"})
    print(leaf)

    parent = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")])
    print(parent)


main()