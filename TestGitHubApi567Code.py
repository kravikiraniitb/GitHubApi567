import unittest

from GitHubApi567Code import githubapi567


class TestAPI(unittest.TestCase):
    def testAPI1(self): 
        self.assertEqual(githubapi567("kravikiraniitb"),"Results obtained successfully")

    def testAPI2(self): 
        self.assertEqual(githubapi567("kravikiraniitb2"),"error occured while retrieving a user's repositories")
        #invalid repository name passed



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

