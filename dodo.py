
def task_nose():
    return "nosetests"

pyFiles = ["lib/doit/__init__.py","lib/doit/runner.py","lib/doit/task.py",
           "lib/doit/main.py", "lib/doit/util.py", "lib/doit/dependency.py", 
           "lib/doit/loader.py", 
           "tests/__init__.py", "tests/test_runner.py", "tests/test_task.py",
           "tests/test_util.py", "tests/test_dependency.py",
           "tests/test_loader.py", "tests/test_main.py"]

def task_checker():
    for file in pyFiles:
        yield {'action': ["pychecker",file], 
               'name':file, 
               'dependencies':(file,)}

def bad_seed():
    xiiiiii = 5


