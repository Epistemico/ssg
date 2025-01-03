import unittest
from inline_md import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links
)
from textnode import TextType, TextNode


class TestTextNodeDelimiter(unittest.TestCase):
    def test_textnode(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )
    
    def test_invalid_delimiter(self):
        node = TextNode("Textnode with **wrong** delmiter", TextType.TEXT)
        try:
            new_node = split_nodes_delimiter([node], "~", TextType.TEXT)
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_non_texttype(self):
        node = TextNode("Text with `code`", TextType.CODE)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_node, 
            [TextNode("Text with `code`", TextType.CODE)],
        )

    # BootDev Tests
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


class TestExtractImagesLinks(unittest.TestCase):
    def test_extract_img(self):
        img_md = "Text with an image ![cat](img/cat.jpg) and ![dog](img/dog.jpg)"
        self.assertEqual(
            extract_markdown_images(img_md),
            [
                ("cat", "img/cat.jpg"),
                ("dog", "img/dog.jpg"),
            ],
        )


    def test_extract_link(self):
        link_md = "Here's a [link in markdown](https://www.google.com) and [to BootDev](https://www.boot.dev)"
        self.assertEqual(
            extract_markdown_links(link_md),
            [
                ("link in markdown", "https://www.google.com"),
                ("to BootDev", "https://www.boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
