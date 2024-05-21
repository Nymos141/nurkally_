from django.shortcuts import render, get_object_or_404
from .models import Information, Employees, PageType

def main(request):
    if request.method == "GET":
        main_page = Information.objects.filter(page_type=1)
        context = {
            'page_title': 'Главная страница',
            'main_page': main_page
        }
        return render(request, 'main.html', context)

def faculty_history(request):
    if request.method == "GET":
        history_model = Information.objects.filter(page_type=2)
        context = {
            'page_title': 'История кафедры',
            'faculty_history': history_model
        }
        return render(request, 'kl_history.html', context)

def faculty_members(request):
    if request.method == "GET":
        members = Employees.objects.all()
        context = {
            'page_title': 'Состав кафедры',
            'faculty_members': members
        }
        return render(request, 'professors.html', context)

def professors_detail(request, professor_id):
    professor = Employees.objects.get(id=professor_id)
    context = {
        'professor': professor
    }
    return render(request, 'detail.html', context)

def applicant(request):
    if request.method == "GET":
        context = {
            'page_title': 'Абитуриенту'
        }
        return render(request, 'buclet.html', context)

def methodological_work(request):
    if request.method == "GET":
        context = {
            'page_title': 'Методическая работа'
        }
        return render(request, 'methodological.html', context)

def research_work(request):
    if request.method == "GET":
        research_w = Information.objects.filter(page_type=3)
        context = {
            'page_title': 'Научно-исследовательская работа',
            'research_w': research_w
        }
        return render(request, 'research_work.html', context)

def international_cooperation(request):
    if request.method == "GET":
        cooperation = Information.objects.filter(page_type=4)
        context = {
            'page_title': 'Международное сотрудничество',
            'international_cooperation': cooperation
        }
        return render(request, 'collaboration.html', context)

def educational_work(request):
    if request.method == 'GET':
        context = {
            'page_title': 'Воспитательная работа'
        }
        return render(request, 'education.html', context)

def employment(request):
    if request.method == 'GET':
        placement = Information.objects.filter(page_type=5)
        context = {
            'page_title': 'Трудоустройство',
            'placement': placement
        }
        return render(request, 'placement.html', context)
