from asyncio import exceptions
from email.errors import MissingHeaderBodySeparatorDefect
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from mainapp.models import Software
from django.views.generic import View,TemplateView
from django.contrib.auth.models import User
# Create your views here.
class Dashboard(TemplateView):
  model = User
  template_name = 'mainapp/dashboard.html'
  def get_context_data(self, *args, **kwargs):
    context =super(Dashboard,self).get_context_data( *args, **kwargs)
    context['users'] =  User.objects.all()
    return context

def home(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    else:
        request.session.set_test_cookie()
        messages.error(request, 'Please enable cookie')
    software = Software.objects.all()
    return render(request, 'mainapp/home.html',{'software':software} )

def login(request):
     # set new data
    request.session['user_id'] = 20
    request.session['user'] = 'Joshua'
    print(request.session['user'])
    return render(request,"users/login.html")

# def logout(request):
#     try:
#         del request.session['user_id']
#         del request.session['user']
#     except KeyError:
#         pass

#     return HttpResponse("Session Data cleared")

''' 
  1. God of mercy and compassion,
    look with pitty upon me;
    father let me call thee father,
    this thy child returns to theee.

    chorus:
        Jesus Lord, i ask for mercy,
        let me not implore in vain;
        all my sins i now detest them, 
        never will i sin again 

   2. by my sins i have deserve death,
    and endless misery
    hell with all its pain and toments, 
    and for all eternity
  
  3. by my sins i have abandoned Right and claim to heaven above
  where the saints rejoice forever'
  in a boundless sea of love

  4. see our savior bleeding, dying
  on the crose of calvary,
  to that cross my sins have nailed him
  yet he bleeds and dies for me
    '''