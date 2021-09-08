from django.shortcuts import render, HttpResponse,redirect

# Create your views here.


def auth(func):
    def inner(request, *args,**kwars):
        if not request.session.get('is_login'):
            return (redirect('/login/'))
        else:
            return(func(request))
    return(inner)

@auth
def home(request):
    if request.method =='GET':
        return (render(request,'home.html'))


def login(request):
    if request.method =='GET':
        return(render(request,'login.html'))
    else:
        uname=request.POST.get('username')
        pwd = request.POST.get('password')
        if uname == 'alex' and pwd =='123':
            print('23243')
            request.session['is_login'] = True
            return(redirect('/home/'))
        else:
            return(render(request,'login.html'))
