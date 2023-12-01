
import os

CREATE_FOLDERS = False


def create_folders():
    for i in range(1, 25):
        folder_name = str(i)
        os.makedirs(folder_name, exist_ok=True)
        file_name = f"{folder_name}/aoc_day_{folder_name}.py"
        with open(file_name, "w") as file:
            file.write(f"# Advent of Code Day {folder_name}\n\n")
            file.write("def aocSolver():\n")
            file.write("    pass\n\n")
            file.write("if __name__ == '__main__':\n")
            file.write("    aocSolver()\n")

if __name__ == "__main__":
    if CREATE_FOLDERS:
        create_folders()
