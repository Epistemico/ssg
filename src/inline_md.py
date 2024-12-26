from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in ("`", "*", "**"):
            raise ValueError("Invalid markdown syntax")
        else:
            node_text = node.text.split(delimiter)
            for substr in node_text:
                if substr == "":
                    continue
                if delimiter in ("*", "**") and (substr.startswith(" ") or substr.endswith(" ")):
                    new_nodes.append(TextNode(substr, node.text_type))
                elif f"{delimiter}{substr}{delimiter}" in node.text:
                    new_nodes.append(TextNode(substr, text_type))
                else:
                    new_nodes.append(TextNode(substr, node.text_type))

    return new_nodes
