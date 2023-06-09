from django.shortcuts import render, redirect
from .form import SignupForm, PasswordReset, PasswordConfirm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

auth_page = 'account/auth.html'

# Registration
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, auth_page, context)

# Login
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid credential')
        return self.render_to_response(self.get_context_data(form=form))

# Password Reset
class PasswordReset(PasswordResetView):
    form_class = PasswordReset

# Password Reset Confirm
class PasswordConfirm(PasswordResetConfirmView):
    form_class = PasswordConfirm
