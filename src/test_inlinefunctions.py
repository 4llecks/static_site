import unittest

from textnode import *
from inline_functions import *

print("\nsplit_nodes_delimiter ParentNode Test")
node = TextNode("*italic phrase* at the start and *italic phrase* in the middle and another *italic phrase* shortly before the end", TextType.NORMAL)
split_nodes_delimiter([node], "*", TextType.ITALIC)

print("\nanother split_nodes_delimiter ParentNode Test")
node = TextNode("Text with a **bold phrase** in the middle and **another one at the end**", TextType.NORMAL)
split_nodes_delimiter([node], "**", TextType.BOLD)

print("\nanother split_nodes_delimiter ParentNode Test")
node = TextNode("This is `code` text", TextType.NORMAL)
split_nodes_delimiter([node], "`", TextType.CODE)

print("\nanother split_nodes_delimiter ParentNode Test")
node = TextNode("Text with a **bold phrase****and another bold phrase** right after it", TextType.NORMAL)
split_nodes_delimiter([node], "`", TextType.BOLD)

class TestTextNode(unittest.TestCase):
    # TextNode to HTMLNode Tests
    def test_TextNode_to_HTMLNode_1(self):
        node = TextNode("Text with a *an incorecct syntax**", TextType.NORMAL)
        self.assertRaises(Exception, split_nodes_delimiter,[[node], "**", TextType.BOLD])

    # Testing image and link extraction from markdown
    def test_extract_md_img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(expected, extract_markdown_images(text))
    def test_extract_md_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(expected, extract_markdown_links(text))