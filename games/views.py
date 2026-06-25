from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer
from .permissions import Permission
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

    

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, Permission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['genre']
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

