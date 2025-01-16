import os
from utils.constants import PROJECT_STRUCTURE, TEMPLATE_CONTENTS


def create_project_structure(project_name):
    """Create the project structure."""
    try:
        os.makedirs(project_name, exist_ok=True)

        for folder, subfolders in PROJECT_STRUCTURE.items():
            for subfolder in subfolders:
                if subfolder.endswith('.py') or subfolder.endswith('.txt'):
                    file_path = os.path.join(project_name, subfolder)
                    with open(file_path, 'w') as f:
                        f.write(TEMPLATE_CONTENTS.get(subfolder, ""))
                else:
                    folder_path = os.path.join(project_name, folder, subfolder)
                    os.makedirs(folder_path, exist_ok=True)

        print(f"Project '{project_name}' created successfully!")
    except Exception as e:
        print(f"Error creating project: {e}")
