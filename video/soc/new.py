import os

# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Read the list of team pairs from list.txt in the current directory
with open(os.path.join(current_directory, 'list.txt'), 'r') as f:
    team_pairs = [line.strip() for line in f.readlines()]

# Specify the output folder in the current directory
output_folder = os.path.join(current_directory, 'tap')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through team pairs and create modified HTML files
for team_pair in team_pairs:
    team_a, team_b = team_pair.split(' vs ')
    
    # Remove periods and convert to lowercase for file naming
    team_a_filename = team_a.replace('.', '').lower().replace(' ', '-')
    team_b_filename = team_b.replace('.', '').lower().replace(' ', '-')

    # Generate the correct file names based on team names
    file_names = [f'video-{team_a_filename}-vs-{team_b_filename}-hs-football-liv-tvs-{i:02d}.html' for i in range(1, 5)]
    
    # Construct the full paths to the original HTML template files
    template_file_paths = [os.path.join(current_directory, f'video-a-v-b-hs-football-liv-tvs-{i:02d}.html') for i in range(1, 5)]

    # Read the HTML template files
    html_templates = []
    for template_file_path in template_file_paths:
        with open(template_file_path, 'r', encoding='utf-8') as template_file:
            html_templates.append(template_file.read())

    # Loop through each file name and template
    for file_name, html_template in zip(file_names, html_templates):
        # Create the <img> tag with the correct team names
        img_tag = f'<img src="/static/images/d4fdf41d5g.png" onerror=window.location="https://watch.liveespn.com/soccer/?id={team_a.replace(" ", "+")}+vs+{team_b.replace(" ", "+")}">\n'
        
        # Replace specific team names in the HTML template
        modified_html = html_template.replace('XXX', team_a).replace('YYY', team_b)
        
        # Add the <img> tag to the beginning of the modified HTML
        modified_html = img_tag + modified_html
        
        # Write the modified HTML to the output file in the output folder
        with open(os.path.join(output_folder, file_name), 'w', encoding='utf-8') as output_file:
            output_file.write(modified_html)

        print(f"HTML file '{file_name}' created for {team_a} vs {team_b}.")
