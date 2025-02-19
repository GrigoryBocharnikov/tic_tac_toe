from tic_tac_toe.gameparts.parts import Board  # Импортируем только из parts.py

def main():
    board = Board()  # Используем класс Board из parts.py
    board.display()
    # Логика игры...

if __name__ == "__main__":
    main()
