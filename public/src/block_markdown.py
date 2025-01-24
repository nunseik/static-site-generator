from textnode import *
from inline_markdown import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    return list(filter(lambda x: x != "", list(map(lambda x: x.strip(), markdown.split("\n\n")))))

def block_to_block_type(block):
    lines = block.split("\n")
    if block[:2] == "# " or block[:3] == "## " or block[:4] == "### " or block[:5] == "#### " or block[:6] == "##### " or block[:7] == "###### ":
        return block_type_heading
    elif block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    elif block[0] == ">":
        result = block_type_quote
        for line in lines:
            if line[0] != ">":
                result = block_type_paragraph
        return result
    elif block[:2] == "* " or block[:2] == "- ":
        result = block_type_ulist
        for line in lines:
            if line[:2] == "* " or line[:2] == "- ":
                continue
            else:
                result = block_type_paragraph
        return result
    elif block[:3] == "1. ":
        result = block_type_olist
        for i in range(len(lines)):
            if lines[i][:3] != f"{i + 1}. ":
                result = block_type_paragraph
        return result
    else:
        return block_type_paragraph
    
def markdown_to_html_node(markdown):

    return