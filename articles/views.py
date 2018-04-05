from django.shortcuts import render


def base(request):
    return render(request, 'articles/index.html')


def index(request):
    return render(request, 'articles/index.html')


def tabs(request):
    return render(request, 'articles/tabs.html')


def widget(request):
    return render(request, 'articles/widget.html')


def table(request):
    return render(request, 'articles/table.html')


def buttons(request):
    return render(request, 'articles/buttons.html')


def login(request):
    return render(request, 'articles/login.html')


def register(request):
    return render(request, 'articles/register.html')


def _404(request):
    return render(request, 'articles/404.html')


def sign(request):
    return render(request, 'articles/sign.html')


def resume(request):
    return render(request, 'articles/resume.html')


def inbox(request):
    return render(request, 'articles/inbox.html')


def compose(request):
    return render(request, 'articles/compose.html')


def editor(request):
    return render(request, 'articles/editor.html')


def chart(request):
    return render(request, 'articles/chart.html')


def graph(request):
    return render(request, 'articles/graph.html')


def project(request):
    return render(request, 'articles/project.html')


def ribbon(request):
    return render(request, 'articles/ribbon.html')


def blank(request):
    return render(request, 'articles/blank.html')


def _500(request):
    return render(request, 'articles/500.html')
