# created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyse(request):
    text = request.GET.get("st", "default")
    remove = request.GET.get("removepunc", "off")
    caps = request.GET.get("capitalize", "off")
    space = request.GET.get("removespace", "off")
    charcount = request.GET.get("charcount", "off")
    word = request.GET.get("word_count", "off")
    punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    print(text, remove, caps)
    if remove == "on":
        remove_punc = ""
        for char in text:
            if char not in punctuation:
                remove_punc = remove_punc + char
    else:
        remove_punc = "---"
    if caps == "on":
        capitalized = ""
        capitalized = text.upper()
    else:
        capitalized = "---"
    if space == "on":
        removespace = ""
        text2 = text.split(" ")
        for words in text2:
            removespace = "".join(text2)
    else:
        removespace = "---"
    if charcount == "on":
        char_count = 0
        for char in text:
            char_count += 1
    else:
        char_count = 0
    if word == "on":
        text2 = text.split(" ")
        word_count = len(text2)
    else:
        word_count = 0
    params = {
        "remove_punc": remove_punc,
        "capitalized": capitalized,
        "removespace": removespace,
        "char_count": char_count,
        "word_count": word_count,
    }
    return render(request, "analyse.html", params)
