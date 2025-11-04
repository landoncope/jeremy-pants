#!/usr/bin/env python3
"""
Convert the Exploring CS Exam markdown file to a formatted PDF
"""

from weasyprint import HTML, CSS
from markdown import markdown
import os

# Read the markdown file
with open('exploring_cs_exam_version_b.md', 'r') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown(md_content, extensions=['fenced_code', 'tables'])

# Create a complete HTML document with styling
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Exploring Computer Science - Exam (Version B)</title>
    <style>
        @page {{
            size: letter;
            margin: 0.75in;
            @bottom-center {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 10pt;
                color: #666;
            }}
        }}

        body {{
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 11pt;
            line-height: 1.4;
            color: #333;
        }}

        h1 {{
            font-size: 20pt;
            text-align: center;
            margin-bottom: 5px;
            color: #2c3e50;
            page-break-after: avoid;
        }}

        h2 {{
            font-size: 14pt;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #34495e;
            border-bottom: 2px solid #667eea;
            padding-bottom: 5px;
            page-break-after: avoid;
        }}

        h3 {{
            font-size: 12pt;
            margin-top: 15px;
            margin-bottom: 8px;
            color: #555;
            page-break-after: avoid;
        }}

        p {{
            margin: 5px 0;
        }}

        strong {{
            color: #000;
        }}

        ul {{
            margin: 5px 0 15px 0;
            padding-left: 20px;
        }}

        li {{
            margin: 3px 0;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 10pt;
        }}

        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            overflow-x: auto;
            page-break-inside: avoid;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
        }}

        hr {{
            border: none;
            border-top: 2px solid #ddd;
            margin: 20px 0;
        }}

        /* Keep questions together */
        p:has(strong) {{
            page-break-inside: avoid;
            page-break-after: avoid;
        }}

        /* Keep question and answers together */
        p + ul {{
            page-break-before: avoid;
        }}

        /* Answer key section */
        h2:contains("Answer Key") {{
            page-break-before: always;
        }}

        /* Table styling if present */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 10px 0;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}

        th {{
            background-color: #667eea;
            color: white;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Generate the PDF
output_file = 'exploring_cs_exam_version_b.pdf'
HTML(string=full_html).write_pdf(output_file)

print(f"✓ PDF created successfully: {output_file}")
print(f"✓ File size: {os.path.getsize(output_file) / 1024:.1f} KB")
print(f"✓ Ready to print!")
