from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User
from .forms import DictionaryForm
from .models import DictionaryModel


def dictionary_view(request):
    request.build_absolute_uri(request.path)
    form = DictionaryForm(request.POST)
    dict_objs = DictionaryModel.objects.all().order_by('-created_at')
    
    context = {"form": form, "dictionaries": dict_objs}
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                dict_obj = form.save(commit=False)
                dict_obj.user = request.user
                dict_obj.save()
            
            return HttpResponseRedirect('/dictionary/')

        else:
            form = DictionaryForm()
            
        return render(request, 'dictionary/index.html', context)
    else:
        return redirect('login')

def dictionary_update_view(request, id):
    dict_objs = DictionaryModel.objects.all()
    dict_obj = DictionaryModel.objects.get(id=id)
    
    form = DictionaryForm(instance=dict_obj)
    context = {"form": form, "dictionaries": dict_objs, "id": id}
    if request.method == 'POST':
        form = DictionaryForm(request.POST, instance=dict_obj)
        if form.is_valid():
            form.save()
            return redirect('/dictionary/')
            
    return render(request, 'dictionary/update.html', context)

def dictionary_delete_view(request, id):
    
    dict_obj = DictionaryModel.objects.get(id=id)
    dict_obj.delete() 
    if request.method == 'POST':
        dict_obj.delete() 

    return redirect('/dictionary/')


def dictionary_search_view(request):
    dict_objs = DictionaryModel.objects.all()
    
    word = request.POST.get('word')
    
    if word != '' and word is not None:
        dict_objs = dict_objs.filter(word__icontains=word)
        
        return render(request, 'dictionary/index.html', {"dictionaries": dict_objs})

    else:
        return render(request, 'dictionary/index.html', {"dictionaries": dict_objs}) 