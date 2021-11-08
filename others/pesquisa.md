tips:
tool hours

lista distinct de todas as palavras
split (espaço)
trim
<=2 caracteres ignorar (de)
3 caracteres ignorar (proposições - com)

* Primeiro estágio
  * Leitura dos documentos
  * `open()`
    * parâmetros: <path>, `r` = leitura, `t` = text

dados dicionários do arquivo - value implementa no dicionário de palavras do arquivo

```py
def heapsort(A, n):
    # Primeiro estágio: construção do heap.
    for i in range(2, n):
        promove(A, i)

    # Segundo estágio: construção da sequência ordenada.
    for i in range(n, 1, -1):
        A[1], A[i] = A[i], A[1]
        demove(A, i - 1)
```

livro: the data wharehouse toolkit - Ralph Kimball (modelagem dimensional)
Fato Dimensão
