from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from kafedra.views import (main, faculty_history, applicant, faculty_members,
                           professors_detail, methodological_work, research_work,
                           international_cooperation, educational_work, employment)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('faculty_history/', faculty_history, name='faculty_history'),
    path('buclet/', applicant, name='buclet'),
    path('professors/', faculty_members, name='professors'),
    path('professor/<int:professor_id>/', professors_detail, name='professor_detail'),
    path('methodological/', methodological_work, name='methodological'),
    path('research_work/', research_work, name='research_work'),
    path('international_cooperation/', international_cooperation, name='international_cooperation'),
    path('educational_work/', educational_work, name='educational_work'),
    path('employment/', employment, name='employment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
