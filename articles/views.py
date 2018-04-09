import datetime

import pyecharts
from django.shortcuts import render
from .models import LagouJob, Tabs, FreeIP
from .utils.lgjobTable import STRUCT_TIME

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def base(request):
    return render(request, 'articles/index.html')


def index(request):
    url_tabs = Tabs()
    return render(request, 'articles/index.html', {'tabs': url_tabs})


def tabs(request):
    return render(request, 'articles/tabs.html')


def widget(request):
    return render(request, 'articles/widget.html')


def lagou_table(request):
    def bar_chart(x, y, title=None):
        bar = pyecharts.Bar(width=700, height=450)
        bar.add(title, x, y, bar_category_gap='50%')
        return bar

    host = REMOTE_HOST
    collection = datetime.datetime.now().strftime(STRUCT_TIME)
    db = 'lagoujob'
    title = '拉勾网Python工作'
    t = LagouJob(db, collection, limit=0, order='createtime', desc=True)

    title1 = '职位概况'
    x1 = ['职位总计', '爬虫工程师', '新职位']
    y1 = [t.length, t.search, t.new_jobs]
    bar1 = bar_chart(x1, y1, title1)
    myechart1 = bar1.render_embed()

    title2 = '工作经验要求'
    x2 = ['<1年', '1-3年', '3-5年', '5-10年']
    y2 = [t.length-t.year_13-t.year_35-t.year_510, t.year_13, t.year_35, t.year_510]
    bar2 = pie_chart(x2, y2, title2)
    myechart2 = bar2.render_embed()

    script_list = bar2.get_js_dependencies()
    return render(request, 'articles/lagou_table.html', {'t': t, 'title': title, 'title1': title1, 'title2': title2,
                                                   'myechart1': myechart1, 'myechart2':myechart2,
                                                   'host': host, 'script_list': script_list})


def bar_chart(x, y, title=None):
    bar = pyecharts.Bar(width=700, height=450)
    bar.add(title, x, y, bar_category_gap='50%', label_text_size=15)
    return bar


def pie_chart(x, y, title=None):
    pie = pyecharts.Pie(width=700, height=450)
    pie.add(title, x, y, radius=[40, 75], is_label_show=True, legend_orient='vertical', legend_pos='left',
            label_text_color=None, label_text_size=15)
    return pie


def ip_table(request):
    ip_list = FreeIP.objects.all()[:60]
    ip_list_total = FreeIP.objects.all()
    ip_count = len(ip_list_total)
    ip_lastcheck = ip_list_total[0].date_time
    ip_type = 'HTTPS'
    ip_timeout = ip_list_total[0].timeout

    return render(request, 'articles/ip_table.html', {'ip_count': ip_count,
                                                      'ip_lastcheck': ip_lastcheck,
                                                      'ip_type': ip_type,
                                                      'ip_timeout': ip_timeout,
                                                      'ip_list': ip_list
                                                      })


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
