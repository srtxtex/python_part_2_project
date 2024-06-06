"""
Этот модуль содержит реализованную предварительно обученную модель краткого изложения русскоязычного текста
"""
from transformers import MBartForConditionalGeneration, MBartTokenizer
import torch

def summarizer(article_text: str) -> str:
    '''
    Реализует модель mbart_ru_sum_gazeta генераци резюме на
    основе исходного текста

    :param article_text: строка содержащая полный текст на русском языке.
    :return: строка содержащая краткое тезисное изложение исходного текста.
    '''
    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)

    input_ids = tokenizer(
        [article_text],
        max_length=600,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)

    return summary