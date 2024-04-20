traducoes = {
    "casa": "house",
    "gato": "cat",
    "cachorro": "dog",
    "mesa": "table",
    "cadeira": "chair",
    "carro": "car",
    "bicicleta": "bicycle",
    "computador": "computer",
    "celular": "cellphone",
    "livro": "book",
    "caneta": "pen",
    "lapis": "pencil",
    "borracha": "eraser",
    "caderno": "notebook",
    "janela": "window",
    "porta": "door",
    "hello": "oi",
    "goodbye": "tchau",
    "good morning": "bom dia",
    "good afternoon": "boa tarde",
    "good night": "boa noite",
}

print("bem-vindo ao tradutor de palavras!")

palavra = input("digite uma palavra:") 
if palavra in traducoes:
    traducao = traducoes[palavra]
    print(f"A tradução de '{palavra}' é '{traducao}'.")
else:
    print(f"Palvra não encontrada no dicionário de traduções.")