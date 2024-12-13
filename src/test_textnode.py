import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is an anchor node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is an anchor node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_eq_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, "img/cat.jpg")
        node2 = TextNode("This is an image node", TextType.IMAGE, "img/cat.jpg")
        self.assertEqual(node, node2)

    def test_eq_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        node2 = TextNode("This is a code node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsNone(node.url)
    
    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertIsNotNone(node.url)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a normal text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a link node, link, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
