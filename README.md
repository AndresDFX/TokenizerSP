<div align="justify">
<h1><u>TokenizerSP - Tokenizer Sentence Piece </u></h1>

TokenizerSP es un tokenizador de texto sin supervisión, principalmente para sistemas de generación de texto basados ​​en redes neuronales donde el tamaño del vocabulario está predeterminado antes del entrenamiento del modelo neural. Usando el algoritmo SentencePiece implementa unidades de subpalabras (p. Ej., Codificación de pares de bytes (BPE) [Sennrich et al.]) Y modelo de lenguaje unigram [Kudo.]) Con la extensión del entrenamiento directo a partir de oraciones sin formato. SentencePiece nos permite crear un sistema puramente de extremo a extremo que no depende del procesamiento previo / posterior específico del idioma.


---
<h2><u> 1. Construido con </u></h2>

Se deben instalar las siguientes dependencias:


- Emojis 
```bash
pip3 install -U emojis
```
- SentencePiece
```bash
pip3 install -U sentencepiece
```
- Tkinter

- PAGE (GUI Builder for Tkinter)

- Python3.8


---
<h2><u> 2. Instalacion</u></h2>

Para ejecutar el programa abrimos una terminal y ejecutamos el comando `python main.py` esto inciara la interfaz GUI, que permitira ingresar el texto y seleccionar entre la tokenizacion del Modelo de Usuario (BERT) y Modelo de Palabra.

---
<h3><u>2.1) Modelo de Usuario (BERT)</u></h3>

Podemos definir tokens especiales para modificar el comportamiento de DNN a través de los tokens. Ejemplos típicos son los símbolos especiales de BERT., Por ejemplo, [SEP] y [CLS].

Hay dos tipos de tokens especiales:

**Símbolos definidos por el usuario:** siempre se trata como un token en cualquier contexto. Estos símbolos pueden aparecer en la oración de entrada.

**Símbolo de control:** solo reservamos identificadores para estos tokens. Incluso si estos tokens aparecen en el texto de entrada, no se manejan como un token. El usuario necesita insertar identificadores explícitamente después de la codificación.

---
<h3><u>2.2) Modelo de Palabra</u></h3>

En el modelo de palabra, el programa solo segmenta tokens con espacios en blanco, por lo que la entrada de texto debe estar pre-tokenizada. Podemos aplicar diferentes algoritmos de segmentación de forma transparente sin cambiar los procesadores pre/post.

</div>