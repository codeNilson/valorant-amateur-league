import uuid
from django.test import TestCase
from gamedata.models import Agent, Role, Map, Tier


class TestStatModel(TestCase):

    def test_agent_str_method(self):
        agent = Agent.objects.create(name="Sova")
        self.assertEqual(str(agent), agent.name)

    def test_role_str_method(self):
        role = Role.objects.create(uuid=uuid.uuid4(), name="Duelist")
        self.assertEqual(str(role), role.name)

    def test_map_str_method(self):
        game_map = Map.objects.create(uuid=uuid.uuid4(), name="Bind")
        self.assertEqual(str(game_map), game_map.name)

    def test_tier_str_method(self):
        tier = Tier.objects.create(tier="Iron", division="1")
        self.assertEqual(str(tier), tier.tier)
