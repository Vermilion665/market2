from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from market.settings import LOGIN_REDIRECT_URL
from .forms import AuthForm



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)  ## То, что берется из запроса
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})

# так внутри создается пользователь - создается запись во встроенной таблице User
# user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")


def log_in(request):
    form = AuthForm(request, data=request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            print(url)
            return redirect(url)

    return render(request, 'users/login.html', {'form': form})


def log_out(request):
    logout(request)
    url = reverse('myapp:index')
    return redirect(url)
