from django.urls import path
from .views import (
    RecipeListView,
    RecipeCreateView,
    RecipeImageCreateView,
    RecipeUpdateView,
)

urlpatterns = [
    path("recipes/list", RecipeListView.as_view(), name="recipe_list"),
    path("recipe/<int:pk>", RecipeUpdateView.as_view(), name="recipe-detail"),
    path("recipe/add", RecipeCreateView.as_view(), name="add_recipe"),
]

urlpatterns += [
    path(
        "recipe/<int:pk>/add_image",
        RecipeImageCreateView.as_view(),
        name="add_recipeimage",
    ),
]
app_name = "ledger"
