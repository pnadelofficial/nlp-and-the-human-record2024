import nbformat
import os

def clean_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
        cell.metadata = {}

    nb.metadata = {
        "kernelspec": nb.metadata.get("kernelspec", {}),
        "language_info": nb.metadata.get("language_info", {})
    }

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

def clean_notebooks(input_folder):
    notebooks = [f for f in os.listdir(input_folder) if f.endswith('.ipynb')]
    for notebook in notebooks:
        input_path = os.path.join(input_folder, notebook)
        print(f"Cleaning {notebook}")
        clean_notebook(input_path)

# Usage
input_folder = '../notebooks'
clean_notebooks(input_folder)
