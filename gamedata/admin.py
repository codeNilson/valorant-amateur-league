from django.contrib import admin
from .models import Agent, Role, Map, Tier


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    pass


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    pass
