import os
def get_files_info(working_directory, directory="."):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path,directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        emptylist = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir,item)
            item_size = os.path.getsize(item_path)
            is_it = os.path.isdir(item_path)
            emptylist.append(f"- {item}: file_size={item_size} bytes, is_dir={is_it}")
        return "\n".join(emptylist)
    except Exception as e:
        return f"Error: {e}"
