import git

def get_repo_info(repo_path='.'):
    repo = git.Repo(repo_path)
    info = {
        'active_branch': repo.active_branch.name,
        'latest_commit': repo.head.commit.hexsha,
        'commit_message': repo.head.commit.message,
        'committer': repo.head.commit.committer.name,
        'commit_date': repo.head.commit.committed_datetime.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return info
