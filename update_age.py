import re
import datetime

# Your birthdate
birthdate = datetime.date(1988, 1, 28)

# Calculate age
today = datetime.date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Read in the README
readme_path = 'README.md'
with open(readme_path, 'r') as file:
    readme_contents = file.read()

# Replace the age
new_readme_contents = re.sub(
    r"I'm Mihai aka Z3r0L1nk, a \d{2}-year-old",
    f"I'm Mihai aka Z3r0L1nk, a {age}-year-old",
    readme_contents
)

# Write out the README
with open(readme_path, 'w') as file:
    file.write(new_readme_contents)
