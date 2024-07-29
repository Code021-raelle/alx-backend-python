#!/usr/bin/env python3
""" test client
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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


@parameterized_class([
    {"org_payload": org_payload,
     "repos_payload": repos_payload,
     "expected_repos": expected_repos,
     "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Test integration """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """ Side effects """
            if url == "https://api.github.com/orgs/google":
                mock_response = Mock()
                mock_response.json.return_value = cls.org_payload
                return mock_response
            elif url == cls.org_payload["repos_url"]:
                mock_response = Mock()
                mock_response.json.return_value = cls.repos_payload
                return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """ tear down class """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public repos """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test public repos with license """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
