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

    def get_inline_instances(self, request, obj=None):
        if obj is not None and obj.is_parent:
            return [ParentRelationInline(self.model, self.admin_site)]
        return []


admin.site.register(UserProfile, UserProfileAdmin)