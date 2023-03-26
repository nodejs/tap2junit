A utility that converts [TAP version 12 and 13](https://testanything.org/) to [JUnit](https://junit.org/junit5/). That's it.

Upstream is currently unmaintained at https://bitbucket.org/fedoraqa/pytap13/src/develop/

The syntax expected is currently pretty custom-tailored for use at https://ci.nodejs.org

Improvements are welcome.

To install from https://pypi.org/project/tap2junit (recommended):

`pip install tap2junit` or `pipx install tap2junit`

To install directly from this repo (not recommended):

`pipx install --force git+https://github.com/nodejs/tap2junit.git`

To run:

`tap2junit -i file.tap -o file.xml`

`tap2junit --help`
```
usage: tap2junit [-h] --input INPUT --output OUTPUT [--compact] [--name NAME] [--package PACKAGE]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        path to tap13 file
  --output OUTPUT, -o OUTPUT
                        output file name
  --compact, -c         do not prettify the xml output
  --name NAME, -n NAME  override test suite name
  --package PACKAGE, -p PACKAGE
                        set package for test suite
```

Suggested code hygiene:
```
$ ruff --show-fixes --show-source .
$ black .
```
