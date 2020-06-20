from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Country,State,City,Account
from .form import CountryForm,StateForm,CityForm,AccountForm,LoginForm,PostForm,SearchForm,CountrySearch,EditAccountForm
from blog.models import Post
from .fliters import PostFilter,StateFilter,CountryFilter,CityFilter,UserFilter


@login_required(login_url='accounts:login')
def Models(request):
    return render(request,'accounts/models.html')

@login_required(login_url='accounts:login')
def post_list(request,status=None):
    posts = Post.objects.all()
    myFilter = PostFilter(request.GET,queryset=posts)
    posts = myFilter.qs
    context = {
        'posts':posts,
        'myFilter':myFilter,
    }
    return render(request,'accounts/posts/list.html',context)

@login_required(login_url='accounts:login')
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:post_list')
    context = {
        'form':form,
        'title':'Add Post'
    }
    return render(request,'accounts/posts/create.html',context)

@login_required(login_url='accounts:login')
def edit_post(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            state = form.save(commit=False)
            state.save()
            return redirect('accounts:post_list')
    else:
        form=PostForm(instance=post)
    context = {
        'form':form,
        'title':'Add Post'
    }
    return render(request,'accounts/posts/create.html',context)

@login_required(login_url='accounts:login')
def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('accounts:post_list')

def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['Email']
            password = data['Password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                print(user.username)
                return redirect('accounts:models')
            else:
                error="Invalid login"
                print(error)
        else:
            error="Invalid login"
            print(error)
    else:
        form = LoginForm()
        error = None
    context = {
        'form':form,
        'error':error,
    }
    return render(request,'accounts/users/login.html',context)


@login_required(login_url='accounts:login')
def country_list(request):
    countries = Country.objects.all()
    myFilter = CountryFilter(request.GET,queryset=countries)
    countries = myFilter.qs
    context = {
        'countries':countries,
        'myFilter':myFilter,
    }
    return render(request,'accounts/country/list.html',context)

@login_required(login_url='accounts:login')
def country_delete(request,id):
    country = Country.objects.get(id=id)
    country.delete()
    return redirect('accounts:Country_List')

@login_required(login_url='accounts:login')
def edit_country(request,id):
    country = Country.objects.get(id=id)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            return redirect('accounts:Country_List')
    else:
        form = CountryForm(instance=country)
    context = {
        'form':form,
        'title':'Edit Country'
    }
    return render(request,'accounts/country/create.html',context)

@login_required(login_url='accounts:login')
def create_country(request):
    form = CountryForm()
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:Country_List')
    context={
        'form':form,
        'title':'Add Country'
    }

    return render(request,'accounts/country/create.html',context)

@login_required(login_url='accounts:login')
def state_list(request):
    states = State.objects.all()
    myFilter = StateFilter(request.GET,queryset=states)
    states = myFilter.qs
    context = {
        'states':states,
        'myFilter':myFilter
    }
    return render(request,'accounts/State/list.html',context)

@login_required(login_url='accounts:login')
def state_create(request):
    form = StateForm()
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:state_list')
    context={
        'form':form,
        'title':'Add State'
    }

    return render(request,'accounts/State/create.html',context)

@login_required(login_url='accounts:login')
def state_delete(request,id):
    state = State.objects.get(id=id)
    state.delete()
    return redirect('accounts:state_list')

@login_required(login_url='accounts:login')
def edit_state(request,id):
    state = State.objects.get(id=id)
    if request.method == 'POST':
        form = StateForm(request.POST,instance=state)
        if form.is_valid():
            state = form.save(commit=False)
            state.save()
            return redirect('accounts:state_list')
    else:
        form = StateForm(instance=state)
    context={
        'form':form,
        'title':'Edit State'
    }
    return render(request,'accounts/State/create.html',context)

@login_required(login_url='accounts:login')
def city_list(request):
    cities = City.objects.all()
    form = SearchForm()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            search = data['search']
            if search != '':
                cities = City.objects.filter(name=search)
    context={
        'cities':cities,
        'form':form,
    }
    return render(request,'accounts/City/list.html',context)

@login_required(login_url='accounts:login')
def city_add(request):
    form = CityForm()
    if request.method == 'POST':
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:city_list')
    context = {
        'form':form,
        'title':'Add City'
    }
    return render(request,'accounts/City/create.html',context)

@login_required(login_url='accounts:login')
def city_delete(request,id):
    city = City.objects.get(id=id)
    city.delete()
    return redirect('accounts:city_list')

@login_required(login_url='accounts:login')
def city_edit(request,id):
    city = City.objects.get(id=id)
    if request.method == 'POST':
        form = CityForm(request.POST,instance=city)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return redirect('accounts:city_list')
    else:
        form = CityForm(instance=city)
    context = {
        'form':form,
        'title':'Edit City'
    }
    return  render(request,'accounts/City/create.html',context)

@login_required(login_url='accounts:login')
def user_list(request):
    users = Account.objects.all()
    myFilter = UserFilter(request.GET,queryset=users)
    users = myFilter.qs
    context = {
        'users':users,
        'myFilter':myFilter,
    }
    return render(request,'accounts/users/list.html',context)

@login_required(login_url='accounts:login')
def add_user(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_list')
    context = {
        'form':form,
        'title':'Add User',
    }
    return render(request,'accounts/users/create.html',context)

@login_required(login_url='accounts:login')
def edit_user(request,id):
    user = Account.objects.get(id=id)
    if request.method == 'POST':
        form = EditAccountForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('accounts:user_list')
    else:
        form = EditAccountForm(instance=user)
    context = {
        'form':form,
        'title':'Edit User',
    }
    return render(request,'accounts/users/create.html',context)

@login_required(login_url='accounts:login')
def delete_user(redirect,id):
    account = Account.objects.get(id=id)
    account.is_active = False
    account.save()
    return redirect('accounts:user_list')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')


