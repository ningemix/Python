from funçoesSorteio import *
resp = str (input ("Vai sortear números ou nomes? [num/nome]: ")).strip().lower()
if resp == "num":
    sortnum()
if resp == "nome":
    sortnome ()