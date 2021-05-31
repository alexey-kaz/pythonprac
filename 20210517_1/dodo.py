from glob import glob

from doit.tools import create_folder


def task_update():
    """Update translation."""
    return {
        'actions': [
            'pybabel extract -o fig.pot figeq',
            'pybabel update -D fig -d lang -i fig.pot'],
        'file_dep': glob('figeq/*.py'),
        'targets': ['fig.pot',
                    'lang/ru/LC_MESSAGES/fig.po'],
    }


def task_compile():
    """Compile translation."""
    return {
        'actions': [
            (create_folder, ['figeq/ru/LC_MESSAGES']),
            'pybabel compile -f -D fig -l ru -i lang/ru/LC_MESSAGES/fig.po -d figeq'
        ],
        'file_dep': ['lang/ru/LC_MESSAGES/fig.po'],
        'targets': ['figeq/ru/LC_MESSAGES/fig.mo'],
    }


def task_test():
    """Run unittest."""
    return {
        'actions': ['python3 -m unittest'],
    }


def task_wheel():
    """Wheel distribution."""
    return {
        'actions': ['python3 -m build -w'],
        'task_dep': ['compile'],
    }


def task_src():
    """Source distribution."""
    return {
        'actions': ['python3 -m build -s'],
        'task_dep': ['clear'],
    }


def task_clear():
    """Clear junk."""
    return {
        'actions': ['git clean -x -d -f'],
    }
