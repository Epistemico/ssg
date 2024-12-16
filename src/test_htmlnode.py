import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_values(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold Text"),
                ParentNode("p", [LeafNode("strong", "Emphasis")]),
            ],
            {"display": "flex"},
        )
        self.assertEqual(node.tag, "div")
        self.assertIsInstance(node.children[0], LeafNode)
        self.assertIsInstance(node.children[1], ParentNode)
        self.assertEqual(node.props, {"display": "flex"})

    def test_repr(self):
        node = ParentNode("p", [LeafNode("b", "bold")])
        self.assertEqual(repr(node), "ParentNode(p, children: [LeafNode(b, bold, None)], None)")

    def test_to_html_value(self):
        node = ParentNode(None, [LeafNode("b", "boldy")])
        try:
            node.to_html()
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_to_html_no_children(self):
        node = ParentNode("p", [])
        node2 = ParentNode("div", None)
        try:
            node.to_html()
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        try:
            node2.to_html()
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_to_html_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_parent_in_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p",
                           [
                               LeafNode(None, "Hello, "), 
                               LeafNode("b", "world!"),
                               LeafNode("a", "Click here!", {"href": "https://www.boot.dev"})
                            ]
                ),
                LeafNode(None, "Link to image"),
                LeafNode("a", "of a cat.", {"href": "img/cat.jpg"}),
            ]
        )
        self.assertEqual(
            node.to_html(),
            '<div><p>Hello, <b>world!</b><a href="https://www.boot.dev">Click here!</a></p>Link to image<a href="img/cat.jpg">of a cat.</a></div>'
        )


if __name__ == "__main__":
    unittest.main()
