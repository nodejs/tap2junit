A utility that converts [TAP version 13](https://testanything.org/) to [JUnit](https://junit.org/junit5/). That's it.

Upstream is currently unmaintained at https://bitbucket.org/fedoraqa/pytap13/src/develop/

The syntax expected is currently pretty custom-tailored for use at https://ci.nodejs.org

Improvements welcome.

To install:

`pip install tap2junit`

To run:

`tap2junit -i file.tap -o file.xml`

Suggested code hygiene:
```
$ flake8 --max-line-length=88 .
$ isort -rc .
$ black .
```