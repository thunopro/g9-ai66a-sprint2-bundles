"""Edit one Markdown section in place. Run from the repository root.

  python <pkg>/apply.py replace <file> "<heading start>" <snippet.md>
      Replace the section that starts with the line beginning "<heading start>"
      (a "## " heading) up to the next "## " heading. A trailing "---" separator
      is kept. If the section is the last one, it runs to the end of the file.

  python <pkg>/apply.py insert-before <file> "<heading start>" <snippet.md>
      Insert the snippet right before that heading.

This helper is NOT part of the repository - do not commit it.
"""
import sys
from pathlib import Path


def main():
    mode, file, heading, snippet = sys.argv[1:5]
    path = Path(file)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    new = Path(snippet).read_text(encoding="utf-8").rstrip("\n") + "\n"
    start = next((i for i, l in enumerate(lines) if l.startswith(heading)), None)
    if start is None:
        sys.exit(f"Heading not found in {file}: {heading!r}")
    if mode == "insert-before":
        lines[start:start] = [new, "\n"]
    elif mode == "replace":
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        tail = [l for l in lines[start:end] if l.strip()]
        keep_rule = bool(tail) and tail[-1].strip() == "---" and end < len(lines)
        lines[start:end] = [new] + (["\n---\n\n"] if keep_rule else ["\n"] if end < len(lines) else [])
    else:
        sys.exit("mode must be replace or insert-before")
    path.write_text("".join(lines), encoding="utf-8")
    print(f"Updated {file}: {mode} {heading!r}")


if __name__ == "__main__":
    main()
