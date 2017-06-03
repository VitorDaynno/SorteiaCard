# SorteiaCard
Algoritmo responsável por sortear um card da primeira coluna do Trello e imprimir seu nome

1. Instale a api do Trello

	pip install trello

2. Para iniciar renomeie o arquivo Config_example.py para Config.py 

3. Preencha-o com a api_key e o token do Trello. (Ambos podem ser encontrados no link (https://trello.com/app-key), para desenvolvimento e teste)

4. A chamada deve ser feita passando o nome do quadro por parâmetro
	
	python sorteio.py nome_do_quadro
