from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseNotFound
from .models import DiaryEntry
from .forms import EntryCreationForm, EditorForm
from user.forms import UserConfigForm

def entry_required(f):
    def wrap_function(request, entry_id, *args, **kwargs):
        try:
            entryInstance = DiaryEntry.objects.get(uuid=entry_id, author=request.user)
        except:
            return HttpResponseNotFound('Entry missing')
        return f(request, entry_id, *args, **kwargs, entryInstance=entryInstance)
    return wrap_function


# @login_required
def dashboard(request):
    if request.user.is_authenticated:
        # if you're logged in and you POSTed a form...
        if request.method == 'POST':
            # is it a creation form?
            # if 'creation_form' in request.POST:
            form = EntryCreationForm(request.POST)
            if form.is_valid():
                newEntry = DiaryEntry(title=form.cleaned_data['title'],
                    location=form.cleaned_data['location'],
                    mood=form.cleaned_data['mood'], author=request.user)
                newEntry.save()
                return redirect('edit_entry', entry_id=newEntry.uuid)
            # if 'config_form' in request.POST:
                # user.views.save_user_config(request.POST, request.user)

        # if method is GET
        entryList = DiaryEntry.objects.filter(author=request.user).order_by('date_time')
        creationForm = EntryCreationForm(initial={'mood': '2'})
        configForm = UserConfigForm(initial={'theme': request.user.theme, 'font_size': request.user.font_size})
        return render(request, 'diary/dashboard.html', {'entry_list': entryList,
            'creation_form': creationForm, 'config_form': configForm,
            'api_domain': settings.GEOLOCATION_API_DOMAIN,
            'api_key': settings.GEOLOCATION_API_KEY})
    else:
        return render(request, 'diary/dashboard.html', {})

@login_required
@entry_required
def entry(request, entry_id, entryInstance):
    return render(request, 'diary/entry.html', {'entry': entryInstance})

@login_required
@entry_required
def edit_entry(request, entry_id, entryInstance):
    if request.method == 'POST':
        # is it an autosave update from a JS script?
        # if 'is_autosave_update' in request.POST:
        #     entryInstance.content = request.POST['content']
        #     entryInstance.save()
        #     return JsonResponse(data={}, status=200)

        # is it an entry saving form?
        if 'save_form' in request.POST:
            form = EditorForm(request.POST)
            if form._errors:
                return redirect('missing', {'error': form._errors})
            content = form.data['editor']
            # files = form.files
            entryInstance.content = content
            entryInstance.save()
            return redirect('dashboard')
        # or is it an entry deleting form?
        if 'delete_form' in request.POST:
            entryToDelete = DiaryEntry.objects.get(uuid=entry_id, author=request.user)
            # imagesToDelete = Image.objects.filter(entry=entryToDelete)
            # imagesToDelete.delete()
            entryToDelete.delete()
            return redirect('dashboard')
    # if method is GET
    form = EditorForm()
    return render(request, 'diary/edit_entry.html', {'entry': entryInstance, 'form': form})
