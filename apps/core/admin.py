from django.contrib import admin

from django.contrib.admin.widgets import FilteredSelectMultiple
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget

from django.db import models


class BaseModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('', is_stacked=False)},
        models.DateField: {'widget': SuitDateWidget()},
        models.TimeField: {'widget': SuitTimeWidget()},
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget()},
    }

    def _list_field(self, qs, item_func):
        if len(qs) == 0:
            return '-'

        items = []
        for item in qs:
            result = item_func(item)
            items.append('<li> <a href="%s">%s</a></li>' % result)
        return '<ul>%s</ul>' % ''.join(items)
