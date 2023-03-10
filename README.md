# **GitScripts**

Automation scripts that you can use for various Git workflows.

---

## Requirements

* Must use `bash` shell -- right now, these are `bash` scripts.
* Download them to an easy-to-remember directory.
* Go to `~/.bash_profile` or `~/.profile` or wherever you have a `$PATH` variable stored.  Add the full directory path to GitScripts into `$PATH`, then restart your computer so you can start using GitScripts as you would a regular Linux command.

---

## Scripts

* `mkgit` -- creates a local project folder with an empty git repo automatically

  * Usage: `mkgit <new_folder_name>`
  * must be used in directory where you want to create your new project folder, and that directory should not contain a Git repo itself.
* `mkclone` -- automatically creates a local clone of a remote Git repo in any directory

  * Usage: `mkclone <existing_directory> <remote_repo_url>`
* `propergitfetch` -- fetches remote repo changes.  Great for local repos with multiple remote repo connections.

  * Usage: `propergitfetch`
  * Must be used within a Git repo!
* `propergitpull` -- pulls in remote repo changes into a specified branch.

  * Usage: `propergitpull`
  * Must be used within a Git repo!
* `quickpull` -- automates process of pulling from origin repo to a particular branch in local repo.

  * Usage: `quickpull`
  * Must be used within a Git repo!
* `qreb` -- automates process of rebasing your current branch onto tip of `main` branch.

  * Usage: `qreb`
  * Must be used within a Git repo!
* `mkbare` -- automates process of creating a cloned local bare repository from a local project folder

  * Usage: `mkbare <current_folder_name>`
  * Must be used within the directory of the existing project folder you want to create your bare repo from.
* `bareclone` -- automates process of copying content from a local bare repo into a new project folder.

  * Usage:
    * 1. In one terminal: `git daemon --verbose --export-all --base-path=.`
    * 2. In another terminal: `bareclone <new_folder_name_or_path> <existing_bare_repo_name>`
  * Do _NOT_ include `.git` in `<existing_bare_repo_name>`!
  * Must be used in directory where bare repo of your choice exists.
  * Both terminals must be at that directory for the 2-step process to work.
* `localclone` -- automates process of cloning a local project folder containing a Git repo, such that the original repo is now the `origin` remote repo for the cloned project folder.

  * Usage: `localclone <new_folder_name> <original_folder_name>`
  * Creates clone in same directory the original folder is in.
* `openrepo` -- automates process of opening a project folder and its Git repo at a particular branch.  Creates a new branch if specified branch is not yet created.

  * Usage: `openrepo <existing_folder_name_or_path> <branch_name>`
  * Can use this in current repo or anywhere else.
* `viewbranches` -- allows one to view all connected remote repos, as well as all local and pulled remote branches for a particular local repo

  * Usage: `viewbranches <folder_name_or_path>`
  * Can use this in current repo or anywhere else.

## Any concerns or problems?

* Be sure to [create an issue here](https://github.com/astronomical3/GitScripts/issues)

## Wiki

* Link to GitHub wiki [here](https://github.com/astronomical3/GitScripts/wiki)
