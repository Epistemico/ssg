import re
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


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    img_alt_links = re.findall(pattern, text)
    return img_alt_links


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links = re.findall(pattern, text)
    return links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if not images and node.text:
            new_nodes.append(node)
            continue
        if not node.text:
            continue
        
        remaining = node.text
        
        for image_alt, image_link in images:
            pattern = f"![{image_alt}]({image_link})"
            sections = remaining.split(pattern, 1)
            
            if len(sections) == 1:
                if remaining:
                    new_nodes.append(TextNode(remaining, TextType.TEXT))
                remaining = ""
                break
            
            before, after = sections

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            remaining = after

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if not links and node.text:
            new_nodes.append(node)
            continue
        if not node.text:
            continue
        
        remaining = node.text
        
        for link_alt, link_address in links:
            pattern = f"[{link_alt}]({link_address})"
            sections = remaining.split(pattern, 1)
            
            if len(sections) == 1:
                if remaining:
                    new_nodes.append(TextNode(remaining, TextType.TEXT))
                remaining = ""
                break
            
            before, after = sections

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_address))
            
            remaining = after

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes
