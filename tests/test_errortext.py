import unittest

from errortext import error_text


class ErrorTextTest(unittest.TestCase):
    def test_can_render_error_text(self):
        self.assertEqual(error_text(AssertionError()), "AssertionError")
        self.assertEqual(error_text(ValueError("x")), "x")
        self.assertEqual(error_text(ValueError()), "ValueError")
        self.assertEqual(error_text(AssertionError("x")), "AssertionError: x")
        # TODO: Test source_reference
        # try:
        #     raise AssertionError("x")
        # except AssertionError as error:
        #     actual_error_text = error_text(error)
        #     assert re.match(
        #         r"AssertionError: x \(from .*test_can_render_error_text@test_common.py:\d+\)", actual_error_text
        #     ), f"actual_error_text={actual_error_text!r}"
