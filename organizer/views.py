from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from organizer.forms import StartupForm, TagForm, NewsLinkForm
from .models import Startup, Tag, NewsLink

from .utils import ObjectCreateMixin


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = (
        'orgnizer/newslink_form_update.html'
    )

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink,pk=pk)
        context = {
            'form': self.form_class(
                instance=newslink),
             'newslink': newslink,
        }
        return render(
            request, self.template_name, context)


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup})


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all})


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})

