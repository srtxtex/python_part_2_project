from django.shortcuts import render
from django.http import HttpResponse
from main.models import Original, Translate, Summary
from main.forms import OriginalFrom, TranslateFrom, SummaryForm
from shared.translate import translator
from shared.summary import summarizer

"""Модуль содержит функции обработки HTTP запросв и отрисовку представлений."""


def index(request) -> HttpResponse:
    '''
    Выполянет отрисовку страницы index.html (Главная) и
    отвечает за обработку событий формы
    :param request: объект класса HttpRequest
    :return: Объект класса HttpResponse
    '''

    original_articls = list()
    originals = Original.objects.all()
    for original in originals:
        original_articls.append(original.original_article)

    translated_articls = list()
    translates = Translate.objects.all()
    for translate in translates:
        translated_articls.append(translate.translated_article)

    summarize_articls = list()
    summaries = Summary.objects.all()
    for summary in summaries:
        summarize_articls.append(summary.summarize_article)

    original_article = request.POST.get('original_article')
    translated_article = request.POST.get('translated_article')
    summarize_article = request.POST.get('summarize_article')

    if (request.method == 'POST'):
        if (original_article):
            originalFrom = OriginalFrom(request.POST)
            originalFrom.save()
        if (translated_article):
            translateFrom = TranslateFrom(request.POST)
            translateFrom.save()
        if (summarize_article):
            summaryForm = SummaryForm(request.POST)
            summaryForm.save()

    if (original_article):
        translated_article = translator(original_article)

    if (translated_article):
        summarize_article = summarizer(translated_article)

    if (not original_article and len(original_articls)):
        original_article = original_articls[-1]

    if (not translated_article and len(translated_articls)):
        translated_article = translated_articls[-1]

    if (not summarize_article and len(summarize_articls)):
        summarize_article = summarize_articls[-1]

    originalFrom = OriginalFrom({'original_article': original_article})
    translateFrom = TranslateFrom({'translated_article': translated_article})
    summaryForm = SummaryForm({'summarize_article': summarize_article})

    return render(request, 'index.html',
                  {'originalFrom': originalFrom,
                   'translateFrom': translateFrom,
                   'summaryForm': summaryForm})


def faqs(request) -> HttpResponse:
    '''
    Отрисовывает страницу FAQS
    :param request: объект класса HttpRequest
    :return: Объект класса HttpResponse
    '''
    return render(request, 'faqs.html')


def abouts(request) -> HttpResponse:
    '''
    Отрисовывает страниу About
    :param request: объект класса HttpRequest
    :return: объект класса HttpResponse
    '''

    return render(request, 'abouts.html')
