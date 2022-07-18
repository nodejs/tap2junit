import glob
import os
import subprocess

from _common import normalize_output

for file in glob.glob("test/fixtures/*.tap"):
    name = os.path.basename(file).replace(".tap", "")
    output = f"test/output/{name}.xml"
    try:
        run = subprocess.run(
            ["python", "-m", "tap2junit", "-i", file, "-o", output],
            shell=False,
        )
        run.check_returncode()

        data = open(output, "r+").read()
        open(output, "w").write(normalize_output(data))
    except subprocess.CalledProcessError:
        print(f"failed running test {name}")
