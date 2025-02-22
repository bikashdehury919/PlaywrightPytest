# tests/test_api.py
import pytest
from utills.api_client import APIClient
import allure


@allure.feature("API Testing")
@allure.story("Public API - Cat Facts")
def test_get_cat_facts(config, http_session):
    """Test fetching cat facts from a public API using requests."""
    # Using requests session since this is a standalone public API
    api_client = APIClient(http_session=http_session, base_url=config['public_apis']['cat_facts'])

    response = api_client.get("/facts")

    # Validate response
    assert response['status'] == 200, f"Expected status 200, got {response['status']}"
    assert isinstance(response['body'], list), "Expected response body to be a list of facts"
    assert len(response['body']) > 0, "Expected at least one cat fact in the response"
    assert "text" in response['body'][0], "Expected 'text' field in the first cat fact"

    # Log a sample fact for reporting
    sample_fact = response['body'][0]['text']
    allure.attach(f"Sample Cat Fact: {sample_fact}", name="Sample Fact", attachment_type=allure.attachment_type.TEXT)