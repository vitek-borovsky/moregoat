class MoreGoatBoard:
    """
    Represents the state of the board of moregoat game

    After move is performed wifh `put_stone` dead if-any stones are collected and cleared automaticly

    Board is 0-indexed in both axis, and [0,0] is top left corner
    x-axis is horizontal <-->
    """

    CELL_EMPTY = 0

    def __init__(self, player_count: int, board_size: int) -> None:
        self._player_count = player_count
        self._board_size = board_size
        self._board = [ [ self.CELL_EMPTY for _ in range(board_size) ] for _ in range(board_size) ]

    def __getitem__(self, index: tuple[int, int]) -> int:
        x, y = index
        if x < 0 or y < 0: raise IndexError()
        return self._board[y][x]

    def __setitem__(self, index: tuple[int, int], value: int):
        x, y = index
        if x < 0 or y < 0: raise IndexError()
        if value != self.CELL_EMPTY and self[x, y] != self.CELL_EMPTY: raise RuntimeError(f"Stone already at this possition {x},{y}\n{self}")
        self._board[y][x] = value

    def __repr__(self) -> str:
        return "\n".join(
            ", ".join(str(self._board[y][x]) for x in range(self._board_size))
        for y in range(self._board_size))

    # this function can be rewritten more efficiently to not use recursion
    def __is_alive(self, player: int, x: int, y: int, seen: set[ tuple[int, int]]) -> bool:
        """
        Determines whether connected stones are dead

        Args:
            seen: recursive tracker of what we seen so far
        """
        if x not in range(self._board_size): return False
        if y not in range(self._board_size): return False

        if (x,y) in seen: return False
        seen.add((x,y))

        if self[x,y] == self.CELL_EMPTY: return True

        # Diffrent player occupies this cell
        if self[x,y] != player: return False

        return any((
            self.__is_alive(player, x - 1, y, seen),
            self.__is_alive(player, x + 1, y, seen),
            self.__is_alive(player, x, y - 1, seen),
            self.__is_alive(player, x, y + 1, seen),
        ))


    def __check_dead(self, player, x: int, y: int) -> set[tuple[int,int]]:
        """
        Checks if target stone is dead if so it removes
        targeted connected stones

        Returns:
            Stones captured
        """
        if x not in range(self._board_size): return set()
        if y not in range(self._board_size): return set()

        # Stones were not encloused by all sides
        connected_stones = set()
        if self.__is_alive(player, x, y, connected_stones): return set()

        # Connected stones are dead we can remove them from the board
        for x, y in connected_stones:
            self[x, y] = self.CELL_EMPTY

        return connected_stones

    def put_stone(self, player: int, x: int, y :int) -> set[tuple[int,int]]:
        """
        Puts stone of targets player on board
        x-axis is horizontal <--->

        Args:
            Player player_ids from 1-n inc

        Returns:
            set of Stones captured
        """
        if player not in range(1, self._player_count + 1): raise RuntimeError(f"Wrong player id {player}")
        print(f"\n\nbefore\n{self}")
        self[x,y] = player
        print(f"after\n{self}")
        # Succesfully placed stone at valid location
        return self.__check_dead(player, x - 1, y) \
            .union(self.__check_dead(player, x + 1, y)) \
            .union(self.__check_dead(player, x, y - 1)) \
            .union(self.__check_dead(player, x, y + 1))

