from django.shortcuts import render
from app.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from app.models import Recipe,Review
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class RecipeList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Recipesearch(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]

    def list(self,request):
        query=self.request.query_params.get('search')
        if (query):
            rp=Recipe.objects.filter(Q(title__icontains=query) | Q(meal_type__icontains=query) | Q(cuisine__icontains=query))
            r=RecipeSerializer(rp,many=True)
            return Response(r.data)

        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



