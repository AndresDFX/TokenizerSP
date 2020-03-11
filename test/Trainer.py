import sentencepiece as spm
import csv

'''
#BASIC EXAMPLE
# train sentencepiece model from `botchan.txt` and makes `m.model` and `m.vocab`
# `m.vocab` is just a reference. not used in the segmentation.
spm.SentencePieceTrainer.train('--input=botchan.txt --model_prefix=m --vocab_size=2000')

# makes segmenter instance and loads the model file (m.model)
sp = spm.SentencePieceProcessor()
sp.load('m.model')

# encode: text => id
print(sp.encode_as_pieces('This is a test'))
print(sp.encode_as_ids('This is a test'))

# decode: id => text
print(sp.decode_pieces(['▁This', '▁is', '▁a', '▁t', 'est']))
print(sp.decode_ids([209, 31, 9, 375, 586]))
'''
'#WeAppreciateThePower Baby plug in upload your mind http://ow.ly'
#====================PARTE 1=============================================

def modelWord(cadena):
    spm.SentencePieceTrainer.train('--input=dataset.csv --model_prefix=m_word --model_type=word --vocab_size=2000 --normalization_rule_name=nfkc_cf')
    #spm.SentencePieceTrainer.train('--input=botchan.txt --model_prefix=m_word --model_type=word --vocab_size=2000')
    #spm.SentencePieceTrainer.train('--input=botchan.txt --model_prefix=m --vocab_size=2000' '--normalization_rule_name=nfkc_cf)
    #sp = spm.SentencePieceProcessor()
    #sp.load('m.model')                 
    sp_word = spm.SentencePieceProcessor()
    sp_word.load('m_word.model')

    return(sp_word.encode_as_pieces(cadena))

'''
# Gets all tokens as Python list.
vocabs = [sp.id_to_piece(id) for id in range(sp.get_piece_size())]
vocabs.append("_.")
sp_word.set_vocabulary(vocabs)
print(sp_word.encode_as_pieces('this is a test.'))  # '.' will not be one token.
print(sp_word.encode_as_ids('this is a test.'))

# reset the restriction
sp.reset_vocabulary()
print(sp.encode_as_pieces('this is a test.'))
'''

#====================PARTE 2=============================================
'''
SEP Separador de oraciones
CLS Separador de clase, va al principio de las oraciones

[CLS] significa el comienzo de una oración 
[SEP] hace que BERT sepa que la segunda oración ha comenzado.

Se debe tokenizar jergas, abreviauras, nicknames, urls, hashtags
y emoticones.

En la wordsegmentación, el enunciado solo segmenta los tokens con espacios en
blanco, por lo que el texto de entrada debe estar pre-tokenizado. Podemos aplicar
diferentesalgoritmos de segmentación de forma transparente sin cambiar los procesadores pre / post.

'''

'''
## Example of user defined symbols
spm.SentencePieceTrainer.train('--input=botchan.txt --model_prefix=m_user --user_defined_symbols=<unk>,</s>,<s>,<sep>,<cls> --vocab_size=2000')

sp_user = spm.SentencePieceProcessor()
sp_user.load('m_user.model')

# ids are reserved in both mode.
# <unk>=0, <s>=1, </s>=2, <sep>=3, <cls>=4
# user defined symbols allow these symbol to apper in the text.
print(sp_user.encode_as_pieces('this is a test<sep> hello world<cls>'))
print(sp_user.piece_to_id('<sep>'))  # 3
print(sp_user.piece_to_id('<cls>'))  # 4

#Identificacion de SEP y CLS
print('0=', sp_user.decode_ids([0]))
print('1=', sp_user.decode_ids([1]))
print('2=', sp_user.decode_ids([2]))
print('3=', sp_user.decode_ids([3]))  # decoded to <sep>
print('4=', sp_user.decode_ids([4]))  # decoded to <cls>
'''



