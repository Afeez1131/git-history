import re

def describe_command(command):
    command = re.sub(r'https://github\.com/([a-zA-Z0-9-]+)/([a-zA-Z0-9-]+)\.git', 'https://github.com/<username>/<repository>.git', command)
    command_parts = command.split()
    if len(command_parts) < 2:
        return command

    subcommand = command_parts[1]

    # Handling git checkout
    if subcommand == "checkout":
        if "-b" in command_parts:
            for i, part in enumerate(command_parts):
                if part == "-b" and i + 1 < len(command_parts):
                    branch_name = command_parts[i + 1]
                    return f"git checkout -b branch-name"
        
        return "git checkout branch-name"

    # Handle 'switch'
    elif subcommand == "switch":
        if "-c" in command_parts:
            return "git switch -c new-branch-name"
        return "git switch branch-name"

    # Handle 'add'
    elif subcommand == "add":
        if "." in command_parts or "-A" in command_parts:
            return "git add all changes"
        return "git add path/to/file"
    elif subcommand == "remote":
        if "add" in command_parts:
            for i, part in enumerate(command_parts):
                if part == "add" and i + 1 < len(command_parts):
                    remote_name = command_parts[i + 1]
                    return f"git remote add {remote_name} <url>"
        elif "remove" in command_parts:
            for i, part in enumerate(command_parts):
                if part == "remove" and i + 1 < len(command_parts):
                    remote_name = command_parts[i + 1]
                    return f"git remote remove {remote_name}"
        return "git remote <command>"


    # Handling git push
    elif subcommand == "push":
        if len(command_parts) > 2 and command_parts[2] == "origin" and len(command_parts) > 3:
            remote_branch = command_parts[3]
            if ":" in remote_branch:
                    branch_parts = remote_branch.split(":")
                    local_branch = 'local-branch-name'
                    remote_branch = 'remote-branch-name'
                    return f"git push origin {local_branch}:{remote_branch}"
            return f"git push origin remote-branch-name"
        return "git push origin branch-name"

    # Handling git pull
    elif subcommand == "pull":
        if len(command_parts) > 2:
            remote = command_parts[2]
            branch = command_parts[3] if len(command_parts) > 3 else "branch-name"
            return f"git pull remote 'branch-name'"
        return "git pull origin branch-name"

    # Handle 'reset'
    elif subcommand == "reset":
        if "--hard" in command_parts:
            return "git reset --hard commit-hash"
        elif "--soft" in command_parts:
            return "git reset --soft commit-hash"
        elif "--mixed" in command_parts:
            return "git reset --mixed commit-hash"
        return "git reset commit-hash"

    # Handle 'rm'
    elif subcommand == "rm":
        if "-r" in command_parts and "--cached" in command_parts:
            return "git rm -r --cached path/to/files"
        if "-r" in command_parts:
            return "git rm -r path/to/files"
        return "git rm path/to/file"

    # Handle 'revert'
    elif subcommand == "revert":
        if "-m" in command_parts:
            return "git revert -m 1 commit-hash"
        return "git revert commit-hash"

    # Handling git commit
    elif subcommand == "commit":
        if "-am" in command_parts:
            for i, part in enumerate(command_parts):
                if part == "-am" and i + 1 < len(command_parts):
                    commit_message = " ".join(command_parts[i + 1:])
                    return f"git commit -am 'commit message'"
        return "git commit -am 'commit message'"

    # Handle 'fetch'
    elif subcommand == "fetch":
        if len(command_parts) > 2:
            remote = command_parts[2]
            branch = command_parts[3] if len(command_parts) > 3 else "branch-name"
            return f"git fetch remote branch-name"
        return "git fetch"

    # Handle 'merge'
    elif subcommand == "merge":
        if len(command_parts) > 2:
            return "git merge target-branch"
        return "git merge"

    # Handle 'cherry-pick'
    elif subcommand == "cherry-pick":
        if len(command_parts) > 2:
            return "git cherry-pick commit-hash"
        return "git cherry-pick"

    # Handle 'status'
    elif subcommand == "status":
        return "git status"

    # Handle 'log'
    elif subcommand == "log":
        if "--oneline" in command_parts:
            return "git log --oneline"
        elif "--graph" in command_parts:
            return "git log --graph"
        elif "--decorate" in command_parts:
            return "git log --decorate"
        return "git log"

    # Handle 'branch'
    elif subcommand == "branch":
        if "-d" in command_parts or "--delete" in command_parts:
            return "git branch -d branch-name"
        elif "-D" in command_parts or "--force-delete" in command_parts:
            return "git branch -D branch-name"
        if len(command_parts) > 2:
            return "git branch branch-name"
        return "git branch"

    # Handle 'stash'
    elif subcommand == "stash":
        if "apply" in command_parts:
            return "git stash apply"
        elif "pop" in command_parts:
            return "git stash pop"
        elif "list" in command_parts:
            return "git stash list"
        elif "save" in command_parts:
            return "git stash save 'stash message'"
        return "git stash"

    # Handle 'config'
    elif subcommand == "config":
        if "--global" in command_parts and "user.name" in command_parts:
            return "git config --global user.name 'your-name'"
        elif "--global" in command_parts and "user.email" in command_parts:
            return "git config --global user.email 'your-email@example.com'"
        return "git config"

    # Handle 'diff'
    elif subcommand == "diff":
        if len(command_parts) > 2 and command_parts[2].startswith("'") and command_parts[2].endswith("'"):
            branch1 = command_parts[2][1:-1]
            branch2 = command_parts[3][1:-1] if len(command_parts) > 3 and command_parts[3].startswith("'") and command_parts[3].endswith("'") else "main"
            return f"git diff '{branch1}' '{branch2}'"
        return "git diff branch1 branch2"

    # Handle 'blame'
    elif subcommand == "blame":
        if len(command_parts) > 2:
            return "git blame path/to/file"
        return "git blame"

    # Handle 'tag'
    elif subcommand == "tag":
        if len(command_parts) > 2:
            return "git tag tag-name"
        return "git tag"

    # Handle 'init'
    elif subcommand == "init":
        if len(command_parts) > 2 and command_parts[2] == ".":
            return "git init current-directory"
        elif len(command_parts) > 2:
            directory = " ".join(command_parts[2:])
            return f"git init {directory}"
        else:
            return "git init"

    # Handle 'clone'
    elif subcommand == "clone":
        if len(command_parts) > 2:
            return "git clone repository-url"
        return "git clone"

    # Handle 'show'
    elif subcommand == "show":
        if len(command_parts) > 2:
            return "git show commit-hash"
        return "git show"

    # Handle 'rebase'
    elif subcommand == "rebase":
        if len(command_parts) > 2:
            return "git rebase branch-name"
        return "git rebase"

    # Handle 'bisect'
    elif subcommand == "bisect":
        if "start" in command_parts:
            return "git bisect start"
        elif "bad" in command_parts:
            return "git bisect bad"
        elif "good" in command_parts:
            return "git bisect good"
        return "git bisect"

    # Handle 'remote'
    elif subcommand == "remote":
        if "add" in command_parts:
            return "git remote add remote-name remote-url"
        elif "remove" in command_parts:
            return "git remote remove remote-name"
        return "git remote"

    # Handle 'show-ref'
    elif subcommand == "show-ref":
        return "git show-ref"

    # Handle 'archive'
    elif subcommand == "archive":
        return "git archive --format=zip HEAD"

    # Handle 'mv'
    elif subcommand == "mv":
        return "git mv old-filename new-filename"

    # Handle 'filter-branch'
    elif subcommand == "filter-branch":
        return "git filter-branch --tree-filter 'command' -- --all"

    # Handle 'clean'
    elif subcommand == "clean":
        return "git clean -fd"

    # Fallback for unknown or less common commands
    return command
