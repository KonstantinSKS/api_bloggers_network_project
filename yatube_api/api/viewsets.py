from rest_framework import mixins
from rest_framework import viewsets


class OnlyGetPostViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass
