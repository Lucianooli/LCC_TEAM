from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserRegisterForm,CustomAuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Pdf,Desafio


def Index(request):
    return render(request,'lcc_app/index.html')


class LogoutGetView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
def login(request):

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Você foi logado com sucesso.')

            # Redireciona para a página que o usuário tentou acessar, se houver
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')  # Ou a página padrão após o login
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        form = CustomAuthenticationForm()

    return render(request,'lcc_app/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecione para a página de login ou outra página
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserRegisterForm()
    return render(request, 'lcc_app/register.html', {'form': form})

#@login_required
def Introducao_Pc(request):
    pdf_0 = Pdf.objects.get(id=1)
    pdf_1 = Pdf.objects.get(id=2)
    pdf_2 = Pdf.objects.get(id=3)
    pdf_3 = Pdf.objects.get(id=4)
    pdf_4 = Pdf.objects.get(id=5)
    pdf_5 = Pdf.objects.get(id=6)
    pdf_6 = Pdf.objects.get(id=7)
    desafio_0 = Desafio.objects.get(id=1)

    return render(request,'lcc_app/introducao_pc.html',{'pdf_0':pdf_0,'pdf_1':pdf_1,'pdf_2':pdf_2,'pdf_3':pdf_3,'pdf_4':pdf_4,'pdf_5':pdf_5,'pdf_6':pdf_6,'desafio_0':desafio_0})

def Fundamentos_antrofilosoficos_da_educacao(request):
    pdf_0 = Pdf.objects.get(id=8)
    pdf_1 = Pdf.objects.get(id=9)

    return render(request,'lcc_app/Fundamentos_antrofilosoficos_da_educacao.html',{'pdf_0':pdf_0,'pdf_1':pdf_1})
def Metodologia_cientifica(request):
    pdf_0 = Pdf.objects.get(id=10)
    return render(request,'lcc_app/Metologia_cientifica.html',{'pdf_0':pdf_0})
def Calculo_1(request):
    pdf_1 = Pdf.objects.get(id=11)
    pdf_2 = Pdf.objects.get(id=12)
    pdf_3 = Pdf.objects.get(id=13)
    pdf_4 = Pdf.objects.get(id=14)

    pdf_5 = Pdf.objects.get(id=15)
    pdf_6 = Pdf.objects.get(id=16)
    pdf_7 = Pdf.objects.get(id=17)
    pdf_8 = Pdf.objects.get(id=18)
    pdf_9 = Pdf.objects.get(id=19)
    pdf_10 = Pdf.objects.get(id=20)

    desafio_1 = Desafio.objects.get(id=2)
    desafio_2 = Desafio.objects.get(id=3)
    desafio_3 = Desafio.objects.get(id=4)
    desafio_4 = Desafio.objects.get(id=5)
    desafio_5 = Desafio.objects.get(id=6)

    pdf_11 = Pdf.objects.get(id=21)

    desafio_6 = Desafio.objects.get(id=7)

    
    return render(request,'lcc_app/calculo_1.html',{'pdf_1':pdf_1,'pdf_2':pdf_2,'pdf_3':pdf_3,'pdf_4':pdf_4,'desafio_1':desafio_1,'desafio_2':desafio_2,'desafio_3':desafio_3,
    'pdf_5':pdf_5,'pdf_6':pdf_6,'pdf_7':pdf_7,'pdf_8':pdf_8,'pdf_9':pdf_9,'pdf_10':pdf_10,'desafio_4':desafio_4,'desafio_5':desafio_5, 'pdf_11':pdf_11, 'desafio_6':desafio_6})