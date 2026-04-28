# Dado um inteiro rowIndex, retorne a linha rowIndex do Triangulo de Pascal (indexacao 0).
# No triangulo de Pascal, cada numero interno e a soma dos dois numeros acima dele.

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # A linha 0 do triangulo e [1]; comecamos com ela e vamos evoluir ate a rowIndex.
        res = [1]

        # Se rowIndex for 0, o laco nao roda. Se for 1, 2, ... roda essa quantidade de vezes
        # (cada iteracao sobe um nivel: linha 0 -> 1 -> 2 -> ... -> rowIndex).
        for i in range(rowIndex):
            # Aloca a proxima linha: tamanho = tamanho da anterior + 1 (regra do triangulo),
            # preenchida com zeros; vamos preencher somando contribuicoes de res[j].
            next_row = [0] * (len(res) + 1)
            # j indexa cada elemento da linha atual; cada res[j] "empurra" valor para duas casas abaixo.
            for j in range(len(res)):
                # O numero res[j] da linha de cima contribui para a posicao j da linha de baixo
                # (o vizinho "esquerdo" do par acima de next_row[j]).
                next_row[j] += res[j]
                # O mesmo res[j] tambem contribui para a posicao j+1 (o vizinho "direito" do par).
                next_row[j + 1] += res[j]
            # A linha recem-calculada vira a "atual" para a proxima iteracao do laco externo.
            res = next_row
        # res agora e exatamente a rowIndex-esima linha (0-based) do Triangulo de Pascal.
        return res