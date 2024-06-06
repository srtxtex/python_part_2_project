from shared.translate import translator

def test_translator():
    article_en = "This is a test article in English"
    translated = translator(article_en)
    assert translated == "Это тест статья на английском языке"
