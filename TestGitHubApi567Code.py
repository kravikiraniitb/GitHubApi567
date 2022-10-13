import unittest

from unittest.mock import patch, MagicMock
#import json

from GitHubApi567Code import githubapi567

class TestAPI(unittest.TestCase):

    @patch('GitHubApi567Code.githubapi567')
    def testAPI1(self, mock_requests):
        mock_requests.return_value = None
        self.assertEqual(githubapi567("kravikiraniitb"),None)

    @patch('GitHubApi567Code.githubapi567')
    def testAPI2(self, mock_requests):
        mock_requests.return_value = "error occured while retrieving a user's repositories"
        #self.assertEqual(githubapi567("richkempinski"),None)
        self.assertEqual(githubapi567("kravikiraniitb2"),"error occured while retrieving a user's repositories")


    #@patch('GitHubApi567Code.repo_req')
    #@patch('GitHubApi567Code.repo_req')

   # @patch.multiple('GitHubApi567Code', repo_req=MagicMock(return_value="<Response [200]>"),commit_req=MagicMock(return_value="<Response [200]>"))

    #def testAPI1(self, **mocks):
        #mock_repo.return_value = "<Response [200]>"
        #mock_commit.return_value = "<Response [200]>"
     #   self.assertEqual(githubapi567("richkempinski"),None)


    #@patch('GitHubApi567Code.requests')
   # def testAPI1(self, mock_requests): 
      #  mock_response = MagicMock()
       # #mock_response = "<Response [200]>"

        #mock_response.status_code = 200
       # mock_response.json.return_value = {"Sample" : "JSON"}
       # mock_requests.get.return_value = mock_response
       # self.assertEqual(githubapi567("richkempinski"),None)


    #@patch('GitHubApi567Code.requests')
    #def testAPI2(self, mock_requests): 
     #   mock_response = MagicMock()
      #  mock_response.status_code = 404
       # mock_response.json.return_value = {"Sample" : "JSON"}
        #mock_requests.get.return_value = mock_response
       # self.assertEqual(githubapi567("richkempinski2"),"error occured while retrieving a user's repositories")
        #invalid repository name passed



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

