import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from saleor.graphql.core.connection import CountableConnection

from provinces import models


class CountableDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(cls, *args, **kwargs):
        # Force it to use the countable connection
        countable_conn = CountableConnection.create_type(
            "{}CountableConnection".format(cls.__name__), node=cls
        )
        super().__init_subclass_with_meta__(*args, connection=countable_conn, **kwargs)



class RegionNode(CountableDjangoObjectType):
    class Meta:
        model = models.Region
        filter_fields = [
            "id",
            "display_name",
            "geoname_code",
        ]
        interfaces = (graphene.relay.Node,)


class City(CountableDjangoObjectType):
    region = graphene.Field(RegionNode)

    class Meta:
        model = models.City
        filter_fields = [
            "id",
            "display_name",
            "latitude",
            "longitude",
            "subregion",
            "region",
            "country",
        ]
        interfaces = (graphene.relay.Node,)


class CityConnection(relay.Connection):
    class Meta:
        node = City


class CountryNode(CountableDjangoObjectType):
    class Meta:
        model = models.Country
        filter_fields = [
            "id",
            "continent",
            "phone",
        ]
        interfaces = (graphene.relay.Node,)


class CountryConnection(relay.Connection):
    class Meta:
        node = CountryNode
