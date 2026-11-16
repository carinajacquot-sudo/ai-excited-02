import os
import shutil

def main():
    os.makedirs("/output", exist_ok=True)
    src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copy(src_path, "/output/entry.png")
    print("Copied entry.png to /output/entry.png")

if __name__ == "__main__":
    main()
