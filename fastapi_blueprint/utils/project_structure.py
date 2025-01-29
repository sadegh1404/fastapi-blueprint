import os
from fastapi_blueprint.utils.constants import PROJECT_STRUCTURE, TEMPLATE_CONTENTS


def create_project_structure(project_name):
    """Create the project structure."""
    try:
        if os.path.exists(project_name):
            print(f"Error: Project '{project_name}' already exists.")
            return
        os.makedirs(project_name)

        for folder, subfolders in PROJECT_STRUCTURE.items():
            for subfolder in subfolders:
                if subfolder.endswith('.py') or subfolder.endswith('.txt'):
                    file_path = os.path.join(project_name, subfolder)
                    with open(file_path, 'w') as f:
                        f.write(TEMPLATE_CONTENTS.get(subfolder, ""))
                else:
                    folder_path = os.path.join(project_name, folder, subfolder)
                    os.makedirs(folder_path, exist_ok=True)
                    # make init file for each folder
                    init_file_path = os.path.join(folder_path, '__init__.py')
                    with open(init_file_path, 'w') as f:
                        f.write(f"# {subfolder.capitalize()} package for the project")

        print(f"Project '{project_name}' created successfully!")
    except Exception as e:
        print(f"Error creating project: {e}")
