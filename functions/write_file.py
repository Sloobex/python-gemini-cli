import os

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

        with open(final_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
