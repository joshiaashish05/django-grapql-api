import graphene
# from graphene import relay
from graphene_django.types import DjangoObjectType
from .models import Director
from movieapp.models import Movie
import graphql_jwt
from graphql_jwt.decorators import login_required
# from graphene_django.filter import DjangoFilterConnectionField


class MoviesType(DjangoObjectType):
    class Meta:
        model = Movie

    movie_watch = graphene.String()

    def resolve_movie_watch(self, info):
        if self.watch is True:
            return "Movie watched"
        else:
            return "Movie not watch "


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class Query(graphene.ObjectType):
    all_movies = graphene.List(MoviesType)
    movie = graphene.Field(MoviesType, id=graphene.Int(), title=graphene.String())

    all_director = graphene.List(DirectorType)

    def resolve_all_director(self, info, **kwargs):
        return Director.objects.all()

    @login_required
    def resolve_all_movies(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
           raise Exception('Auth creditials were not provided')
        else:
            return Movie.objects.all()

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Movie.objects.get(pk=id)

        if title is not None:
            return Movie.objects.get(title=title)

        return None


class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(MoviesType)

    def mutate(self, info, title, year):
        movie = Movie.objects.create(title=title, year=year)

        return MovieCreateMutation(movie=movie)


class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        year = graphene.Int()
        id = graphene.ID(required=True)

    movie = graphene.Field(MoviesType)

    def mutate(self, info, id, title, year):
        movie = Movie.objects.get(pk=id)
        if title is not None:
            movie.title = title
        if year is not None:
            movie.year = year
        movie.save()

        return MovieUpdateMutation(movie=movie)


class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    movie = graphene.Field(MoviesType)

    def mutate(self, info, id):
        movie = Movie.objects.get(pk=id)
        movie.delete()

        return MovieDeleteMutation(movie=None)


class Mutation:
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    delete_movie = MovieDeleteMutation.Field()
