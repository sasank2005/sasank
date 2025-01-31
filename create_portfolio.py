import os
from datetime import datetime

def create_portfolio(name, profession, about, experience, projects, skills, contact):
    """Creates a text-based personal portfolio."""

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    portfolio_content = f"""
    --------------------------------------------------
    Personal Portfolio - {name}
    --------------------------------------------------
    Generated on: {timestamp}

    About Me:
    {about}

    Profession:
    {profession}

    Experience:
    """
    for job in experience:
        portfolio_content += f"- {job['title']} at {job['company']} ({job['years']})\n"

    portfolio_content += "\nProjects:\n"
    for project in projects:
        portfolio_content += f"- {project['name']}: {project['description']}\n"

    portfolio_content += "\nSkills:\n"
    for skill in skills:
        portfolio_content += f"- {skill}\n"

    portfolio_content += f"""
    
    Contact:
    {contact}

    --------------------------------------------------
    """

    # Save the portfolio to a text file
    filename = f"portfolio_{name.replace(' ', '_').lower()}.txt" # Create filename
    try:
        with open(filename, "w") as file:
            file.write(portfolio_content)
        print(f"Portfolio created successfully as {filename}")
    except Exception as e:
        print(f"Error creating portfolio file: {e}")



# Example usage:
name = "Your Name"
profession = "Software Engineer"
about = "A passionate software engineer with experience in developing web applications and a strong interest in AI."
experience = [
    {"title": "Software Developer", "company": "Tech Co.", "years": "2021-Present"},
    {"title": "Intern", "company": "Startup Inc.", "years": "2020-2021"},
]
projects = [
    {"name": "Project Alpha", "description": "A web application for managing tasks."},
    {"name": "Project Beta", "description": "A mobile app for social networking."},
]
skills = ["Python", "Java", "JavaScript", "SQL", "Agile Development"]
contact = "email@example.com | linkedin.com/in/yourprofile"

create_portfolio(name, profession, about, experience, projects, skills, contact)

# To view the portfolio:
# On most systems, you can then open the generated .txt file in a text editor.
# For example, on Linux/macOS:
# os.system(f"cat portfolio_{name.replace(' ', '_').lower()}.txt")  # Print to console
# or open it with a text editor:
# os.system(f"gedit portfolio_{name.replace(' ', '_').lower()}.txt") # Example using gedit
# os.system(f"nano portfolio_{name.replace(' ', '_').lower()}.txt") # Example using nano
# On Windows:
# os.startfile(f"portfolio_{name.replace(' ', '_').lower()}.txt") # Opens with default text editor