import argparse
import re
from pathlib import Path
from tqdm import tqdm

def load_patterns(pattern_file=None):
    if pattern_file:
        try:
            with open(pattern_file, "r", encoding="utf-8") as f:
                return [re.compile(line.strip(), re.IGNORECASE) for line in f if line.strip()]
        except Exception as e:
            print(f"[ERROR] Failed to read pattern file: {e}")
            exit(1)
    else:
        # Default patterns
        default = [
            r"<script.*?>.*?</script>",
            r"onerror\s*=",
            r"onload\s*=",
            r"javascript:",
            r"<iframe.*?>",
            r"<img.*?onerror=.*?>",
            r"eval\s*\(",
            r"document\.cookie",
            r"window\.location"
        ]
        return [re.compile(pat, re.IGNORECASE) for pat in default]

def scan_file(dump_path, patterns):
    try:
        with open(dump_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(tqdm(f, desc="Scanning"), 1):
                if any(pat.search(line) for pat in patterns):
                    print(f"[!] Baris {i}: {line.strip()}")
    except Exception as e:
        print(f"[ERROR] Gagal membaca file dump: {e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="XSS Scanner To scan MySQLdump for potential XSS patterns.")
    parser.add_argument("--file-dump", required=True, help="Path to MySQL dump file (.sql)")
    parser.add_argument("--pattern-file", help="Path to file containing list of custom XSS patterns (regex per line)")
    args = parser.parse_args()

    dump_path = Path(args.file_dump)
    if not dump_path.exists():
        print(f"[ERROR] File dump not found: {dump_path}")
        exit(1)

    patterns = load_patterns(args.pattern_file)
    scan_file(dump_path, patterns)

if __name__ == "__main__":
    main()