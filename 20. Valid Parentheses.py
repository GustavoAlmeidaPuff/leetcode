# Classe que o LeetCode usa para agrupar a solução do problema.
class Solution(object):
    # Método principal: recebe a string s e devolve True se os parênteses forem válidos.
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Pilha (lista usada como stack): guardamos só os símbolos de ABERTURA na ordem em que aparecem.
        stack = []
        # Dicionário: para cada FECHAMENTO, qual é o par de ABERTURA correspondente.
        # Assim, ao ver ")", sabemos que o topo da pilha deve ser "(".
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # Percorre cada caractere da string da esquerda para a direita.
        for c in s:
            # Se o caractere é um de fechamento (está nas chaves do dicionário)...
            if c in closeToOpen:
                # Só é válido se a pilha não estiver vazia E o topo for o par correto de abertura.
                if stack and stack[-1] == closeToOpen[c]:
                    # Remove o abertura correspondente da pilha (fechou um par bem formado).
                    stack.pop()
                else:
                    # Pilha vazia com fechamento sobrando, ou tipo errado no topo → inválido.
                    return False
            else:
                # É um símbolo de abertura: empilha para esperar o fechamento depois.
                stack.append(c)
        # No fim, se a pilha está vazia, todos os pares fecharam; se sobrou algo, faltou fechar.
        return True if not stack else False
