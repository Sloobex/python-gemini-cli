import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        base_path = os.path.abspath(working_directory)
        joined_path = os.path.join(base_path, file_path)
        final_path = os.path.normpath(joined_path)

        if os.path.commonpath([base_path, final_path]) != base_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(final_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        file_directory = os.path.dirname(final_path)
        os.makedirs(file_directory, exist_ok=True)

        with open(final_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specific file at the given path relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string content to write into the file.",
            ),
        },
    ),
)
