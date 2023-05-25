from typing import List


class FileProcessor:
    def __init__(self, input_files: List[str], output_file: str):
        self.input_files = input_files
        self.output_file = output_file

    def process_files(self):
        with open(self.output_file, "w") as out_file:
            for input_file in self.input_files[:-1]:
                with open(input_file, "r") as in_file:
                    for line in in_file:
                        out_file.write(line.upper())

                out_file.write("\\n")

            with open(self.input_files[-1], "r") as last_file:
                contents = last_file.read()
                for word in contents.split():
                    try:
                        with open(word + ".txt", "r+") as in_file:
                            text = in_file.read()
                            in_file.seek(0)
                            in_file.write(text.upper())
                            in_file.truncate()
                    except FileNotFoundError:
                        pass


if __name__ == "__main__":
    input_files = ["file1.txt", "file2.txt", "file3.txt"]
    output_file = "output.txt"

    processor = FileProcessor(input_files, output_file)
    processor.process_files()
