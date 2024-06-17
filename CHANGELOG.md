# tap2junit changelog

## [0.2.0](https://github.com/nodejs/tap2junit/compare/v0.1.6...v0.2.0) (2024-06-17)


### Features

* add missing release-please files ([efaf634](https://github.com/nodejs/tap2junit/commit/efaf634126c82edb551b89391a86a9bf8d56dca5))

### Fixes

* fix missing stack property ([4ddd24](https://github.com/nodejs/tap2junit/commit/4ddd2472a94b6153d7f298fc63fde04980903f66))

### 0.1.6
* Support for parsing YAML blocks
* Add option to override test suite name
* Add support for TAP version 12
* Support TAP with nested tests
* Fix duration_ms to be milliseconds instead of seconds
* Explicitly encode input file as utf-8
* Use GitHub Actions for ci testing
* Replace Python linting tools with Ruff
* Add pypa/hatch for building and publishing

### 0.1.5
* Add support for Python 3
* Add automated testing on Travis CI
* Remove Pipfile.lock to support multiple Python versions
