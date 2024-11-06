import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    test_props = {
    "href": "https://www.google.com", 
    "target": "_blank"
    }
    def test_eq(self):
        node = HTMLNode("a", "This is a url html node", None, self.test_props)
        node2 = HTMLNode("a", "This is a url html node", None, self.test_props)
        self.assertEqual(node, node2)
    def test_eq2(self):
        child_node = HTMLNode("a", "This is a url html node", None, self.test_props)
        node = HTMLNode("p", "This is a paragraph html node", child_node, None)
        node2 = HTMLNode("p", "This is a paragraph html node", child_node, None)
        self.assertEqual(node, node2)
    def test_noneq(self):
        node = HTMLNode(None, "This is pure text", None, None)
        node2 = HTMLNode("p", "This is pure text", None, None)
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        expected = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode("a", "This is a url html node", None, self.test_props)
        self.assertEqual(node.props_to_html(), expected)

    def test_leafnode_to_html(self):
        expected = "<p>This is a paragraph of text.</p>"
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), expected)
    def test_leafnode_to_html2(self):
        expected = '<a href="https://www.google.com">Click me!</a>'
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), expected)
        
    def test_parentnode_to_html(self):
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode("p",[LeafNode("b", "Bold text"),
                               LeafNode(None, "Normal text"),
                               LeafNode("i", "italic text"),
                               LeafNode(None, "Normal text")])
        self.assertEqual(node.to_html(), expected)

    def test_parentnode_to_html_nested(self):
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode("p",[LeafNode("b", "Bold text"),
                               LeafNode(None, "Normal text"),
                               LeafNode("i", "italic text"),
                               LeafNode(None, "Normal text")])
        self.assertEqual(node.to_html(), expected)
    

if __name__ == "__main__":
    unittest.main()