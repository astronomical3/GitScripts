# **GitScripts**

Automation scripts that you can use for common Git workflows.

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

## Any concerns or problems?

* Be sure to [create an issue here](https://github.com/astronomical3/GitScripts/issues)

## Wiki

* Link to GitHub wiki [here](https://github.com/astronomical3/GitScripts/wiki)
