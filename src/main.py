from textnode import *
from htmlnode import *
from inline_functions import *

def main():
    print("TextNode Test")
    textNodeTestObject =  TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    print(textNodeTestObject)

    print("\nHTMLNode Test")
    test_props = {
    "href": "https://www.google.com", 
    "target": "_blank"
    }
    child_html_node = HTMLNode("a", "This is a url html node", None, test_props)
    html_node = HTMLNode("p", "This is a  paragraph html node", child_html_node, None)
    print(html_node)

    print("\nLeafNode Test")
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node)

    print("\nParentNode Test")
    parent_node = ParentNode("p",[LeafNode("b", "Bold text"),
                               LeafNode(None, "Normal text"),
                               LeafNode("i", "italic text"),
                               LeafNode(None, "Normal text")])
    print(parent_node)

    print("\nNested ParentNode Test")
    parent_node_nested = ParentNode("p",[
        ParentNode("b", [LeafNode("a", "Click me!", {"href": "https://www.google.com"})]),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text")])
    print(parent_node_nested)

    print("\nsplit_nodes_delimiter ParentNode Test")
    node = TextNode("*italic phrase* at the start and *italic phrase* in the middle and another *italic phrase* shortly before the end", TextType.NORMAL)
    split_nodes_delimiter([node], "*", TextType.ITALIC)

    print("\nanother split_nodes_delimiter ParentNode Test")
    node = TextNode("Text with a **bold phrase** in the middle and **another one at the end**", TextType.NORMAL)
    split_nodes_delimiter([node], "**", TextType.BOLD)

main()
