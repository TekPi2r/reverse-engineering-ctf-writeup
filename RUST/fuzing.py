import subprocess
import string
import random

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def fuzz_binary(binary_path, output_file, iterations=1000):
    """Fuzz the binary and save interesting outputs."""
    with open(output_file, 'w') as f:
        # Test with predefined patterns
        patterns = [
            "",
            "test",
            "flag",
            "FLAG",
            "123456",
            "password",
            "letmein",
            "rust"
        ]
        
        for pattern in patterns:
            try:
                result = subprocess.run([binary_path, pattern], capture_output=True, timeout=5)
                if result.returncode != 0 or result.stdout or result.stderr:
                    f.write(f"Input: {pattern}\n")
                    f.write(f"Return Code: {result.returncode}\n")
                    f.write(f"Stdout: {result.stdout.decode()}\n")
                    f.write(f"Stderr: {result.stderr.decode()}\n")
                    f.write("="*40 + "\n")
            except subprocess.TimeoutExpired:
                f.write(f"Input: {pattern} caused a timeout.\n")
                f.write("="*40 + "\n")

        # Test with random patterns
        for _ in range(iterations):
            pattern = generate_random_string(random.randint(1, 50))
            try:
                result = subprocess.run([binary_path, pattern], capture_output=True, timeout=5)
                if result.returncode != 0 or result.stdout or result.stderr:
                    f.write(f"Input: {pattern}\n")
                    f.write(f"Return Code: {result.returncode}\n")
                    f.write(f"Stdout: {result.stdout.decode()}\n")
                    f.write(f"Stderr: {result.stderr.decode()}\n")
                    f.write("="*40 + "\n")
            except subprocess.TimeoutExpired:
                f.write(f"Input: {pattern} caused a timeout.\n")
                f.write("="*40 + "\n")

if __name__ == "__main__":
    BINARY_PATH = "./rust-reverse"
    OUTPUT_FILE = "fuzzing_results.txt"
    fuzz_binary(BINARY_PATH, OUTPUT_FILE)
