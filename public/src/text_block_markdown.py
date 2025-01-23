import unittest
from block_markdown import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.   


        * This is the first list item in a list block\n* This is a list item\n* This is another list item"""

        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(markdown_to_blocks(input), expected)


if __name__ == "__main__":
    unittest.main()