import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, 
                          delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in node.text:
            new_nodes.append(node)
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

def extract_markdown_images(text):
    pattern = r"\!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    if len(old_nodes) == 0:
        return []
    
    new_nodes = []
    node = old_nodes[0]
    remaining_nodes = old_nodes[1:]

    extracted = extract_markdown_images(node.text)
    if not extracted:
        new_nodes.append(node)
        new_nodes.extend(split_nodes_image(remaining_nodes))
        return new_nodes
    
    image_alt, image_link = extracted[0]
    splitted_text = node.text.split(f"![{image_alt}]({image_link})", 1)
    
    if splitted_text[0]:  # Avoid empty nodes
        new_nodes.append(TextNode(splitted_text[0], TextType.TEXT))
    
    new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
    
    if splitted_text[1]:  # Avoid empty nodes
        new_nodes.extend(split_nodes_image([TextNode(splitted_text[1], TextType.TEXT)]))

    new_nodes.extend(split_nodes_image(remaining_nodes))
    return new_nodes

def split_nodes_link(old_nodes):
    if len(old_nodes) == 0:
        return []
    
    new_nodes = []
    node = old_nodes[0]
    remaining_nodes = old_nodes[1:]

    extracted = extract_markdown_links(node.text)
    if not extracted:
        new_nodes.append(node)
        new_nodes.extend(split_nodes_link(remaining_nodes))
        return new_nodes
    
    text_alt, txt_link = extracted[0]
    splitted_text = node.text.split(f"[{text_alt}]({txt_link})", 1)
    
    if splitted_text[0]:  # Avoid empty nodes
        new_nodes.append(TextNode(splitted_text[0], TextType.TEXT))
    
    new_nodes.append(TextNode(text_alt, TextType.LINK, txt_link))
    
    if splitted_text[1]:  # Avoid empty nodes
        new_nodes.extend(split_nodes_link([TextNode(splitted_text[1], TextType.TEXT)]))

    new_nodes.extend(split_nodes_link(remaining_nodes))
    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes_italic = split_nodes_delimiter(nodes_bold, "*", TextType.ITALIC)
    nodes_code = split_nodes_delimiter(nodes_italic, "`", TextType.CODE)
    nodes_img = split_nodes_image(nodes_code)
    nodes_link = split_nodes_link(nodes_img)
    return nodes_link