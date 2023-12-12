import os
import shutil
from typing import List
import glob
import subprocess
import re
import os
import subprocess
import glob

URL = "http://grifouniou.free.fr/sosecu2/"
SITE_PATH = "/home/antgib/Documents/Codes/grifouniou.free.fr/sosecu2"


def get_website(site_path: str) -> None:
    subprocess.run(
        [
            "wget",
            "-r",
            "-np",
            "--cut-dirs=1",
            URL,
            os.path.basename(os.path.basename(site_path)),
        ]
    )


def convert_html_to_markdown(site_path: str) -> None:
    html_files = glob.glob(os.path.join(site_path, "**/*.htm"), recursive=True)
    for file in html_files:
        file_name = os.path.basename(file)
        subprocess.run(
            [
                "iconv",
                "-f",
                "ISO-8859-1//TRANSLIT",
                "-t",
                "UTF-8//TRANSLIT",
                file,
                "-o",
                file,
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )
        markdown_file_path = os.path.join(
            site_path, f"{os.path.splitext(file_name)[0]}.md"
        )
        subprocess.run(
            [
                "pandoc",
                "-f",
                "html",
                "-t",
                "markdown",
                "--wrap=none",
                "--no-highlight",
                "-o",
                markdown_file_path,
                file,
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )
        os.remove(file)


def create_directories(site_path: str) -> None:
    directories = ["images", "videos", "documents", "others"]
    for directory in directories:
        os.makedirs(os.path.join(site_path, "assets", directory), exist_ok=True)


def move_file_safely(source: str, destination: str) -> None:
    try:
        shutil.move(source, destination)
    except shutil.Error as e:
        print(f"An error occurred while moving the file: {e}")
    except OSError as e:
        print(f"OS error occurred while moving the file: {e}")


def move_files_to_directories(site_path: str) -> None:
    file_types = {
        "images": ["*.jpg", "*.jpeg", "*.png", "*.gif"],
        "videos": ["*.mov", "*.mp4", "*.avi", "*.mkv"],
        "documents": ["*.pdf", "*.doc", "*.ppt", "*.docx", "*.txt", "*.xml"],
    }

    for file_type, extensions in file_types.items():
        for ext in extensions:
            files = glob.glob(os.path.join(site_path, "**", ext), recursive=True)
            for file in files:
                base_dir = os.path.basename(os.path.dirname(file))
                destination = os.path.join(site_path, "assets", file_type, base_dir)
                os.makedirs(destination, exist_ok=True)
                move_file_safely(file, destination)


def update_path(site_path: str, pattern: str):
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        for result in re.finditer(
            r"\!\[([^/]*)\]\(([^)]*(\.jpg|\.jpeg|\.png|\.gif))\)", content
        ):
            new_destination = os.path.join(
                os.path.basename(os.path.dirname(result.group(2))),
                os.path.basename(result.group(2)),
            )
            full_new = f"assets/images/articles/{new_destination}"
            replacement = f"![{result.group(1)}]({full_new})"
            content = content.replace(result.group(0), replacement)
        with open(file, "w") as f:
            f.write(content)


def update_paths(site_path: str):
    # Image
    update_path(site_path, r"\!\[([^/]*)\]\(([^)]*(\.jpg|\.jpeg|\.png|\.gif))\)")
    # Videos
    update_path(site_path, r"\!\[([^/]*)\]\(([^)]*(\.mov|\.mp4|\.avi|\.mkv))\)")
    # Documents
    update_path(site_path, r"\!\[([^/]*)\]\(([^)]*(\.pdf|\.doc|\.docx|\.txt|\.xml))\)")


def remove_pipes(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = content.replace("|", "")
        with open(file, "w") as f:
            f.write(updated_content)


def remove_lines_from_tabular(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            lines = f.readlines()
        updated_lines = [line for line in lines if not re.match(r"\+(\-)+\+", line)]
        with open(file, "w") as f:
            f.writelines(updated_lines)


def remove_html_tags(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = re.sub(r"<[^>]*>", "", content)
        with open(file, "w") as f:
            f.write(updated_content)


def remove_curly_braces(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = re.sub(r"{[^}]*}", "", content)
        with open(file, "w") as f:
            f.write(updated_content)


def remove_consecutive_whitespaces(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = re.sub(r" {2,}", " ", content)
        with open(file, "w") as f:
            f.write(updated_content)


def remove_empty_lines(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            lines = f.readlines()

        # Removing consecutive blank lines
        updated_lines = []
        previous_line_empty = False
        for line in lines:
            line_stripped = line.strip()
            if not line_stripped and not previous_line_empty:
                updated_lines.append(line)
                previous_line_empty = True
            elif line_stripped:
                updated_lines.append(line)
                previous_line_empty = False

        with open(file, "w") as f:
            f.writelines(updated_lines)


def remove_haut_de_page_lines(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            lines = f.readlines()
        updated_lines = [line for line in lines if "Haut de page" not in line]
        with open(file, "w") as f:
            f.writelines(updated_lines)


def convert_single_quote(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = content.replace("\\'", "'")
        with open(file, "w") as f:
            f.write(updated_content)


def convert_double_quote(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = content.replace('\\"', '"')
        with open(file, "w") as f:
            f.write(updated_content)


def two_nested_brackets_to_subtitle(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = re.sub(r"\[\[\s*([^]]+)\]\]", "## \g<1>", content)
        with open(file, "w") as f:
            f.write(updated_content)


def one_nested_brackets_to_subtitle(site_path: str) -> None:
    markdown_files = glob.glob(os.path.join(site_path, "**/*.md"), recursive=True)
    for file in markdown_files:
        with open(file, "r") as f:
            content = f.read()
        updated_content = re.sub(r"\[\s*([^]]+)]\s*$", "# \g<1>", content)
        with open(file, "w") as f:
            f.write(updated_content)


def clean_up_markdown(site_path: str) -> None:
    print("Removing pipes...")
    remove_pipes(site_path)
    print("Removing lines from tabular...")
    remove_lines_from_tabular(site_path)
    print("Removing HTML tags...")
    remove_html_tags(site_path)
    print("Removing curly braces...")
    remove_curly_braces(site_path)
    print("Removing consecutive whitespaces...")
    remove_consecutive_whitespaces(site_path)
    print("Removing empty lines...")
    remove_empty_lines(site_path)
    print("Removing haut de page lines...")
    remove_haut_de_page_lines(site_path)
    print("Converting single quote...")
    convert_single_quote(site_path)
    print("Converting double quote...")
    convert_double_quote(site_path)
    print("Converting one nested brackets to subtitle...")
    one_nested_brackets_to_subtitle(site_path)
    print("Converting two nested brackets to subtitle...")
    two_nested_brackets_to_subtitle(site_path)


def main():
    # print("Getting website...")
    # get_website(SITE_PATH)
    print("Converting HTML to Markdown...")
    convert_html_to_markdown(SITE_PATH)
    print("Creating directories...")
    create_directories(SITE_PATH)
    print("Moving files to directories...")
    move_files_to_directories(SITE_PATH)
    print("Updating paths...")
    update_paths(SITE_PATH)
    print("Cleaning up markdown...")
    clean_up_markdown(SITE_PATH)


if __name__ == "__main__":
    main()
