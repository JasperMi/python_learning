import unittest
from chapter_11.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对单个答案会被妥善地存储"""

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)


if __name__ == "__main__":
    unittest.main()
