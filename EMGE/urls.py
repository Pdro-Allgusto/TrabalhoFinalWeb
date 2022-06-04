from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('alunos/', include('alunos.urls', namespace='alunos')),
    path('professores/', include('professores.urls', namespace='professores')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
