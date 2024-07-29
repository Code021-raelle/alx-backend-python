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
        """ test org """
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_result)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test to return the result of public repos url """
        expected_url = "https://api.github.com/orgs/google/repos"
        mock_org.return_value = {'repos_url': expected_url}

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """ Test for list of repos and mocked property """
        expected_url = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = expected_url

        expected_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient("google")
        result = client.public_repos()

        self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(expected_url)


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False),
        ({"license": {"key": "my_license"}}, "other_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
