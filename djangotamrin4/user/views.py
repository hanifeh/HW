from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from user import forms, models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def create_user(request):
    form_instance = forms.UserForm()

    if request.method == 'POST':
        form_instance = forms.UserForm(data=request.POST)
        print(form_instance)
        if form_instance.is_valid():
            form_instance.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
    return render(request, 'create_user.html', {'form': form_instance})


@csrf_exempt
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', None)
        obj = models.MyUser.objects.filter(first_name__contains=searched)
        if obj:
            # user = obj[0]
            # first = user.first_name
            # last = user.last_name
            # number = user.phone_number
            return JsonResponse({
                    # 'first': f'first name : {first}',
                    # 'last': f'last name : {last}',
                    # 'number': f'phone number : {number}',
                    'results': list(obj.values())
                })
        else:
            return JsonResponse({'result': "phone number not found !"})
    else:
        return render(request, 'search.html', {})
