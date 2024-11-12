from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path ('',views.Index, name='home'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name='register'),
    path('logout/',views.LogoutGetView.as_view(),name='logout'),
    path('introducao_pc/', views.Introducao_Pc, name='Intro_Pc'),
    path('Fundamento_antrofilofico/', views.Fundamentos_antrofilosoficos_da_educacao, name='fundamento_antro'),
    path('Metologia_cientifica/',views.Metodologia_cientifica, name='Metologia_cientifica'),
    path('calculo_1/', views.Calculo_1, name='calculo_1'),
    path('Matematica_Discreta', views.Matematica_Discreta, name='Matematica_discreta'),
path("Introducao_programacao/", views.Introducao_programacao, name="intro_programa")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)