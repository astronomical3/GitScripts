#Used for parsing clone url to get local clone name and open up local clone in mkclone shell command.

import os
import sys

remote_repo_string = sys.argv[1].replace("https://github.com/", "").replace("https://gitlab.com/", "").replace("https://bitbucket.org/", "").replace("/src/main", "").replace(".git", "").replace("git@bitbucket.org:", "").replace("git@gitlab.com:", "").replace("git@github.com:", "")
remote_repo_list = remote_repo_string.split("/")
print(remote_repo_list[1])
