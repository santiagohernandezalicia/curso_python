import Levenshtein 
input1 = "castor"
input2 = "castro"

dist =Levenshtein.distance(input1, input2)
print(f"La distancia entre {input1} y {input2} es: {dist}")

ratio =Levenshtein.ratio(input1, input2)
print(f"El ratio de similitud entre {input1} y {input2} es: {ratio}")

set_ratio = Levenshtein.setratio(input1, input2)
print(f"El ratio de similitud entre {input1} y {input2} es: {set_ratio}")

hamming = Levenshtein.hamming(input1, input2)
print(f"La distancia de Hamming entre {input1} y {input2} es: {hamming}")
