import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is another text node", TextType.NORMAL, None)
        node2 = TextNode("This is another text node", TextType.NORMAL, None)
        self.assertEqual(node, node2)
    def test_noneq(self):
        node = TextNode("This is another text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a different text node", TextType.BOLD, "www.google.com")
        self.assertNotEqual(node, node2)
    def test_noneq2(self):
        node = TextNode("This is another text node", TextType.NORMAL)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    #Test TextNode to HTMLNode
    def test_TextNode_to_HTMLNode_1(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node_to_html = text_node_to_html_node(node).to_html()
        expected = "<b>This is a bold text node</b>"
        self.assertEqual(node_to_html, expected)
    def test_TextNode_to_HTMLNode_1(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "src/test.jpg")
        node_to_html = text_node_to_html_node(node).to_html()
        expected = '<img src="src/test.jpg" alt="This is an image text node">'
        self.assertEqual(node_to_html, expected)

if __name__ == "__main__":
    unittest.main()