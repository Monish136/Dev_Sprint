import markdown


with open('mnma.md', 'r') as md_file:
    md_content = md_file.read()


html_content = markdown.markdown(md_content)


with open('op.html', 'w') as html_file:
    html_file.write(html_content)

print("Markdown file has been converted to HTML.")
