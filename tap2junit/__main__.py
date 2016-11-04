import argparse
import os
import platform
from junit_xml import TestSuite, TestCase
from tap13 import TAP13 as tap13

tap_parser = tap13()


def parse(name, data):
    tap_parser.parse(data)
    junit_tests = []

    for test in tap_parser.tests:
        t = TestCase(test.description, None, test.yaml['duration_ms'])
        if test.result == 'ok':
            if test.directive in ['SKIP', 'TODO']:
                t.add_skipped_info(test.comment)
            else:
                t.stdout = test.comment

        elif test.result == 'not ok':
            t.add_error_info(test.yaml['stack'])

        junit_tests.append(t)

    return TestSuite(name, junit_tests, platform.node())


def main():
    parser = argparse.ArgumentParser('tap2junit')
    parser.add_argument('--input', '-i', type=argparse.FileType('r'), nargs='?',
                        help='path to tap13 file', required=True)
    parser.add_argument('--output', '-o', type=argparse.FileType('w'),
                        nargs='?', help='destination', required=True)
    args = parser.parse_args()

    data = False
    try:
        data = args.input.read()
    except IOError:
        raise

    result = parse(os.path.splitext(args.input.name)[0], data)
    try:
        result.to_file(args.output, [result], prettyprint=False)
    except IOError:
        raise

if __name__ == "__main__":
    main()
