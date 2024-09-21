from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Role
from pprint import pprint
from django.db.utils import (
    IntegrityError,
)  # Assuming UniqueConstraintFailed is an IntegrityError


def AgentList(request):
    valorant_data = requests.get(
        "https://valorant-api.com/v1/agents?isPlayableCharacter=True"
    )
    json_data = valorant_data.json()
    data = json_data["data"]
    for agent in data:
        role = agent["role"]
        try:
            role = Role.objects.create(
                uuid=role["uuid"],
                name=role["displayName"],
                description=role["description"],
                icon=role["displayIcon"],
            )
        except IntegrityError:
            pass

    return HttpResponse("Hello, world. You're at the polls index.")
