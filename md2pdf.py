import os
import markdown
from fpdf import FPDF

# Get all .md files in current directory
md_files = [f for f in os.listdir('.') if f.endswith('.md')]

# Convert markdown to plain text
text_content = ""
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        text_content += f.read() + "\n\n"

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, text_content.encode('latin1', 'replace').decode('latin1'))
pdf.output("combined.pdf")

print(f"Successfully converted {len(md_files)} .md files to combined.pdf")