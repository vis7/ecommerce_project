from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm
from .models import CustomUser
from ecommerce_app.models import Cart


# Create your views here.
def registration(request):
    """
    It takes data of user and register User
        - It also create cart for user at the time of registration
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # create cart for user
            Cart.objects.create(user=user)

            return redirect('accounts:login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration.html', context=context)


def login(request):
    """
    This view login user using email and password,
        - It will throw error if user not exist with provided email
        - It will raise error if password not matched with user
        - it store user_email in session which will be further used in extract user and check that if user is logged in or not
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.filter(email=email).first()
            is_authorised = check_password(password, user.password)
            if user and is_authorised:
                request.session['user_email'] = user.email
                return redirect('ecommerce_app:index')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)


def logout(request):
    """
    It logout user.
        - It also delete 'user_email' session variable which is used to vefify user is logged in or not and extract user letter for use
    """
    del request.session['user_email']
    return redirect('accounts:login')


def user_list(request):
    """
    This view provide list of users
        - It also provide feature to activate/deactivate user
        - It allow admin to promote user to "Admin" role
    """
    users = CustomUser.objects.all()

    user_email = request.session.get('user_email')
    user = CustomUser.objects.filter(email=user_email).first()

    if user and user.role == CustomUser.ADMIN:
        if request.method == 'POST':
            if 'activate_users' in request.POST:
                user_ids = request.POST.getlist('selected_user_ids', [])
                CustomUser.objects.filter(id__in=user_ids).update(is_active=True)
                return redirect('accounts:user_list')
            if 'deactivate_users' in request.POST:
                user_ids = request.POST.getlist('selected_user_ids', [])
                CustomUser.objects.filter(id__in=user_ids).update(is_active=False)
                return redirect('accounts:user_list')
            if 'promote_to_admin' in request.POST:
                user_ids = request.POST.getlist('selected_user_ids', [])
                CustomUser.objects.filter(id__in=user_ids).update(role=CustomUser.ADMIN)
                return redirect('accounts:user_list')
    else:
        return redirect('accounts:login')

    context = {
        "users": users
    }
    return render(request, 'accounts/user_list.html', context=context)

