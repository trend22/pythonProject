from django.urls import path

from . import views


# для того, чтобы псевдонимы 'detail' различать и не путать в разных приложениях
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # для перехода на определённую статью
    path('<int:article_id>', views.detail, name='detail'),
    # для создания комментария
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment')

]