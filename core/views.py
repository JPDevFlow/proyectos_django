from django.shortcuts import render, HttpResponse

html_base ='''
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Potrada</a></li>
    <li><a href="/about">Acerca de</a></li>
</ul>
'''
# Create your views here.

def home(request):
    return HttpResponse(html_base+"""
                        <h2>Portada</h2>
                        <p>Esto es la portada</p>""")

def about(request):
    return HttpResponse(html_base+"""
                        <h2>Acerca de</h2>
                        <p>Me llamo JPDevFlow soy programdor y desarrolador web</p>""")