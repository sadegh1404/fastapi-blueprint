import argparse
from fastapi_blueprint.utils.component import add_component
from fastapi_blueprint.utils.project_structure import create_project_structure


def main():
    parser = argparse.ArgumentParser(description="FastAPI CLI, Helper tool for FastAPI projects")
    subparsers = parser.add_subparsers(dest="command")

    # Command: init
    init_parser = subparsers.add_parser("init", help="Initialize a new FastAPI project")
    init_parser.add_argument("project_name", help="Name of the project")

    # Command: add
    add_parser = subparsers.add_parser("add", help="Add a new component to the project")
    add_parser.add_argument("component_type", choices=["routers", "models", "schemas", "services", "utils"],
                            help="Type of component to add")
    add_parser.add_argument("component_name", help="Name of the component")
    add_parser.add_argument("project_name", help="Name of the existing project")

    args = parser.parse_args()

    if args.command == "init":
        create_project_structure(args.project_name)
    elif args.command == "add":
        add_component(args.project_name, args.component_type, args.component_name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
