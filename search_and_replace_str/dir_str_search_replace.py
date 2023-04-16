from pathlib import Path
import re
import argparse
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def should_ignore(file_path, ignore_list):
    for item in ignore_list:
        if item.lower() in str(file_path).lower():
            return True
    return False


def find_replacements(file_path, search_string, replace_string):
    replacements = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        return replacements

    search_string_pattern = re.compile(search_string, re.IGNORECASE)
    for index, line in enumerate(lines):
        if search_string_pattern.search(line):
            replacements.append(
                (index + 1, line.rstrip(), search_string_pattern.sub(replace_string, line.rstrip())))

    return replacements


def apply_replacements(file_path, replacements, search_string, replace_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    search_string_pattern = re.compile(search_string, re.IGNORECASE)
    for index, line in enumerate(lines):
        if any(index + 1 == replacement[0] for replacement in replacements):
            lines[index] = search_string_pattern.sub(replace_string, line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def process_files(dir_path, search_string, replace_string, ignore_list):
    all_replacements = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = Path(root) / file
            if should_ignore(file_path, ignore_list):
                continue
            replacements = find_replacements(
                file_path, search_string, replace_string)
            if replacements:
                all_replacements.append((file_path, replacements))

    if not all_replacements:
        print("No replacements found.")
        return

    print("\nFound replacements:")
    for file_path, replacements in all_replacements:
        for line_number, original_line, replaced_line in replacements:
            print(
                f"In {file_path}: Line {line_number}\nOriginal: {original_line}\nReplaced: {replaced_line}\n")

    user_input = input("Do you want to apply these replacements? (y/n): ")
    if user_input.lower() == 'y':
        for file_path, replacements in all_replacements:
            apply_replacements(file_path, replacements,
                               search_string, replace_string)
        print("Replacements applied.")
    else:
        print("Replacements not applied.")


def main():
    parser = argparse.ArgumentParser(description='Search and replace strings in files within a directory.')
    parser.add_argument('search_string', help='String to search for')
    parser.add_argument('replace_string', help='String to replace with')
    parser.add_argument('dir_path', help='Directory path to process files')
    parser.add_argument('--ignore', nargs='*', default=[], help='List of directories or files to ignore')

    args = parser.parse_args()

    if not os.path.isdir(args.dir_path):
        print(f"Error: {args.dir_path} is not a valid directory.")
        sys.exit(1)

    process_files(args.dir_path, args.search_string, args.replace_string, args.ignore)



if __name__ == '__main__':
    main()
