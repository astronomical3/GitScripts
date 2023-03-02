import os
import sys

remote_repo_string = sys.argv[1].replace("/", " ")
remote_repo_list = remote_repo_string.split()
print(remote_repo_list[3].replace(".git", ""))