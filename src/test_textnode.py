import unittest
from htmlnode import LeafNode
from textnode import TextType, TextNode, text_node_to_html


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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_leaf_error(self):
        node = TextNode("Normal text", None)
        try:
            leaf = text_node_to_html(node)
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_textnode_to_leafnode(self):
        text_textnode = TextNode("Normal text", TextType.TEXT)
        bold_textnode = TextNode("Bold text", TextType.BOLD)
        italic_textnode = TextNode("Italic text", TextType.ITALIC)
        code_textnode = TextNode("Code text", TextType.CODE)
        link_textnode = TextNode("Link text", TextType.LINK, "https://www.boot.dev")
        image_textnode = TextNode("Image text", TextType.IMAGE, "img/cat.jpg")

        self.assertIsInstance(
            text_node_to_html(text_textnode), LeafNode
        )
        self.assertIsInstance(
            text_node_to_html(bold_textnode), LeafNode
        )
        self.assertIsInstance(
            text_node_to_html(italic_textnode), LeafNode
        )
        self.assertIsInstance(
            text_node_to_html(code_textnode), LeafNode
        )
        self.assertIsInstance(
            text_node_to_html(link_textnode), LeafNode
        )
        self.assertIsInstance(
            text_node_to_html(image_textnode), LeafNode
        )

    def test_textnode_to_leafnode_to_html(self):
        text_leafnode = text_node_to_html(TextNode("Normal text", TextType.TEXT))
        bold_leafnode = text_node_to_html(TextNode("Bold text", TextType.BOLD))
        italic_leafnode = text_node_to_html(TextNode("Italic text", TextType.ITALIC))
        code_leafnode = text_node_to_html(TextNode("Code text", TextType.CODE))
        link_leafnode = text_node_to_html(TextNode("Link", TextType.LINK, "https://www.boot.dev"))
        image_leafnode = text_node_to_html(TextNode("Image text", TextType.IMAGE, "img/cat.jpg"))

        self.assertEqual(text_leafnode.to_html(), "Normal text")
        self.assertEqual(bold_leafnode.to_html(), "<b>Bold text</b>")
        self.assertEqual(italic_leafnode.to_html(), "<i>Italic text</i>")
        self.assertEqual(code_leafnode.to_html(), "<code>Code text</code>")
        self.assertEqual(link_leafnode.to_html(), '<a href="https://www.boot.dev">Link</a>')
        self.assertEqual(image_leafnode.to_html(), '<img src="img/cat.jpg" alt="Image text"></img>')
        self.assertEqual(image_leafnode.value, "")


if __name__ == "__main__":
    unittest.main()
