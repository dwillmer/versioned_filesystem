
from pathlib import Path

from git import Repo

from fs.expose import dokan
from fs.osfs import OSFS


def clone_to_local_dir(remote, local: Path):
    Repo.clone_from(remote, local)


def ensure_path_invalid(path: Path):
    if path.exists() or path.is_dir():
        msg = f"'{path}' already exists"
        raise ValueError(msg)


def create_virtual_filesystem(local, mount):
    repo_fs = OSFS(local)
    mount_point = dokan.mount(repo_fs, mount)
    return mount_point


def changed_files(repo):
    """ Returns a list of files which have current
        differences from HEAD.
    """
    return [x.a_path for x in repo.index.diff(None)]


if __name__ == '__main__':

    # This must *not* already exist
    local = Path('/Users/dave/vfs_tmp')
    remote = 'https://github.com/fastats/fastats.git'
    mount = '/virtual_test'

    ensure_path_invalid(local)
    clone_to_local_dir(local=local)
    create_virtual_filesystem(local, mount)

