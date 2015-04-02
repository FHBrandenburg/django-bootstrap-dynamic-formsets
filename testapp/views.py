from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib import messages
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.shortcuts import render
from testapp.models import *

def manage_articles(request):
    AlbumFormSet = modelformset_factory(Album, max_num=1, can_order=True, can_delete= True,
                                        fields=['artist','name','release',])
    if request.method == 'POST':
        formset = AlbumFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            for form in formset.ordered_forms:
                form.instance.order = form.cleaned_data['ORDER']
            formset.save()
            messages.success(request, u"Formset edited successfully.")
            return HttpResponseRedirect(reverse('formsets'))
        else:
            messages.error(request, u"Please correct the errors below.")


    else:
        formset = AlbumFormSet(queryset=Album.objects.order_by('order'))
    # return render_to_response('testapp/manage_articles.html', {'formset': formset})
    return render(request, 'testapp/manage_articles.html', {'formset': formset})