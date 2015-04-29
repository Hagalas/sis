from django.core.urlresolvers import reverse


def admin_url(app, model, view, args=None):
    return reverse('admin:%s_%s_%s' % (app, model, view), args=args)


def register_list_field(admin, name, title, func, qs_func):
    def field(self, obj):
        return self._list_field(qs_func(obj), func)
    field.short_description = title
    field.allow_tags = True
    setattr(admin, name, field)