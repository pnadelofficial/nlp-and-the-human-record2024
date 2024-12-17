import os
import subprocess

def convert_notebooks(input_folder, output_folder):
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	notebooks = [f for f in os.listdir(input_folder) if f.endswith('.ipynb')]
	for notebook in notebooks:
		input_path = os.path.join(input_folder, notebook)
		output_path = os.path.join(output_folder, notebook.replace('.ipynb', '.html'))
		subprocess.run(['jupyter', 'nbconvert', '--to', 'html', input_path, '--output', output_path])
		print(f"Converted {notebook} to HTML")

input_folder = '../notebooks'
output_folder = '../html'
convert_notebooks(input_folder, output_folder)
