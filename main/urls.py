from django.urls import path
from . import views
from main.models import Publisher

object_list_view = views.ObjectListView.as_view(
    queryset=Publisher.objects.order_by("imprint")[:5],  # :5 limits the results to the five most recent
    context_object_name="object_list",
    template_name="list.html",
)

urlpatterns = [
    path("publisher/", object_list_view, name="publisher"),
    path("journal/", views.input_data, name="journal"),
]