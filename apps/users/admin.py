from __future__ import unicode_literals

from django.contrib import admin

from .models import UserProfile, ParentRelation


class ParentRelationInline(admin.TabularInline):
    model = ParentRelation
    extra = 1
    fk_name = 'parent'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_teacher', 'is_parent', 'is_student')
    readonly_fields = ('signature_tag', )
    inlines = [ParentRelationInline]

    # def get_inline_instances(self, request, obj=None):
    #     if obj is not None and obj.is_parent:
    #         return [ParentRelationInline(self.model, self.admin_site)]
    #     return []

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ParentRelationInline) and obj is None:
                continue
            elif obj.is_parent:
                yield inline.get_formset(request, obj), inline
            else:
                continue


admin.site.register(UserProfile, UserProfileAdmin)