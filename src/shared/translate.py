"""
Этот модуль содержит реализованную предварительно обученную модель машинного перевода
"""
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch

def translator(text, source_language="en_XX", target_language="ru_RU", piece_len = 128, max_batch = 32) -> str:
    '''
    Функция реализует модель многоязычного машинного перевода
    mbart-large-50-many-to-many-mmt на целевой язык - Русский
    :param text: строка содержащая текст на английском языке.
    :source_language: язык с которого нужно перевести
    :target_language: язык на который нужно перевести
    :piece_len: максимальная длина входных кусков текста
    :max_batch: количество батчей сэмла для перевода
    :return: строка содержащая переведенный на русский язык исходный текст    
    '''
    text = text.replace('\n', '')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.cuda.is_available()

    model_path = "facebook/mbart-large-50-many-to-many-mmt"
    tokenizer = MBart50TokenizerFast.from_pretrained(model_path)
    model = MBartForConditionalGeneration.from_pretrained(model_path).to(device)
    tokenizer.src_lang = source_language
    
    input_id = tokenizer.encode(text)
    
    start_id=[input_id[0]]
    end_id=[input_id[-1]]
    input_id = input_id[1:-1]
    
    # Сохранение результата
    res_text=''
    
    input_id_list= []
    attention_mask_list=[]
    
    # Создание батчей сэмла
    for i in range(0, len(input_id), piece_len):
        tmp_id = start_id+input_id[i:i+piece_len]+end_id
        if len(input_id) < piece_len:
            # Один из сэмплов
            input_id_list.append(tmp_id)
            attention_mask_list.append([1]*len(tmp_id))
            break
        else:
            input_id_list.append(tmp_id+((piece_len+2)-len(tmp_id))*[1])#padding
            attention_mask_list.append([1]*len(tmp_id)+((piece_len+2)-len(tmp_id))*[0])

    # Перевод 
    for i in range(0, len(input_id_list), max_batch):        
        input_id_list_batch = input_id_list[i:i+max_batch]
        attention_mask_list_batch= attention_mask_list[i:i+max_batch]

        input_ids_ss = torch.LongTensor(input_id_list_batch).to(device)
        attention_mask_ss = torch.LongTensor(attention_mask_list_batch).to(device)
        input_dict = {'input_ids': input_ids_ss,"attention_mask": attention_mask_ss}

        generated_tokens = model.generate(
            **input_dict,
            forced_bos_token_id = tokenizer.lang_code_to_id[target_language]
        )

        res_tmp = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        # Конкатинация перевода
        res_text+=' '.join(res_tmp)

    return res_text