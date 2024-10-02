from rest_framework.pagination import PageNumberPagination


class HabitsPaginator(PageNumberPagination):
    max_page_size = 5
    page_size = 5
    page_query_param = "page_size"
