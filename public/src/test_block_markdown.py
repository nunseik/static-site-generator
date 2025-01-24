import unittest
from block_markdown import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.   


        * This is the first list item in a list block\n* This is a list item\n* This is another list item"""

        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(markdown_to_blocks(input), expected)

    def test_block_to_block_type(self):
        ordered = """
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(ordered)[0]), block_type_olist)
        code = """```
Sample text here...
```"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(code)[0]), block_type_code)
        heading = """# Blockquotes"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(heading)[0]), block_type_heading)
        quote = """
> text
> text
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(quote)[0]), block_type_quote)
        unordered = """
* Create a list by starting a line with `+`, `-`, or `*`
- Sub-lists are made by indenting 2 spaces:
- Marker character change forces new list start:
* Ac tristique libero volutpat at
- Facilisis in pretium nisl aliquet
- Nulla volutpat aliquam velit
* Very easy!
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(unordered)[0]), block_type_ulist)

if __name__ == "__main__":
    unittest.main()