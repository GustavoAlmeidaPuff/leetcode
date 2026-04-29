"""Dado um inteiro rowIndex, retorne a linha rowIndex do Triangulo de Pascal (indexacao 0).
No triangulo de Pascal, cada numero interno e a soma dos dois numeros acima dele.
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j + 1] += res[j]
            res = next_row
        return res
