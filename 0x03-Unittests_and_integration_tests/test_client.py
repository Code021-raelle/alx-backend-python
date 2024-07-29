#!/usr/bin/env python3
""" test client
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ test client """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, org_name, expected_result, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_result)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        expected_url = "https://api.github.com/orgs/google/repos"
        mock_org.return_value = {'repos_url': expected_url}

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
