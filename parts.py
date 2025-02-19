class Board:
    # Инициализировать игровое поле - списков с пробелами.
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Пустые клетки обозначены пробелами

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        row -= 1  # Уменьшаем на 1 для индексации с 0
        col -= 1
        if 0 <= row < 3 and 0 <= col < 3:  # Проверка на допустимые индексы
            if self.board[row][col] == ' ':  # Проверка на пустую клетку
                self.board[row][col] = player
                print('Ход сделан!')
                return True  # Возвращаем True, если ход успешен
            else:
                print('Клетка занята!')
                return False  # Возвращаем False, если клетка занята
        else:
            print('Некорректные координаты!')
            return False  # Возвращаем False, если координаты некорректны

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
            print('-' * 5)

    # Метод для получения хода от игрока
    def player_move(self, player):
        while True:  # Цикл для повторного запроса ввода в случае некорректных данных
            row_input = input(f'Игрок {player}, введите номер строки (1-3) или одну из команд для выхода: "end", "quit", "exit": ')
            if row_input.lower() in ['end', 'quit', 'exit']:  # Проверка на ввод команд выхода
                print("Игра завершена.")
                self.display()  # Отобразить финальное состояние игрового поля
                exit()  # Завершение программы
            try:
                row = int(row_input)

                col_input = input(f'Игрок {player}, введите номер столбца (1-3) или одну из команд для выхода: "end", "quit", "exit": ')
                if col_input.lower() in ['end', 'quit', 'exit']:  # Проверка на ввод команд выхода
                    print("Игра завершена.")
                    self.display()  # Отобразить финальное состояние игрового поля
                    exit()  # Завершение программы
                col = int(col_input)

                if self.make_move(row, col, player):  # Проверяем, был ли ход успешным
                    break  # Выход из цикла, если ход был сделан
            except ValueError:
                print('Пожалуйста, введите корректные числа! Для выхода из данной игры выберите одну из команд: "end", "quit", "exit".')

# Создать иговое поле - обьект класса Board.
game = Board()

# Основной игровой цикл
while True:
    game.display()
    game.player_move('X')  # Ход игрока X
    game.display()
    game.player_move('O')  # Ход игрока O
