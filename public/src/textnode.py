from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"
    NORMAL = "normal"

class TextNode():
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode):
        return isinstance(textnode, TextNode) and self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Text type not valid")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in node.text:
            raise Exception("delimiter not found in node")
        else:
            splitted = node.text.split(delimiter)
            for i in range(len(splitted)):
                if i % 2 == 0 and splitted[i] != "":
                    inside_node = TextNode(splitted[i], TextType.TEXT)
                    new_nodes.append(inside_node)
                elif splitted[i] != "":
                    inside_node = TextNode(splitted[i], text_type)
                    new_nodes.append(inside_node)                
    return new_nodes