from rest_framework import viewsets, mixins
from apps.simmaster.custom_mixin import NewCreateModelMixin, NewListModelMixin, NewRetrieveModelMixin, NewUpdateModelMixin


class NewModelViewSet(NewCreateModelMixin,
                   NewRetrieveModelMixin,
                   NewUpdateModelMixin,
                   mixins.DestroyModelMixin,
                   NewListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass