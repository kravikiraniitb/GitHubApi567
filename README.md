# GitHubApi567
[![kravikiraniitb](https://circleci.com/gh/kravikiraniitb/GitHubApi567.svg?style=svg)](https://app.circleci.com/pipelines/github/kravikiraniitb/GitHubApi567?branch=main&filter=all)

Deliverable 2:
Main hurdle I faced was by the API rate limit set by github. I couldn't test all cases at once and this delayed testing.<br/>
As it's extremely challenging to go through all API responses, I designed the testing to only check if the reponse with status code 200 (successful) was recieved.<br/>
My unit testing only contained two cases as these were main tests required and they both indirectly tested the third scenerio (error while retrieving the commits of a repository)<br/>
Time limit for no response has to be defined so the function stops after some time if there's no response to the API request.<br/>
Other constraint was only Public repositories are listed as one can't private repositories without valid permission.<br/>

