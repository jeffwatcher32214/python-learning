import gzip
import shutil

def compress_file(source, destination):
    with open(source, 'rb') as f_in:
        with gzip.open(destination, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Compressed '{source}' ➜ '{destination}'")

def decompress_file(source, destination):
    with gzip.open(source, 'rb') as f_in:
        with open(destination, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Decompressed '{source}' ➜ '{destination}'")

if __name__ == "__main__":
    compress_file("students_data.txt", "students_data.txt.gz")
    decompress_file("students_data.txt.gz", "students_data_restored.txt")
