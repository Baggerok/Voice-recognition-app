import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def from_root(*path_parts):
    return os.path.join(PROJECT_ROOT, *path_parts)