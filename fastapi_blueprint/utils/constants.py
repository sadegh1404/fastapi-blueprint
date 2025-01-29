PROJECT_STRUCTURE = {
    "app": ["routers", "models", "schemas", "services", "utils"],
    "": ["requirements.txt", "main.py"],
}

TEMPLATE_CONTENTS = {
    "main.py": """from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to FastAPI CLI generated project!"}
""",
    "requirements.txt": "fastapi\nuvicorn",
}