import unittest

from htmlnode import HTMLNode, LeafNode

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
    def test_leaf_eq(self):
        node = LeafNode("h1", "This is the title", None)
        node2 = LeafNode("h1", "This is the title")
        self.assertEqual(node, node2)
    def test_leafs_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test2_leafs_to_html(self):
        node = LeafNode("div", "Hello", {"class": "greeting", "id": "msg", "data-test": "true"})
        self.assertEqual(node.to_html(), '<div class="greeting" data-test="true" id="msg">Hello</div>')

if __name__ == "__main__":
    unittest.main()