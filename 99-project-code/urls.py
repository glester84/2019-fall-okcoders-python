from django.contrib import admin
from django.urls import path

from Bingo_Game import views

urlpatterns = [
    path('ballcall/', views.BallCallView.as_view()),
    path('ballcall/<int:c>/', views.BallCallView.as_view()),
    path('admin/', admin.site.urls),
    path('card/', views.BingoCardView.as_view()),
    path('card/<int:c>/', views.BingoCardView.as_view()),
    path('buycard/<int:a>/<int:b>/<int:x>/', views.BuyCardView.as_view()),
    path('', views.PlayGameView.as_view()),
    path('result/', views.GameResultView.as_view()),
]
