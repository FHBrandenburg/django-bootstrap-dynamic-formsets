Dynamic Formsets for Django with Bootstrap
==========================================

Requirements:
-------------

-  **django-bootstrap3**
-  **jQuery**
-  **jQuery UI**

Installation:
-------------

-  pip install django-bootstrap-dynamic-formsets

Usage:
------

-  Add django\_bootstrap\_dynamic\_formsets to Applications in your
   **settings.py**. If you haven't done so already, add
   django-bootstrap3 as well.

-  Create a regular model, form and formset. If you need dynamic order
   functionality, in the ``fields`` parameter of the formset factory, do
   not include a custom order field. Instead, set ``can_order`` to True.
   Set ``can_delete`` to True as well, if you wish to be able to delete
   forms.

-  Write your view as you would for a regular formset, with one
   exception:

   -  If ``can_order`` is True,you need to specifically save the order,
      Django will not do this for you! Check out the example below.

-  In your template, load the custom template tag library.

   -  ``{% load bootstrap_dynamic_formsets %}``

-  Use the provided custom tag where you'd like to place the formset.

   -  ``{% bootstrap_dynamic_formset formset can_order=True can_delete=True layout="horizontal" %}``
   -  where ``formset`` is your formset and
   -  ``can_order`` and ``can_delete`` are set accordingly to how you
      set them in your formset. Their default value if you don't specify
      anything is ``False``
   -  Optionally, you can add the ``form_wrapper`` parameter. This is
      the class that surrounds every form instance. Default:
      ``form_wrapper="well"``
   -  Also optionally, you can choose which Bootstrap form layout to
      use. Options are ``""``, ``"inline"`` or ``"horizontal"``

-  Make sure you don't forget to include jQuery and jQuery UI in your
   template.
-  The form submit button has to have the id ``form-submit``

-  In your browser

   -  Order forms by dragging and dropping them. You can grab them on
      the move icon.
   -  Alternatively, you can use the up/down buttons.
   -  Delete a form by clicking on the trash icon. It will disappear.
      You cannot undo this. However, the database will only be changed
      if you click submit.
   -  Add a new form below the current one by clicking the plus icon.
   -  Submit the changed data by hitting submit.

Example:
--------

For this example, we are going to use a simple model called ``Album``:

**models.py**

::

    ...
    class Album(models.Model):
        artist = models.CharField(max_length=75)
        name = models.CharField(max_length=100)
        release = models.DateField()
        order = models.IntegerField(blank=True, null=True)
    ...

To make this simple, let's use a model formset instead of creating a
custom form and formset. Also, add everything else that is needed for
your view.

**views.py**

::

    ...
    def manage_albums(request):
        AlbumFormSet = modelformset_factory(Album, can_order=True, can_delete= True,
                                            fields=['artist','name','release',])
        if request.method == 'POST':
            formset = AlbumFormSet(request.POST, request.FILES)
            if formset.is_valid():
                for form in formset.ordered_forms:
                    form.instance.order = form.cleaned_data['ORDER']
                formset.save()
                messages.success(request, u"Formset edited successfully.")
                return HttpResponseRedirect(reverse('formsets'))
            else:
                messages.error(request, u"Please correct the errors below.")


        else:
            formset = AlbumFormSet(queryset=Album.objects.order_by('order'))
        return render(request, 'manage_albums.html', {'formset': formset})
    ...

Notice a few things:

-  ``order`` is not included in ``fields``
-  The for-loop is necessary to save the order. Just calling
   ``formset.save()`` will not save it.

Finally, let's write the template. This is actually very easy:

**manage\_albums.html**

::

    ...
    {% load bootstrap_dynamic_formsets %}
    ...
    {% bootstrap_dynamic_formset formset %}
    ...

That's it!

Thanks to all contributors:
---------------------------

-   mattions
