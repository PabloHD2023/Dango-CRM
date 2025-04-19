from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm, AddRecordForm
from .models import Record

def home(request):

      records = Record.objects.all()
      #Check to see if the user is authenticated
      
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
                  messages.error(request, 'El usuario o la clave son incorrectas, por favor vuelva a intentar...')
                  return redirect('home')
      else:
            return render(request, 'home.html', {'records': records})


def logout_user(request):
      logout(request)
      messages.success(request, 'Se ha desconectado correctamente. Hasta luego!')
      return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SingUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SingUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
      if request.user.is_authenticated:
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
      else:
            messages.error(request, 'Por favor inicie sesión para ver el registro del cliente.')
            return redirect('home')
      

def delete_record(request, pk):
      if request.user.is_authenticated:
            customer_record = Record.objects.get(id=pk)
            customer_record.delete()
            messages.success(request, 'El registro del cliente ha sido eliminado correctamente.')
            return redirect('home')
      else:
            messages.error(request, 'Por favor inicie sesión para eliminar el registro del cliente.')
            return redirect('home')
      
def add_record(request):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  form = AddRecordForm(request.POST)
                  if form.is_valid():
                        form.save()
                        messages.success(request, 'El registro del cliente ha sido creado correctamente.')
                        return redirect('home')
            else:
                  form = AddRecordForm()
                  return render(request, 'add_record.html', {'form': form})
      else:
            messages.error(request, 'Por favor inicie sesión para agregar un nuevo registro de cliente.')
            return redirect('home')

def update_record(request, pk):
      if request.user.is_authenticated:
            customer_record = Record.objects.get(id=pk)
            if request.method == 'POST':
                  form = AddRecordForm(request.POST, instance=customer_record)
                  if form.is_valid():
                        form.save()
                        messages.success(request, 'El registro del cliente ha sido actualizado correctamente.')
                        return redirect('home')
            else:
                  form = AddRecordForm(instance=customer_record)
                  return render(request, 'update_record.html', {'form': form})
      else:
            messages.error(request, 'Por favor inicie sesión para actualizar el registro del cliente.')
            return redirect('home')


      
      