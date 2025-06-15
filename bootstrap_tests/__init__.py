import bootstrap_tests.test_llm_rewrite
import unittest


def run_unittests():
    return unittest.main(
        exit=False,
        verbosity=2,
        argv=['dummy'],
        module=bootstrap_tests.test_llm_rewrite
    )


tests_result = run_unittests().result
if len(tests_result.failures) > 0:
    raise Exception("Failures in the bootstrap tests")
if len(tests_result.errors) > 0:
    raise Exception("Errors with the bootstrap tests")
