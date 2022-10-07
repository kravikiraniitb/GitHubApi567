import requests
import json

def githubapi567(GithubID):

    #GithubID = input("Please enter your github ID: ")
    try:
        repo = requests.get('https://api.github.com/users/'+GithubID+'/repos')
        #print(str(repo))

        if str(repo) == "<Response [200]>":
            for x in repo.json():
                repo_name = x["name"]
                commits = requests.get('https://api.github.com/repos/'+GithubID+'/'+repo_name+'/commits')

                if str(commits) == "<Response [200]>":
                    no_comits = len(commits.json())
                    print("Repo: "+repo_name+" Number of commits: "+str(no_comits))
                    #return "Repo: "+repo_name+" Number of commits: "+str(no_comits)
                    return "Results obtained successfully"
                else:
                    #raise Exception("error occured while retrieving the commits of a repository")
                    return "error occured while retrieving the commits of a repository"

        else:
            
            #raise Exception("error occured while retrieving a user's repositories")
            return "error occured while retrieving a user's repositories"

    except:
        return "some error occured"
        #print("some error occured")

githubapi567("kravikiraniitb")
