#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import PropertyMock
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    # ... previous methods
    """Test suite for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')  # patch correction
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct payload"""
        test_payload = {"login": org_name, "id": 12345}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, test_payload)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns expected repo names"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
                GithubOrgClient, "_public_repos_url",
                return_value="https://fake.url/api") as mock_url:
            client = GithubOrgClient("testorg")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://fake.url/api")
