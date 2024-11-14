#Trabalhando com substrings

txt = "Python é divertido"
txtGrande = "É um fato conhecido de todos que um leitor se distrairá com o conteúdo de texto legível de uma página quando estiver examinando sua diagramação. A vantagem de usar Lorem Ipsum é que ele tem uma distribuição normal de letras, ao contrário de fazendo com que ele tenha uma aparência similar a de um texto legível. Muitos softwares de publicação e editores de páginas na internet agora usam Lorem Ipsum como texto-modelo padrão, e uma rápida busca por 'lorem ipsum' mostra vários websites ainda em sua fase de construção. Várias versões novas surgiram ao longo dos anos, eventualmente por acidente, e às vezes de propósito (injetando humor, e coisas do gênero"

print(txt.startswith("Python")) #Verifica a semelhança da palavra passada como parâmetro com a primeira palavra
print(txt.endswith("divertido")) #Verifica a semelhança da palavra parâmetro com a última palavra
print("divertido" in txt) #Verifica se a palavra parâmetro existe na frase
print("ler" in txtGrande) 
print(txtGrande.count("de")) #Verifica quantas vezes a palavra parâmetro aparece no texto

txt1 = txtGrande.replace("de" , "lorem") #Substitui a palavra "de" para "lorem" no texto
print(txt1)