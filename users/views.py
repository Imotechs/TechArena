from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from users.models import Student
from . forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,studentRegistrationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import Student
from django.contrib.auth.decorators import login_required
from .import functions
# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username','email')
            messages.success(request, f' Account for {username} was created!  Login Now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form":form,"title":"User Registration"})


class studentRegistration(LoginRequiredMixin,CreateView):

    model = Student
    fields = ['software','image'] 
    success_url = '/account/profile/'
    template_name ='users/studentregister.html'
    def form_valid(self, form):
        pk = self.request.user
        obj = Student.objects.filter(user=pk)
        if obj:
            student_id = obj[0].student_id
            print(student_id)
            messages.info(self.request,f"Student has previousely Registered with  Registration ID = {student_id}")
            messages.error(self.request,f'Pls Logout {pk} to Register Another user')
            return HttpResponse(f"<h3 style='color:red; margin:10% 30% 30% 30%'>Student has previousely Registered with <br/> Registration ID = <strong style='color:cyan;'>{student_id}<br> Pls Logout to Register Another user</strong></h2>")
        
        form.instance.user = self.request.user
        form.instance.student_id = functions.get_student_id()
        messages.info(self.request,f'Registration was Succesful, your student_id is {form.instance.student_id}')

        return super().form_valid(form)

@login_required
def profile(request):
    try:
        if request.method == 'POST':
            U_form = UserUpdateForm(request.POST, instance= request.user)
            P_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance = request.user.student)
            S_form =studentRegistrationForm(request.POST,instance = request.user.student)

            if U_form.is_valid() and P_form.is_valid() and S_form.is_valid():
                U_form.save()
                P_form.save()
                S_form.save()
                print(S_form)
                messages.success(request, f'{request.user.username} profile was updated!')
                return redirect ('profile')
    except AttributeError as erro:
        print('Error:'+ str(erro))
        return redirect ('login')
    try:
        U_form = UserUpdateForm(instance= request.user)
        P_form = ProfileUpdateForm(instance= request.user)
        S_form =studentRegistrationForm(request.POST,instance=request.user)
        student = Student.objects.filter(user=request.user)
        student_id = student[0].student_id
        student_img = student[0].image
        software = student[0].software
        print(software)
        print(student_img)
        context = {
            'software':software,
            'student_img':student_img,
            'student_id':student_id,
            "U_form": U_form,
            "P_form": P_form,
            'S_form':S_form,
            "title": "my account's Profile"
        }
        return render(request, 'users/profile.html',context)
    except IndexError:
         return redirect('studentregister')
    # except Exception as err:
    #     print('myError:'+ str(err))
    #     return redirect ('makeprofile')
    
    

def usersprofile(request):
    user = User.objects.get(username = request.user)
    context = {'user':user}
    return render(request, 'users/userprofiles.html', context)


def logoutView(request):

    return render(request, 'users/logoutview.html')