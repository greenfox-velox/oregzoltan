import sys
import csv

def main():
    todo = TodoApp()
    if len(sys.argv) > 1:
        todo.menu(sys.argv)
    else:
        print(todo.usage())

class TodoApp():
    def __init__(self):
        self.name = 'todo.csv'

    def menu(self, arg):
        self.arg = arg
        if self.arg[1] == '-l':
            print(self.list_task())
        elif self.arg[1] == '-a':
            self.add_new_task()
        elif self.arg[1] == '-r':
            self.remove_task()
        elif self.arg[1] == '-c':
            self.complete_task()
        else:
            self.argument_error_handling()

    def argument_error_handling(self):
        print('Unsupported argument')
        print(self.usage())

    def usage(self):
        text = 'Python Todo application\n=======================\n\nCommand line arguments:\n -l   Lists all the tasks\n -a   Adds a new task\n -r   Removes an task\n -c   Completes an task\n'
        return text

    def checked(self, x):
        if x == 'True':
            return '[x] '
        else:
            return '[ ] '

    def list_task(self):
        try:
            f = open(self.name)
            text = csv.reader(f, delimiter=';')
        except:
            self.create_file_if_missing()
            f = open(self.name)
            text = csv.reader(f, delimiter=';')
        line_number = 1
        text2 = ''
        for i in text:
            text2 = text2 + str(line_number) + ' - ' + self.checked(i[0]) + i[1] + '\n'
            line_number += 1
        if len(text2) <= 0:
            return('No todos for today!')
        return(text2)
        f.close()

    def add_new_task(self):
        if len(self.arg) == 2:
            print('Unable to add: No task is provided')
        else:
            try:
                f = open(self.name, 'a')
            except:
                self.create_file_if_missing()
                f = open(self.name)
            f.write('False;'+self.arg[2]+'\n')
            f.close()

    def remove_task(self):
        if len(self.arg) == 2:
            print('Unable to remove: No index is provided')
        else:
            try:
                f = open(self.name)
            except:
                self.create_file_if_missing()
                f = open(self.name)
            try:
                text = f.readlines()
                del text[int(self.arg[2])-1]
                f.close()
                f = open(self.name, 'w')
                for i in text:
                    f.write(i)
                f.close()
            except IndexError:
                print('Unable to remove: Index is out of bound')
            except ValueError:
                print('Unable to remove: Index is not a number')

    def create_file_if_missing(self):
        f = open(self.name, 'w')

    def complete_task(self):
        pass

main()
