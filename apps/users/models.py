from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class PersonalDataMixin(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    first_name = models.CharField(_('First Name'), max_length=100, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=100, blank=True)
    phone = models.CharField(_('Phone Number'), max_length=100, blank=True)
    email = models.EmailField(_('Email'), max_length=100, blank=True)
    date_of_birth = models.DateField(_('Date of birth'), blank=True, null=True)
    genders = models.CharField(_('Gender'), max_length=10, choices=GENDER_CHOICES, default=MALE)
    pesel = models.CharField(_('PESEL'), max_length=11, blank=True, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class UserProfile(PersonalDataMixin, models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), related_name='profile')
    is_active = models.BooleanField(_('Active'), default=True)

    is_parent = models.BooleanField(_('Is parent'), default=False)
    is_student = models.BooleanField(_('Is student'), default=False)
    is_teacher = models.BooleanField(_('Is teacher'), default=False)

    signature_upload = models.ImageField(upload_to='signatures', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def signature_tag(self):
        return u'<img src="%s" style="max-width:300px"/>' % self.signature_upload.url
    signature_tag.short_description = 'Signature'
    signature_tag.allow_tags = True

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


@python_2_unicode_compatible
class ParentRelation(models.Model):
    parent = models.ForeignKey(UserProfile, verbose_name=_('Parent'), limit_choices_to={'is_parent': True},
                               related_name='children_rel')
    child = models.ForeignKey(UserProfile, verbose_name=_('Child'), limit_choices_to={'is_student': True},
                              related_name='parent_rel')

    def __str__(self):
        return '%s (%s)' % (self.child, self.parent)

    class Meta:
        verbose_name = _('Parent Relation')
        verbose_name_plural = _('Parent Relations')


# @receiver(post_save, sender=User)
# def update_user_profile(sender, **kwargs):
#     user = kwargs['instance']
#     profile, created = UserProfile.objects.get_or_create(user=user)
#     UserProfile.objects.filter(id=profile.id).update(first_name=user.first_name,
#                                                      last_name=user.last_name,
#                                                      email=user.email)


@receiver(post_save, sender=UserProfile)
def update_user(sender, **kwargs):
    profile = kwargs['instance']
    user = profile.user
    user.first_name = profile.first_name
    user.last_name = profile.last_name
    user.email = profile.email
    User.objects.filter(id=user.id).update(first_name=profile.first_name,
                                           last_name=profile.last_name,
                                           email=profile.email)
