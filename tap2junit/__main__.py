import argparse
import os
import platform

import yamlish
from junit_xml import TestCase, TestSuite

from tap2junit.tap13 import TAP13 as tap13


def extract_test_info_from_description(description):
    # If test description is path-like (contains /), consider the last
    # token to be the test name and convert the dirname to classname.
    # The test description can also have already a class name style
    # (module serapated by '.') so do the same for this case
    if description and "/" in description:
        sanitize = os.path.normpath(description)
        (test_class, test_name) = os.path.split(sanitize)
        # Remove possible heading slash and replace / by .
        test_class = test_class.lstrip("/").replace("/", ".")
    elif description and "." in description:
        # Remove possible heading slash and replace / by .
        test_name = description.split(".")[-1]
        test_class = ".".join(description.split(".")[0:-1])
    else:
        test_name = description
        test_class = None
    return (test_class, test_name)


def map_yaml_to_junit(test):
    yaml = test.yaml or {}
    # Even though the name is `duration_ms` the value is in seconds.
    elapsed_sec = yaml.get("duration_ms", None)
    (test_class, test_name) = extract_test_info_from_description(test.description)
    t = TestCase(test_name, classname=test_class, elapsed_sec=elapsed_sec)
    if test.result == "ok":
        if test.directive in ("SKIP", "TODO"):
            t.add_skipped_info(test.comment)
        else:
            t.stdout = test.comment

    elif test.result == "not ok":
        raw_yaml = f"\n{yamlish.dumps(yaml)}" if yaml else ""
        err_code = yaml.get("exitcode", 0)
        err_severity = yaml.get("severity", "")
        err_output = yaml.get("stack", "") or raw_yaml
        error_message = yaml.get("message", "") or f"{err_severity} ({err_code})"
        if err_code < 0 or err_severity == "crashed":
            t.add_error_info(error_message, err_output, err_code)
        else:
            t.add_failure_info(error_message, err_output, err_code)
        t.stderr = test.diagnostics
    return t


def parse(name, data, package=None):
    tap_parser = tap13()
    tap_parser.parse(data)
    junit_tests = [map_yaml_to_junit(t) for t in tap_parser.tests]
    return TestSuite(
        name, test_cases=junit_tests, hostname=platform.node(), package=package
    )


def convert(in_file, out_file, pretty=True, name=None, package=None):
    input_file = os.path.splitext(in_file.name)[0]
    data = in_file.read()
    result = parse(name or input_file, data, package)
    TestSuite.to_file(out_file, [result], prettyprint=pretty, encoding="utf-8")


def main():
    arg_parser = argparse.ArgumentParser("tap2junit")
    arg_parser.add_argument(
        "--input",
        "-i",
        type=argparse.FileType("r"),
        help="path to tap13 file",
        required=True,
    )
    arg_parser.add_argument(
        "--output",
        "-o",
        type=argparse.FileType("w"),
        help="output file name",
        required=True,
    )
    arg_parser.add_argument(
        "--compact", "-c", action="store_true", help="do not prettify the xml output"
    )
    arg_parser.add_argument("--name", "-n", help="override test suite name")
    arg_parser.add_argument("--package", "-p", help="set package for test suite")
    args = arg_parser.parse_args()
    convert(
        args.input,
        args.output,
        pretty=not args.compact,
        name=args.name,
        package=args.package,
    )


if __name__ == "__main__":
    main()
