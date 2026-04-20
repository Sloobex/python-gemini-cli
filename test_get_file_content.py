from functions.get_file_content import get_file_content
from config import MAX_CHARS
result = get_file_content("calculator", "lorem.txt")
print(len(result))
print("--- END OF THE FILE ---")
print(result[-100:]) 
print("------------------")
expected_suffix = f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'

if result.endswith(expected_suffix):
    print("✅IT WORKS!")
else:
    print("❌IT DOESNT WORK")
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))
