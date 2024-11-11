#!/bin/bash

# Run the SSL_members Python script to generate HTML content and capture it
html_content=$(python3 SSL_members.py)

# Define the HTML file to update
html_file="index.html"

# Use `awk` to replace the placeholder with the generated content
awk -v html="$html_content" '
    BEGIN {output = ""}
    /<!-- SSL_MEMBER_SECTION -->/ {
        output = output html
        next
    }
    {output = output $0 "\n"}
    END {print output}
' "$html_file" > temp.html && mv temp.html "$html_file"

echo "HTML content inserted successfully into $html_file."
