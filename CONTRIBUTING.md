
This document instructs with setting up a dev environment and experimenting with `cli-manager` and contributing to the project.

Create a personal fork of the project on Github. (Click on the `Fork` button on Project's main page).

Clone the fork on your local machine:
- `git clone git@github.com:YourUsername/cli-manager`

Your remote repo on Github is called `origin`.

Change directory to the cloned repo.
- `cd cli-manager`

Add the original repository as a remote called upstream.
- `git remote set-url upstream git@github.com:Anbarryprojects/cli-manager.git`

If you created your fork a while ago be sure to pull upstream changes into your local repository.
- `git pull upstream`

Set up your dev environment:
- Create a `virtualenv` first:
    - `python -m virtualenv .venv`
- Activate the `virtualenv`:
    - `source ./venv/bin/activate`
- Install the dev requirements:
    - `poetry install`

Create a new branch to work on! Branch from `develop` if it exists, else from `main`.

Implement/fix your feature, comment your code.

Follow the code style of the project, including indentation.

Write or adapt tests as needed. run the tests with `tox`.

Add or change the documentation as needed.

Squash your commits into a single commit with git's interactive rebase.

Push your branch to your fork on Github, the remote origin.

Click the `Compare & pull request` button that is showed up in Github.
