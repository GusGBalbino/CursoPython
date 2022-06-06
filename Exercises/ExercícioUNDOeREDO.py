
def show_tasks(todo_list):
    print('Tarefas a fazer:')
    print(todo_list)

def dolist_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer.')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def dolist_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def dolist_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou digite: "undo" - Para desfazer | "redo" - Para refazer | "ls" - Para listar as terefas \n')

        if todo == 'ls':
            show_tasks(todo_list)
            continue
        
        elif todo == 'undo':
            dolist_undo(todo_list, redo_list)
            continue

        elif todo == 'redo':
            dolist_redo(todo_list, redo_list)
            continue

        dolist_add(todo, todo_list)

