import os
import re

# Directory containing the playthrough files
playthroughs_dir = "playthroughs"

# Dictionary to store hero counts
hero_counts = {}

# Pattern to match place lines with hero0
pattern = r'place\s+(\w+)\s+hero0'

# Check if directory exists
if not os.path.exists(playthroughs_dir):
    print(f"Directory {playthroughs_dir} does not exist")
else:
    # Process each file in the directory
    file_count = 0
    for filename in os.listdir(playthroughs_dir):
        if filename.endswith('.btd6'):
            file_path = os.path.join(playthroughs_dir, filename)
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    # Find all matches of place lines with hero0
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    for hero in matches:
                        # Normalize hero name (first letter uppercase, rest lowercase)
                        hero = hero.capitalize()
                        hero_counts[hero] = hero_counts.get(hero, 0) + 1
                file_count += 1
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    
    print(f"Analyzed {file_count} files")
    print("Hero counts:")
    for hero, count in sorted(hero_counts.items()):
        print(f"{hero}: {count}")