from rest_framework import viewsets, permissions, filters, status
from players.models import Player
from players.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    # lookup_field = "id"
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [filters.SearchFilter]
    # search_fields = [
    #     "name",
    #     "email",
    #     "phone",
    #     "address",
    #     "city",
    #     "state",
    #     "country",
    #     "zip_code",
    # ]
    # pagination_class = CustomPagination
    # authentication_classes = [TokenAuthentication]
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    # def create(self, request, *args, **kwargs):
    #     serializer = PlayerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = PlayerSerializer(instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
