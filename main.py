# # main.py is used for script runner
# import subprocess
# import sys

# script = sys.argv[1]

# result = subprocess.run(
#     ["python", script],
#     capture_output=True,
#     text=True
# )

# print(result.stdout)

import subprocess
import sys

script = sys.argv[1]

script_path = f"/scripts/{script}"

result = subprocess.run(
    ["python", script_path],
    capture_output=True,
    text=True
)

print(result.stdout)

