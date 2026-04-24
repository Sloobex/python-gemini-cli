import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        base_path = os.path.abspath(working_directory)
        joined_path = os.path.join(base_path, file_path)
        final_path = os.path.normpath(joined_path)

        if os.path.commonpath([base_path, final_path]) != base_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(final_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python3", final_path]
        if args is not None:
            command.extend(args)
        result = subprocess.run(command, cwd = base_path,capture_output=True,text=True,timeout=30)
        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        if result.stdout =="" and result.stderr == "":
            output += "No output produced/n"
        if result.stdout != "":
            output += f"STDOUT:\n{result.stdout}\n"
        if result.stderr != "":
            output += f"STDERR:\n{result.stderr}\n"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file at the specified path relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="Optional list of command-line arguments to pass to the script.",
            ),
        },
    ),
)
