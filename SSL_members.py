import pandas as pd

# Load Excel data
df = pd.read_excel('SSL_members.xlsx')

# Create HTML content for the members section only
html_content = """
<div class="items style1 medium">
"""

# Generate HTML for each member
for _, row in df.iterrows():
    name = row['Name']
    subtitle = row['Subtitle']
    grade = row['Grade']
    
    # Start member section
    html_content += f"""
    <section>
        <h3>{name}</h3>
        <p>{subtitle}</p>
        <h2>{grade}</h2>
    </section>
    """

# Close the items div
html_content += """
</div>
"""

# Output to command line
print(html_content)
