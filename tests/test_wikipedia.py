from test_poetry import wikipedia


def test_random_page_use_given_language(mock_requests_get):
    wikipedia.random_page(language="de")
