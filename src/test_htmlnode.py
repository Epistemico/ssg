import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "p",
            "Some text here",
        )
        self.assertEqual(
            node.tag,
            "p",
        )
        self.assertEqual(
            node.value,
            "Some text here",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_not_eq(self):
        node = HTMLNode(
            "p",
            "Value",
            ["a"],
            {"color": "black", "font-size": "10px"}
        )
        node2 = HTMLNode(
            "p",
            "Value",
            ["a"],
            {"color": "black", "font-size": "10px"}
        )
        self.assertNotEqual(node, node2)

    def test_attr(self):
        node = HTMLNode(
            "p", 
            "Value", 
            None, 
            {"color": "black", "font-size": "10px"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' color="black" font-size="10px"',
        )

    def test_repr(self):
        node = HTMLNode(
            "p", 
            "Value", 
            ["a", "div"], 
            {"color": "black", "font-size": "10px"}
        )
        self.assertEqual(
            "HTMLNode(p, Value, children: ['a', 'div'], {'color': 'black', 'font-size': '10px'})",
            repr(node),
        )


class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode("a", "Click link", {"href": "https://www.boot.dev"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click link")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.boot.dev"})

    def test_props(self):
        node = LeafNode("p", "Paragraph text")
        self.assertIsNone(node.props, None)

    def test_to_html(self):
        node = LeafNode("p", "Paragraph text")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<p>Paragraph text</p>')
        self.assertEqual(node2.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "raw string")
        self.assertEqual(node.to_html(), "raw string")

    def test_to_html_error(self):
        node = LeafNode("b", None)
        try:
            node.to_html()
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_repr(self):
        node = LeafNode("b", "Bold")
        self.assertEqual(node.__repr__(), "LeafNode(b, Bold, None)")


if __name__ == "__main__":
    unittest.main()
