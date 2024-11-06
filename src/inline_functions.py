import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            node_text = node.text
            delimiter_count = node_text.count(delimiter)
            if delimiter_count % 2 != 0:
                raise Exception("Invalid markdown syntax, no closing or opening delimiter found")
            if delimiter_count == 0:
                new_nodes.append(node)
                continue
            del_len = len(delimiter)
            delimiter_positions = []
            pos = 0
            while len(delimiter_positions) < delimiter_count:
                pos = node_text.index(delimiter, pos)
                delimiter_positions.append(pos)
                pos += del_len
            texts = []
            start = 0
            for i in range(0, delimiter_count, 2):
                texts.append((node_text[start:delimiter_positions[i]], TextType.NORMAL))
                texts.append((node_text[delimiter_positions[i]+del_len:delimiter_positions[i+1]], text_type))
                start = delimiter_positions[i+1] + del_len
            texts.append((node_text[start:], TextType.NORMAL))
            for text, type in texts:
                if text != "":
                    new_nodes.append(TextNode(text, type))
    #print(f"new nodes: {new_nodes}")
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)