class Converter:
    def __init__(self, _rows):
        self.rows = _rows

    def convert(self, _input):
        output = ""
        for letter in _input:
            if letter == ' ':
                output += letter
                continue

            index = self.find_index(letter)
            output += self.rows[index[0]][index[1] - 1]

        return output

    def find_index(self, letter):
        for i, rows in enumerate(self.rows):
            for j, item in enumerate(rows):
                if item == letter:
                    return [i, j]
