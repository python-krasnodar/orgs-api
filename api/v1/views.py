from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.v1.serializers import OrganizationSerializer, OrganizationArticleSerializer
from domain.orgs.models import Organization, Article
from domain.refs.models import District


class OrganizationByDistrictViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        district = get_object_or_404(District, pk=self.kwargs['district'])
        return self.queryset.filter(districts__in=[district])


class ArticleByOrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects
    serializer_class = OrganizationArticleSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        district = get_object_or_404(District, pk=self.kwargs['district'])
        organization = get_object_or_404(Organization, pk=self.kwargs['organization'], districts__in=[district])
        return self.queryset.filter(organization=organization)
