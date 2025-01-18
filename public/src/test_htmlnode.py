import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "This is the title", None, None)
        node2 = HTMLNode("h1", "This is the title")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode("h1", "This is the title", None, "None")
        node2 = HTMLNode("h1", "This is the title", None, None)
        self.assertNotEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode("h1", "This is the title", None, { "href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()