import sentencepiece as spm
import emojis

def modelCadena(cadena):  
    spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000 --normalization_rule_name=nfkc_cf')  
    sp_word = spm.SentencePieceProcessor()
    sp_word.load('m_word.model')
    cleanCadena = cadena.strip()
    return(sp_word.encode_as_pieces(emojis.encode(cleanCadena)))

def modelUsuario(cadena):  
    spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_user --user_defined_symbols=</s>,<s>,<sep>,<cls> --vocab_size=2000')
    sp_user = spm.SentencePieceProcessor()
    sp_user.load('m_user.model')
    cleanCadena = cadena.strip()
    indexSpace = len(cadena.split(' ', 1)[0])
    tokenInit ='<s>'
    tokenSpace='<sep>'
    tokenFinal ='<cls></s>'
    cadenaSalida = tokenInit+ cleanCadena[:indexSpace] + tokenSpace + cleanCadena[indexSpace:]+tokenFinal
    return(sp_user.encode_as_pieces(emojis.encode(cadenaSalida)))