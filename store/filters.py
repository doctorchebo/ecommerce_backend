from typing import Any

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PointsValueListFilter(admin.SimpleListFilter):
    title = _("Points Value Range")
    parameter_name = "Range"

    def lookups(self, request, model_admin):
        return [
            ("<10", _("Less than 10 PV")),
            (">=10", _("10 PV or more"))
        ]
    def queryset(self, request, queryset):
        if self.value() == "<10":
            return queryset.filter(points_value__lt = 10)
        if self.value() == ">=10":
            return queryset.filter(points_value__gte = 10)