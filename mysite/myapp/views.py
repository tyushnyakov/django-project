from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("Hello, world. You're at the myapp about.")


def contact(request):
    return HttpResponse("Hello, world. You're at the myapp contact.")


def all(request):
    goods = [
        "thermometer", "candy wrapper", "pool stick", "buckel", "drawer",
        "cell phone", "flag", "glass", "cork", "milk", "chapter book",
        "drill press", "lip gloss", "key chain", "leg warmers", "bookmark",
        "floor", "sand paper", "hair brush", "outlet", "pencil", "beef",
        "needle", "rusty nail", "glow stick", "deodorant", "canvas", "boom box",
        "fork", "cookie jar", "television", "seat belt", "lamp shade",
        "nail clippers", "carrots", "hair tie", "tissue box", "slipper",
        "flowers", "mop", "fridge", "keyboard", "mouse pad", "model car",
        "towel", "water bottle", "speakers", "glasses", "toe ring", "candle",
        "rubber band", "shoes", "soda can", "toothpaste", "white out", "chair",
        "clock", "headphones", "piano", "book", "grid paper", "greeting card",
        "tooth picks", "screw", "money", "bread", "wallet", "scotch tape",
        "sketch pad", "playing card", "bottle", "paint brush", "eraser",
        "camera", "sandal", "house", "ring", "tire swing", "fake flowers",
        "USB drive", "credit card", "doll", "door", "balloon", "video games",
        "brocolli", "hanger", "wagon", "sofa", "shovel", "car", "toothbrush",
        "tv", "picture frame", "tomato", "computer", "pants", "thread", "clothes",
        "thermostat",
    ]
    return render(request, 'all.html', context={'goods': goods})


def info(request):
    return HttpResponseRedirect("/myapp/about")


def good(request):
    category = request.GET.get('category', 'cat')
    id = request.GET.get('id', 1)
    return HttpResponse("Good. Category: {}. Id: {}.".format(category, id))
