import os
import re

# Define the directory to search (current directory)
directory = '.'

# Define the regex pattern to match any tags with both aria-label and title attributes containing spans with the class "material-icons"
pattern = re.compile(
    r'<(\w+)[^>]*\s(?=[^>]*\saria-label="[^"]*")(?=[^>]*\stitle="[^"]*")[^>]*>\s*'
    r'(<span[^>]*class="material-icons"[^>]*>(.*?)</span>)\s*</\1>',
    re.MULTILINE | re.DOTALL
)

# Function to process each file
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Function to replace matches
    def replace_match(match):
        tag = match.group(1)
        span_tag = match.group(2)

        # Extract the title and i18n-title attributes from the parent tag
        title_match = re.search(r'title="([^"]*)"', match.group(0))
        i18n_title_match = re.search(r'i18n-title', match.group(0))

        if not title_match:
            return match.group(0)

        title_attr = title_match.group(0)
        i18n_title_attr = 'i18n-title' if i18n_title_match else ''

        # Add the title and i18n-title attributes to the existing span tag
        new_span_tag = re.sub(
            r'(<span[^>]*class="material-icons"[^>]*)(>)',
            rf'\1 {title_attr} {i18n_title_attr} \2',
            span_tag
        )

        # Remove title and i18n-title attributes from the parent tag
        new_tag = re.sub(r'\s(title="[^"]*")', '', match.group(0))
        new_tag = re.sub(r'\s(i18n-title)', '', new_tag)

        # Replace the span tag in the new parent tag
        new_tag = re.sub(re.escape(span_tag), new_span_tag, new_tag)

        return new_tag

    # Replace all matches in the content
    new_content = pattern.sub(replace_match, content)

    # Write the modified content back to the file only if changes were made
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)

# Function to walk through the directory and process all files
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.htm'):
                process_file(os.path.join(root, file))

# Run the script
process_directory(directory)
