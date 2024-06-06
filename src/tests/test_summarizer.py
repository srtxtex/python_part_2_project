from shared.summary import summarizer

def test_summarizer():
    article_text = "Это тестовая статья на русском языке. Она содержит некоторый текст для проверки функции summarizer."
    summary = summarizer(article_text)
    assert summary == "Представляю тестовую статью на русском языке, которая содержит некоторый текст для проверки функции summarizer."