from package import *

def main():
    task = Task(options)

    task.operation_control()
    del task

if __name__ == "__main__":
    main()