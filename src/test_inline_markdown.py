import unittest
from inline_markdown import *

from textnode import *
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_to_leafnode(self):
        node = TextNode("This is text", TextType.BOLD, "https://www.google.com")
        node2 = HTMLNode("b", "This is text")
        self.assertEqual(text_node_to_html_node(node), node2)
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )
    def test_basic_delimiter_handling(self):
        node = TextNode("This is a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode("This **bold** and **more bold**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("more bold", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_text_with_input_fully_highlighted(self):
        node = TextNode("**Fully highlighted**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("Fully highlighted", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

        # Test with no images
        text = "This text has no markdown images."
        self.assertEqual(extract_markdown_images(text), [])

        # Test with one image
        text = "Here is an image ![cat](https://cat-pic.com/cat.jpeg)"
        expected = [("cat", "https://cat-pic.com/cat.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(extract_markdown_links(text), expected)

        # Test with no links
        text = "This text has no markdown links."
        self.assertEqual(extract_markdown_links(text), [])

        # Test with one link
        text = "Here is a link [to Google](https://www.google.com)"
        expected = [("to Google", "https://www.google.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_split_nodes_image(self):
        nodes = [TextNode("This is text with an image ![cat](https://cat-pic.com/cat.jpeg) and more text", TextType.TEXT)]
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "https://cat-pic.com/cat.jpeg"),
            TextNode(" and more text", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_image(nodes), expected)

        # Test with no images
        nodes = [TextNode("This text has no images.", TextType.TEXT)]
        self.assertEqual(split_nodes_image(nodes), nodes)

        # Test with multiple images
        nodes = [TextNode("![dog](https://dog-pic.com/dog.jpeg) and ![bird](https://bird-pic.com/bird.jpeg)", TextType.TEXT)]
        expected = [
            TextNode("dog", TextType.IMAGE, "https://dog-pic.com/dog.jpeg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("bird", TextType.IMAGE, "https://bird-pic.com/bird.jpeg"),
        ]
        self.assertEqual(split_nodes_image(nodes), expected)

    def test_split_nodes_link(self):
        nodes = [TextNode("This is text with a [link](https://example.com) and more text", TextType.TEXT)]
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and more text", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_link(nodes), expected)

        # Test with no links
        nodes = [TextNode("This text has no links.", TextType.TEXT)]
        self.assertEqual(split_nodes_link(nodes), nodes)

        # Test with multiple links
        nodes = [TextNode("[Google](https://google.com) and [YouTube](https://youtube.com)", TextType.TEXT)]
        expected = [
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("YouTube", TextType.LINK, "https://youtube.com"),
        ]
        self.assertEqual(split_nodes_link(nodes), expected)

    def test_text_to_textnodes(self):
        text_input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text_input), expected)

if __name__ == "__main__":
    unittest.main()