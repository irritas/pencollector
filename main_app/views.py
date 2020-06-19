from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pen, Ink
from .forms import RefillForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pens_index(request):
	pens = Pen.objects.all()
	return render(request, 'pens/index.html', {'pens': pens})

def pens_detail(request, pen_id):
	pen = Pen.objects.get(id=pen_id)
	inks_pen_doesnt_have = Ink.objects.exclude(id__in = pen.inks.all().values_list('id'))
	refill_form = RefillForm()
	return render(request, 'pens/detail.html', {
		'pen': pen, 'refill_form': refill_form,
		'inks': inks_pen_doesnt_have
	})

def assoc_ink(request, pen_id, ink_id):
	Pen.objects.get(id=pen_id).inks.add(ink_id)
	return redirect('detail', pen_id=pen_id)

class PenCreate(CreateView):
	model = Pen
	fields = '__all__'

class PenUpdate(UpdateView):
	model = Pen
	fields = ['brand', 'style', 'features']

class PenDelete(DeleteView):
	model = Pen
	success_url = '/pens/'

def add_refill(request, pen_id):
	form = RefillForm(request.POST)
	if form.is_valid():
		new_refill = form.save(commit=False)
		new_refill.pen_id = pen_id
		new_refill.save()
	return redirect('detail', pen_id=pen_id)

class InkList(ListView):
	model = Ink

class InkDetail(DetailView):
	model = Ink

class InkCreate(CreateView):
	model = Ink
	fields = '__all__'

class InkUpdate(UpdateView):
	model = Ink
	fields = ['name', 'color']

class InkDelete(DeleteView):
	model = Ink
	success_url = '/inks/'