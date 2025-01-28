import shutil
from textnode import *
from inline_markdown import *
from block_markdown import *
import os

def extract_title(markdown):
    lines = markdown.strip().split("\n")
    if lines[0].startswith("# "):
        return lines[0][2:]
    else:
        raise Exception("no title found")
    

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensure the source content directory exists
    if os.path.exists(dir_path_content):
        # Recreate the destination directory
        os.makedirs(dest_dir_path, exist_ok=True)
        
        # List all files and directories in the source directory
        files = os.listdir(dir_path_content)
        for file in files:
            source_path = os.path.join(dir_path_content, file)
            dest_path = os.path.join(dest_dir_path, file)
            
            if os.path.isfile(source_path):  # Check if it's a file
                if file.endswith(".md"):  # Process only Markdown files
                    dest_file_name = file.rsplit(".", 1)[0] + ".html"
                    print(f"Transforming {source_path} to HTML and saving as {os.path.join(dest_dir_path, dest_file_name)}")
                    generate_page(source_path, template_path, os.path.join(dest_dir_path, dest_file_name))
                else:
                    print(f"Skipping non-Markdown file: {source_path}")
            elif os.path.isdir(source_path):  # If it's a directory, recurse into it
                generate_pages_recursive(source_path, template_path, dest_path)