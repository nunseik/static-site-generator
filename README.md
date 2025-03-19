# Markdown to HTML Static Site Generator

A simple and lightweight static site generator that converts Markdown files to HTML pages using a customizable template.

## Overview

This project allows you to:
- Write content in Markdown format
- Convert Markdown content to HTML using a customizable template
- Support for inline Markdown formatting (bold, italic, code, links, images)
- Support for block-level Markdown elements (paragraphs, headings, code blocks, quotes, ordered and unordered lists)
- Automatically generate a static website with proper HTML structure

## File Structure

The project expects the following directory structure:

```
project_root/
├── content/         # Your Markdown content files
├── static/          # Static assets (CSS, images, JavaScript, etc.)
├── public/          # Generated website (created automatically)
├── template.html    # HTML template for generated pages
└── src/             # Source code
    ├── block_markdown.py
    ├── copy_to_public.py
    ├── generate_page.py
    ├── htmlnode.py
    ├── inline_markdown.py
    ├── main.py
    └── textnode.py
```

## Setup Instructions

1. Clone or download this repository
2. Ensure you have Python 3 installed
3. Create the required directories if they don't exist:
   ```
   mkdir -p content static
   ```
4. The template.html file is already provided in the root directory

## How to Use

### Creating Content

1. Create Markdown (.md) files in the `content/` directory
2. Each Markdown file should start with a level 1 heading (e.g., `# Page Title`) which will be used as the page title
3. You can organize content in subdirectories within the `content/` directory, and the structure will be preserved in the output

### Adding Static Files

Place any static files (CSS, JavaScript, images, etc.) in the `static/` directory. They will be copied to the `public/` directory when the site is generated.

### Template Format

The project includes a template.html file in the root directory with the following placeholders:
- `{{ Title }}` - Will be replaced with the title extracted from the Markdown file
- `{{ Content }}` - Will be replaced with the HTML content generated from the Markdown

The provided template.html:
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> {{ Title }} </title>
    <link href="/index.css" rel="stylesheet">
</head>

<body>
    <article>
        {{ Content }}
    </article>
</body>

</html>
```

This is a simple, clean template that loads an index.css stylesheet from the static directory and renders your content within an article tag.

### Building and Viewing the Site

The easiest way to build and view the site is to use the provided shell script at the root directory:

```bash
sh main.sh
```

This script will:
1. Run `python3 src/main.py` to generate the site
2. Start a local web server with `python3 -m http.server 8888`
3. You can then view your site by opening a web browser and navigating to `http://localhost:8888`

If you prefer to run the commands separately, you can:

```bash
# Generate the site
python3 src/main.py

# Start a local web server
cd public && python3 -m http.server 8888
```

## Supported Markdown Features

### Inline Elements
- **Bold text** with double asterisks: `**bold**`
- *Italic text* with single asterisks: `*italic*`
- `Code` with backticks: `` `code` ``
- [Links](https://example.com) with `[text](url)` syntax
- Images with `![alt text](image_url)` syntax

### Block Elements
- Paragraphs (separated by blank lines)
- Headings (levels 1-6) with `#` syntax: `# Heading 1`, `## Heading 2`, etc.
- Code blocks with triple backticks: ` ```code block``` `
- Blockquotes with `>` syntax
- Ordered lists with `1. `, `2. `, etc.
- Unordered lists with `* ` or `- ` syntax

## Project Structure

- `textnode.py`: Defines the TextNode class and text node types
- `htmlnode.py`: Defines HTML node classes for building the HTML tree
- `inline_markdown.py`: Handles inline Markdown parsing (bold, italic, links, etc.)
- `block_markdown.py`: Handles block-level Markdown parsing (paragraphs, headings, etc.)
- `generate_page.py`: Converts Markdown files to HTML using the template
- `copy_to_public.py`: Handles copying static files to the public directory
- `main.py`: Main script that orchestrates the site generation process

## Customization

You can customize this static site generator by:
1. Modifying the `template.html` file to change the overall site structure
2. Adding CSS files in the `static/` directory
3. Extending the Markdown parsers to support additional Markdown features

## Limitations and Room for Improvement

This static site generator is intentionally simple and has several limitations that could be addressed in future improvements:

1. **Nested Formatting**: The current implementation doesn't properly handle nested Markdown formatting such as `**bold and *italic* text**` or other combinations of inline elements.

2. **Advanced Markdown Features**: No built-in support for:
   - Tables
   - Footnotes
   - Task lists
   - Definition lists
   - Strikethrough
   - Syntax highlighting in code blocks

3. **Performance**: The parser uses a simple approach and may not be optimized for large documents or sites with many pages.

4. **Error Handling**: Limited error reporting for malformed Markdown.

5. **Template System**: The template system is very basic and only supports two placeholders (`{{ Title }}` and `{{ Content }}`).

### Potential Enhancements

If you're interested in extending this project, here are some improvement ideas:

1. Implement support for nested formatting using a proper parsing algorithm
2. Add support for additional Markdown features
3. Improve error handling and reporting
4. Enhance the template system to support more variables, partials, and includes
5. Add support for front matter to include metadata in Markdown files
6. Implement a watch mode that automatically rebuilds the site when files change
7. Add a configuration file to customize the build process
