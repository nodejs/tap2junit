import glob
import os
import subprocess
import sys
from pathlib import Path

import pytest
from _common import normalize_output


class TestOutputs:
    filelist = glob.glob("test/fixtures/*.tap")
    print(filelist)

    @pytest.mark.parametrize("file", filelist)
    def test_file(self, tmp_path, file):
        name = os.path.basename(file).replace(".tap", "")
        original = f"./test/output/{name}.xml"
        output = f"{tmp_path}/out.xml"
        subprocess.run([sys.executable, "-m", "tap2junit", "-i", file, "-o", output])
        assert Path(original).read_text() == normalize_output(Path(output).read_text())
