'''
Glosary:
[CLS] significa el comienzo de una oración 
[SEP] hace que BERT sepa que la segunda oración ha comenzado.

Objetivo: Se debe tokenizar jergas, abreviauras, nicknames, urls, hashtags y emoticones.

Instrucciones:
En la word segmentación, el enunciado solo segmenta los tokens con espacios en
blanco, por lo que el texto de entrada debe estar pre-tokenizado. Podemos aplicar
diferentes algoritmos de segmentación de forma transparente sin cambiar los procesadores pre / post.

En la user segmentacion, ............

'''
import sentencepiece as spm

def modelCadena(cadena):  
    spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000 --normalization_rule_name=nfkc_cf')  
    sp_word = spm.SentencePieceProcessor()
    sp_word.load('m_word.model')
    return(sp_word.encode_as_pieces(cadena))

def modelUsuario(cadena):  
    spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_user --user_defined_symbols=<unk>,</s>,<s>,<sep>,<cls> --vocab_size=2000')
    sp_user = spm.SentencePieceProcessor()
    sp_user.load('m_user.model')

    #Identificacion de SEP y CLS
    print('0=', sp_user.decode_ids([0]))
    print('1=', sp_user.decode_ids([1]))
    print('2=', sp_user.decode_ids([2]))
    print('3=', sp_user.decode_ids([3]))  # decoded to <sep>
    print('4=', sp_user.decode_ids([4]))  # decoded to <cls>
    print(sp_user.encode_as_pieces('this is a test<sep> hello world<cls>'))
    return(sp_user.encode_as_pieces(cadena))