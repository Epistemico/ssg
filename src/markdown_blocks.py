def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for i in range(len(blocks)):
        if blocks[i]:
            filtered_blocks.append(blocks[i].strip())
    return filtered_blocks
