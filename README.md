# teste_de_mutacao_em_python
É a utilização da biblioteca de testes 'Mutpy' para realizar a mutação dos testes unitários do arquivo teste_calculadora, sendo que as funções se encontram no arquivo calculadora.

Foi criado dois arquivos em python:
calculadora.py
teste_calculadora.py

No arquivo calculadora.py estão funções a respeito de operações matemáticas foram feitas.
No arquivo teste_calculadora.py estão os testes unitários utilizando a biblioteca de testes unittest, testes esses relacionados as funções das operações matemáticas no arquivo calculadora.py.

Instalando a biblioteca Mutpy é possivel utilizar o teste de mutação. Através do Mutpy, ele utilizará os 2 arquivos para fazer a mutação do código.

mut.py --target calculadora --unit-test teste_calculadora -m --runner unittest

Target: o arquivo que rodará os casos de teste.
Unit-test: o arquivo que utilizará os testes unitários. 
Runner: biblioteca utilizada: pytest ou unittest.
