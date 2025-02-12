class Ship:
    def __init__(self, size, orientation, start_position):
        self.size = size
        self.orientation = orientation
        self.start_position = start_position
        self.positions = self._calculate_positions()
        self.hits = set()

    def _calculate_positions(self):
        x, y = self.start_position
        if self.orientation == "H":
            return [(x + i, y) for i in range(self.size)]
        elif self.orientation == "V":
            return [(x, y + i) for i in range(self.size)]

    def is_hit(self, position):
        if position in self.positions:
            self.hits.add(position)
            return True
        return False

    def is_sunk(self):
        return set(self.positions) == self.hits
import random

class Board:
    def __init__(self, size=10):
        self.size = size
        self.ships = []
        self.attacks = set()

    def place_ship(self, ship):
        if self._can_place_ship(ship):
            self.ships.append(ship)
        else:
            raise ValueError("Невозможно разместить корабль.")

    def _can_place_ship(self, ship):
        for pos in ship.positions:
            x, y = pos
            if not (0 <= x < self.size and 0 <= y < self.size):
                return False
            for other_ship in self.ships:
                if pos in other_ship.positions:
                    return False
        return True

    def random_place_ships(self, ship_sizes):
        """Случайное размещение кораблей."""
        for size in ship_sizes:
            while True:
                orientation = random.choice(["H", "V"])
                start_x = random.randint(0, self.size - 1)
                start_y = random.randint(0, self.size - 1)
                ship = Ship(size, orientation, (start_x, start_y))
                try:
                    self.place_ship(ship)
                    break
                except ValueError:
                    continue

    def attack(self, position):
        if position in self.attacks:
            return "Уже стреляли"
        self.attacks.add(position)
        for ship in self.ships:
            if ship.is_hit(position):
                return "Попадание!" if not ship.is_sunk() else "Корабль потоплен!"
        return "Мимо!"

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def display(self, show_ships=False):
        """Отображение игрового поля с нумерацией координат."""
        board = [["~"] * self.size for _ in range(self.size)]

        # Размещение кораблей (если требуется показать)
        for ship in self.ships:
            for x, y in ship.positions:
                if show_ships:
                    board[y][x] = "S"

        # Обозначение атак
        for x, y in self.attacks:
            if any((x, y) in ship.positions for ship in self.ships):
                board[y][x] = "X"
            else:
                board[y][x] = "*"

        # Формирование строк для вывода
        header = "   " + " ".join(str(i) for i in range(self.size))  # Заголовок с цифрами по X
        rows = []
        for i, row in enumerate(board):
            rows.append(f"{i:2} " + " ".join(row))  # Нумерация строк по Y

        return header + "\n" + "\n".join(rows)
    
class Player:
    def __init__(self, name, board_size=10):
        self.name = name
        self.board = Board(board_size)

    def random_place_ships(self, ship_sizes):
        self.board.random_place_ships(ship_sizes)

    def attack(self, opponent_board, position):
        return opponent_board.attack(position)
def main():
    print("Добро пожаловать в 'Морской бой'!")
    
    # Создаем игроков
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")

    # Размещение кораблей
    ship_sizes = [5, 4, 3, 3, 2]
    print("Размещение кораблей для Игрока 1...")
    player1.random_place_ships(ship_sizes)
    print("Размещение кораблей для Игрока 2...")
    player2.random_place_ships(ship_sizes)

    # Основной игровой процесс
    current_player, opponent = player1, player2
    while True:
        print(f"\nПоле {current_player.name}:")
        print(current_player.board.display(show_ships=True))

        print(f"\nПоле {opponent.name}: (для атак)")
        print(opponent.board.display(show_ships=False))

        print(f"\n{current_player.name}, ваш ход!")
        try:
            x, y = map(int, input("Введите координаты для атаки (x, y): ").split())
            if not (0 <= x < current_player.board.size and 0 <= y < current_player.board.size):
                print("Координаты за пределами поля. Попробуйте снова.")
                continue
            result = current_player.attack(opponent.board, (x, y))
            print(result)
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if opponent.board.all_ships_sunk():
            print(f"{current_player.name} победил!")
            break

        current_player, opponent = opponent, current_player

if __name__ == "__main__":
    main()


