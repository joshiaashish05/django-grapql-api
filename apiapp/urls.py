from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
urlpatterns = [
    path('graphql1/', jwt_cookie(GraphQLView.as_view(graphiql=True))),
]
