from config import MAX_CHARS
from google.genai import types
import os
def get_file_content(working_directory, file_path):
    try:
        base_path = os.path.abspath(working_directory)
        joined_path = os.path.join(base_path, file_path)
        final_path = os.path.normpath(joined_path)
        if os.path.commonpath([base_path, final_path]) != base_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(final_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(final_path, 'r') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {e}"
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specific file at the given path relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)
