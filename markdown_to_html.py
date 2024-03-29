import sys
import re

def convert_markdown_to_html(input_file, output_file=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        # Convert bold text
        markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)
        # Convert italic text
        markdown_text = re.sub(r'_([^_]+)_', r'<i>\1</i>', markdown_text)
        # Convert monospaced text
        markdown_text = re.sub(r'`([^`]+)`', r'<tt>\1</tt>', markdown_text)
        # Convert preformatted text
        markdown_text = re.sub(r'```(.*?)```', r'<pre>\1</pre>', markdown_text, flags=re.DOTALL)
        # Convert paragraphs
        markdown_text = re.sub(r'(?<!\n)\n(?!\n)', r'</p>\n<p>', markdown_text, flags=re.DOTALL)
        
        html_text = f'<p>{markdown_text}</p>'

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_text)
        else:
            print(html_text)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markdown_to_html.py <input_file> [--out <output_file>]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = None

    if len(sys.argv) > 2 and sys.argv[2] == "--out" and len(sys.argv) > 3:
        output_file = sys.argv[3]

    convert_markdown_to_html(input_file, output_file)
