Basic Git:
    git init
    git diff
    git add filename
    git status #check staging area
    git commit -m "" #with -m cmd, less than 50 char
    git log
    git push

Generalizations:
    git checkout HEAD filename: Discards changes in the working directory.
    git reset HEAD filename: Unstages file changes in the staging area.
    git reset commit_SHA: Resets to a previous commit in your commit history.

Git checkout #since 2023, it is splited as git switch & git restore
    git checkout branch-name == git switch branch-name
    git checkout -b new-branch-name == git switch -c new-branch-name #create a new branch
    git checkout -- file-name == git restore file-name

Git stash: Store your work temporarily
    git stash
    git stash pop

Git log: more git log cmd
    git log --oneline: oneline expression
    git log -S "keyword": search "keyword" in log
    git log --oneline --grah: describe branches

Git commit --amend:
    git commit --amend: overwrite previous commit
    git commit --amend --no-edit: without msg update

Git alias cmd:
    git config --global alias.co "checkout": git checkout -> git co

Git branching:
    git branch: check branches
    git branch name
    git checkout name
    git merge [from] [to] #In general, from is a branch and to is master or main
    git branch -d name: delete branch
    git branch -D name: delete branch which is not fully merged

Git workflow:
    Create a branch
    Commit changes
    Create a pull request
    Review pull request
    Merge and delete branch

Git clone:
    git clone remote_location clone_name
    git remote -v: checking remote repo
    git fetch: update from origin, bringing the changes
    git merge origin/master [current repo]: after fetching, you need to merge updated remote repo to local repo
    git push [remote repo to be updated] [local repo to update]
    