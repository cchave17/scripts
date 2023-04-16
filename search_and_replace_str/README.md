# Directory String Search and Replace Script

This Python script searches for a specified string in all text files within a given directory and its subdirectories and replaces it with another string. It also allows you to exclude specific directories or files from the search.

## Usage

1. Install Python 3 on your system if you haven't already.
2. Save the script as `dir_str_search_replace.py` in a directory of your choice.
3. Open a terminal/command prompt and navigate to the directory where the script is located.
4. Run the script with the following command:

```bash
python dir_str_search_replace.py <search_string> <replace_string> <directory_path> --ignore <directories_or_files_to_ignore>
```

Replace `<search_string>`, `<replace_string>`, `<directory_path>`, and `<directories_or_files_to_ignore>` with the appropriate values.

### Arguments

- `search_string`: The string you want to search for in the text files.
- `replace_string`: The string you want to replace the `search_string` with.
- `directory_path`: The path to the directory containing the text files you want to process.
- `--ignore`: (Optional) A list of directories or files to ignore during the search and replace process. You can specify any number of directories or files to ignore by separating them with spaces.

### Example

```bash
python dir_str_search_replace.py "search_this" "replace_with_this" "/path/to/directory" --ignore ".github" "venv" "another_directory"
```

This command searches for the string `search_this` in all text files within the `/path/to/directory` directory and replaces it with the string `replace_with_this`. It ignores any files in the `.github`, `venv`, and `another_directory` directories.

## Notes

- This script only processes files with UTF-8 encoding.
- Before applying any replacements, the script shows a list of all found instances and prompts you to confirm whether you want to proceed with the replacements.
- The script will display the file name and line number for each instance where a replacement is made.
- In case a file cannot be processed due to encoding issues, the script will skip the file without raising any warnings.
- You can specify any number of directories or files to ignore by separating them with spaces after the `--ignore` flag.
