import os
import sys

TARGET_ROOT = "Beginner Study Guide"
TEMPLATE_PATH = "algorithm_template.md"


def load_template():
    with open(TEMPLATE_PATH, "r") as f:
        return f.read()


def create_problem_directory(name, link):
    dir_path = os.path.join(TARGET_ROOT, name)
    os.makedirs(dir_path, exist_ok=True)

    # Create code.py
    open(os.path.join(dir_path, "code.py"), "w").close()

    # Create README.md with replaced link
    template = load_template().replace("[Link]: https://leetcode.com/problems/", f"[Link]: {link}")
    with open(os.path.join(dir_path, "README.md"), "w") as f:
        f.write(template)

    print(f"\033[34mSuccessfully created a new Leetcode problem:\033[3m \'{dir_path}\' \033[0m")


def main():
    if len(sys.argv) >= 2:
        problem_name = sys.argv[1]
        link = sys.argv[2] if len(sys.argv) >= 3 else "https://leetcode.com/problems/"
    else:
        problem_name = input("Enter problem name (e.g., '412. Fizzbuzz'): ").strip()
        link = input("Enter Leetcode link (or press Enter for default): ").strip() or "https://leetcode.com/problems/"

    create_problem_directory(problem_name, link)


if __name__ == "__main__":
    main()