from django.http.response import JsonResponse
from django.shortcuts import render
from .models import UserModel
from .forms import UserRegistration
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


def home_index(request):
    form = UserRegistration()
    users = UserModel.objects.all()
    context = {
        'form': form,
        'users': users,
    }
    return render(request, 'enroll/home.html', context)


# INSERT DATA USING AJAX
def save_data(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            # THIS request.POST['name'] comes fron ajax.html
            user_id = request.POST.get('user_id')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            if (user_id == ''):
                user = UserModel(name=name, email=email, password=password)
            else:
                user = UserModel(id=user_id, name=name,
                                 email=email, password=password)

            user.save()

            user = UserModel.objects.values()
            user_data = list(user)

            return JsonResponse({
                'status': 'Save',
                'response': user_data,
            })
        else:
            return JsonResponse({
                'status': 0,
            })


# DELETE DATA USING AJAX
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('user_id')
        print(id)
        instance = UserModel.objects.get(pk=id)
        instance.delete()
        return JsonResponse({
            'status': True,
        })
    else:
        return JsonResponse({
            'status': False,
        })


# EDIT DATA USING AJAX
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('user_id')
        instance = UserModel.objects.get(pk=id)
        user_data = {
            'id': instance.id,
            'name': instance.name,
            'email': instance.email,
            'password': instance.password,
        }
        return JsonResponse(user_data)
