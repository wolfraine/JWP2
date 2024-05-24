ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.

class TicTacToe:
    def __init__(self):
        """Inicjalizuje nową grę w kółko i krzyżyk."""
        self.board = self.getBlankBoard()
        self.currentPlayer = X
        self.nextPlayer = O

    def getBlankBoard(self):
        """Tworzy nową, pustą planszę gry w kółko i krzyżyk."""
        board = {space: BLANK for space in ALL_SPACES}
        return board

    def getBoardStr(self):
        """Zwraca tekstową reprezentację planszy."""
        b = self.board
        return f'''
            {b['1']}|{b['2']}|{b['3']} 1 2 3 
            -+-+-
            {b['4']}|{b['5']}|{b['6']} 4 5 6 
            -+-+-
            {b['7']}|{b['8']}|{b['9']} 7 8 9'''

    def isValidSpace(self, space):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        return space in ALL_SPACES and self.board[space] == BLANK

    def isWinner(self, player):
        """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
        b, p = self.board, player
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def isBoardFull(self):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        return all(self.board[space] != BLANK for space in ALL_SPACES)

    def updateBoard(self, space, mark):
        """Ustawia pole na planszy na podany znak."""
        self.board[space] = mark

    def switchPlayer(self):
        """Zmienia bieżącego gracza."""
        self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer

    def playGame(self):
        """Rozgrywka w kółko i krzyżyk."""
        print('Witaj w grze kółko i krzyżyk!')
        while True:
            print(self.getBoardStr())
            move = None
            while not self.isValidSpace(move):
                print(f'Jaki jest ruch gracza {self.currentPlayer}? (1-9)')
                move = input()
            self.updateBoard(move, self.currentPlayer)
            if self.isWinner(self.currentPlayer):
                print(self.getBoardStr())
                print(self.currentPlayer + ' wygrał grę!')
                break
            elif self.isBoardFull():
                print(self.getBoardStr())
                print('Gra zakończyła się remisem!')
                break
            self.switchPlayer()
        print('Dziękuję za grę!')

if __name__ == '__main__':
    game = TicTacToe()
    game.playGame()
