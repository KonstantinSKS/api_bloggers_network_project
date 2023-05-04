from rest_framework import mixins
from rest_framework import viewsets


class Only_Get_Post_ViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass
