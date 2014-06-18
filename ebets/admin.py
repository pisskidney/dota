from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from ebets.models import Player, Match, Team, Event, EbetsUser


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = EbetsUser
        fields = (
            'identifier', 'password', 'short_name', 'is_active', 'is_admin',
            'full_name', 
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = EbetsUser
        fields = ('identifier', 'short_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(DefaultUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('short_name', 'full_name', 'identifier', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('identifier', 'password')}),
        ('Personal info', {'fields': (
            'short_name', 'full_name', 'profile_url', 'avatar_full',
            'time_created', 'last_logoff'
        )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identifier', 'short_name', 'password1', 'password2')}
        ),
    )

    search_fields = ('identifier',)

    ordering = ('identifier',)

    filter_horizontal = ()

    '''
    fields = (
        'identifier', 'short_name', 'full_name', 'last_logoff', 'profile_url',
        'avatar', 'avatar_medium', 'avatar_full', 'time_created', 'is_admin',
        'is_active',
    )

    fieldsets = (
        (None, {'fields': ('identifier', 'short_name', 'password')}),
        ('Personal info', {'fields': ('full_name', 'avatar')}),
        ('Permissions', {
            'fields': ('is_admin', 'is_superuser')}),
        ('Important dates', {'fields': ('last_logoff', 'time_created')}),
    )

    list_display = ('identifier', 'short_name', 'full_name', 'last_logoff')
    readonly_fields = ('last_logoff, time_created')
    '''
    pass

admin.site.register(EbetsUser, UserAdmin)


class PlayerAdmin(admin.ModelAdmin):
    fields = ('nickname', 'team', 'first_name', 'last_name',
              'pic_pattern', 'description')
    list_display = ('nickname', 'team')


admin.site.register(Player, PlayerAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'logo_pattern')
    list_display = ('name',)


admin.site.register(Team, TeamAdmin)


class MatchAdmin(admin.ModelAdmin):
    fields = ('radiant', 'dire', 'date', 'event', 'description', 'winner',
              'over')
    list_display = ('radiant', 'dire', 'date', 'event')


admin.site.register(Match, MatchAdmin)


class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'description', 'online', 'offline')
    list_display = ('name',)


admin.site.register(Event, EventAdmin)
