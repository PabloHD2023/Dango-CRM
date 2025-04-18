from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
   #Check o see if logging in
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          #Authenticate the user
          user = authenticate(request, username=username, password=password)
          if user is not None:
                login(request, user)
                messages.success(request, 'Se ha conectado correctamente. Bienvenido!')
                return redirect('home')
          else:
                messages.error(request, 'El usuario o la clave son correctas, por favor vuelva a intentar...')
                return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Se ha desconectado correctamente. Hasta luego!')
    return redirect('home')

