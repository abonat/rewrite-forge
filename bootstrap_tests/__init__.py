import bootstrap_tests.test_llm_rewrite
import unittest


def run_unittests():
    return unittest.main(
        exit=False,
        argv=['dummy'],
        module=bootstrap_tests.test_llm_rewrite
    )

if len(run_unittests().result.failures) > 0:
    raise Exception("Failures in the bootstrap tests")
if len(run_unittests().result.errors) > 0:
    raise Exception("Errors with the bootstrap tests")
