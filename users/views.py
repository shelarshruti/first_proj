from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
# Create your views here.


def loginfun(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'userTemp/login.html', {'msg': 'Invalid username or password'})

    else:
        return render(request, 'userTemp/login.html')



def logoutfun(request):
    logout(request)
    return redirect('login')


def registration(request):
    msg = ''
    if request.method == 'POST':

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            msg = 'Registration Done'
            return render(request, 'userTemp/registration.html', {'msg': msg} )
        else:
            msg = 'Passwords are not matching'
            return render(request, 'userTemp/registration.html', {'msg': msg} )

    else:
        return render(request, 'userTemp/registration.html')
