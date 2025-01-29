import os


def add_component(project_name, component_type, component_name):
    """Add a new component (e.g., router, model) to the project."""
    component_path = os.path.join(project_name, "app", component_type)
    if not os.path.exists(component_path):
        print(f"Error: {component_type} directory does not exist in the project.")
        return

    file_name = f"{component_name}.py"
    file_path = os.path.join(component_path, file_name)
    if os.path.exists(file_path):
        print(f"Error: {component_type} '{component_name}' already exists.")
        return

    try:
        with open(file_path, 'w') as f:
            f.write(f"# {component_type.capitalize()} for {component_name}")
        print(f"{component_type.capitalize()} '{component_name}' added successfully!")
    except Exception as e:
        print(f"Error adding component: {e}")
