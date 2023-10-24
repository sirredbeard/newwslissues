# newwslissues

This repository is a GitHub Action and Python script that checks for all new issues created in [microsoft/WSL](https://github.com/microsoft/wsl) in the last hour and tweets them at [@New_WSL_Issues](https://twitter.com/New_Wsl_Issues).

[check-issues.yaml](https://github.com/sirredbeard/newwslissues/blob/main/.github/workflows/check-issues.yaml) runs hourly, it:

* Installs Python
* Updates pip
* Installs [Tweepy](https://www.tweepy.org/)
* Goes back in time an hour via flux capacitance as-a-service
* Requests details on all new issues in microsoft/WSL created
* Extracts the title and URL of each
* Passes those to tweet.py as options
* [tweet.py](https://github.com/sirredbeard/newwslissues/blob/main/tweet.py):
    * Grabs all the authentication tokens required for Twitter, stored as GitHub secrets, as environmental variables
    * Grabs anything passed after tweet.py, in this case, the title and URL of each issue created
    * Tweets it
* Repeats that for each new issue, sleeping a bit each time to avoid rate limiting
