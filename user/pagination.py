from rest_framework import pagination


class UserAddressPagination(pagination.PageNumberPagination):
    page_size = 10
