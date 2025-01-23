from textnode import *
from inline_markdown import *


def markdown_to_blocks(markdown):
    return list(filter(lambda x: x != "", list(map(lambda x: x.strip(), markdown.split("\n\n")))))