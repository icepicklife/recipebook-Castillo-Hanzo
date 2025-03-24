from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

from django.urls import reverse_lazy, reverse


class RecipeListView(ListView):

    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):

    model = Recipe
    template_name = "recipe_soloview.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):

    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)


class RecipeImageCreateView(LoginRequiredMixin, CreateView):

    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'add_recipeimage.html'

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        recipe_image = form.save(commit=False)
        recipe_image.recipe = recipe
        recipe_image.save()
        return redirect('ledger:recipe-detail', pk=recipe.pk)
    
    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe-detail',
            kwargs={'pk': self.kwargs['pk']}
        )
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return ctx


class RecipeUpdateView(UpdateView):

    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_soloview.html'


class RecipeImageUpdateView(UpdateView):

    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_soloview.html'