#!/usr/bin/python3
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions"""
    question = "What language did you speak first?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    language_survey.store_responses('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    """Test that three individual responses are stored properly"""
    responses = ['Kinyarwanda', 'English', 'French']
    for response in responses:
        language_survey.store_responses(response)

    for response in responses:
        assert response in language_survey.responses
