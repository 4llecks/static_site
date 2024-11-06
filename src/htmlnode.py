class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        html_str = ""
        for prop in self.props:
            html_str += f' {prop}="{self.props[prop]}"'
        return html_str

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}; html props: {self.props_to_html()})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        #self.tag = tag
        #self.value = value
        #self.props = props
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})\n html string: {self.to_html()}"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        #self.tag = tag
        #self.children = children
        #self.props = props
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("Object of class ParentNode needs children")
        html_result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_result += child.to_html()
        html_result += f"</{self.tag}>"
        return html_result
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})\n html string: {self.to_html()}"
    