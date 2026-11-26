LINE = "One star: the maple tree dripped sap on my car, my laptop, and my sandwich, and then had the nerve to look beautiful doing it."

# The entry must be exactly one line of 1-279 characters.
assert 1 <= len(LINE) <= 279, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back what was written: a silent partial write must fail loudly.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match LINE"
