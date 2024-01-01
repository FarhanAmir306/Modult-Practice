from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from accounts.models import UserAccount
from posts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Profile,Post
from django.shortcuts import get_object_or_404
from django.contrib import messages
# from datetime import datetime
# from django.db.models import Sum
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string



def send_transaction_mail(user,amount,subject,template):
        
        massage=render_to_string(template,{
            'user':user,
            'amount':amount
        })
        send_email=EmailMultiAlternatives(subject,'',to=[user.email])
        send_email.attach_alternative(massage,'text/html')
        send_email.send()



class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')




def logout_view(request):
        logout(request)
        return redirect('home')
  


class UserBankAccountUpdateView(View):
    template_name = 'accounts/edit_profile_information.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})


    



# class ProfileView(LoginRequiredMixin, View):
#     template_name = "accounts/profile.html"

#     def get(self, request, *args, **kwargs):
#         # Make sure the user is authenticated
#         if not request.user.is_authenticated:
#             return render(request, 'accounts/login.html')
#         else:
#             user_accounts = UserAccount.objects.all()
#             return render(request, self.template_name, {'user_accounts': user_accounts})


def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    book_post = user_profile.book_post.all()
    return render(request, 'accounts/profile.html', {'books': book_post})
        
def BookBuy(request,id):
    user_account = get_object_or_404(UserAccount, user=request.user)
    post=Post.objects.filter(id=id).first()
    book_price=post.price
   
    if user_account.balance >=book_price:
        user_account.balance -= book_price
        user_profile, created = Profile.objects.get_or_create(user=request.user)
        user_profile.book_post.add(post)
        user_account.save(update_fields=["balance"])
        messages.success(request,"Purchase The Book Successfully !")
        send_transaction_mail(request.user,book_price,'Purchase Book','accounts/buying_mail.html')

    else:
        messages.error(request,"Your Balance is Not enough for the book buying")

    return redirect('profile')


    
    
