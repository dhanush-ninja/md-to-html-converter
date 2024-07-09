
# Markdown to HTML Converter using Tailwind CSS

This project is a simple Markdown to HTML converter that utilizes Tailwind CSS for styling.

## Usage

Below is an example of how to use the converter:

```python
markdown_content = """markdown
# Title
## Subtitle
Some text here.
- Item 1
- Item 2
"""

converter = Converter()
converted_html = converter.convert_md_to_html(markdown_content)

# Print or use the converted HTML
print(converted_html)
```

## Features

- Converts Markdown content to HTML
- Uses Tailwind CSS for styling

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Running the Converter

To use the converter, create an instance of the `Converter` class and call the `convert_md_to_html` method with your Markdown content.

## Example

```python
markdown_content = """markdown
# Title
## Subtitle
Some text here.
- Item 1
- Item 2
"""

converter = Converter()
converted_html = converter.convert_md_to_html(markdown_content)

# Print or use the converted HTML
print(converted_html)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
