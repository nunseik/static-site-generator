import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    def test_parent_eq(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test2_parent_eq(self):
        node = ParentNode("p", None)
        node2 = ParentNode("p", None, None)
        self.assertEqual(node, node2)

    def test_parent_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Invalid children: no value")

    def test_parent_no_tag(self):
        node = ParentNode(None, LeafNode("b", "Bold text"))
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Invalid tag: no value")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()