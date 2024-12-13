import unittest

from htmlnode import *


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


if __name__ == "__main__":
    unittest.main()
