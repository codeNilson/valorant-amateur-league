from django.test import SimpleTestCase
from utils.discord_utils import get_random_color


class GetRandomColorTests(SimpleTestCase):

    def test_get_random_color(self):
        cores_decimais = [
            65535,  # Ciano (0x00FFFF)
            255,  # Azul (0x0000FF)
            16711935,  # Rosa choque (0xFF00FF)
            16776960,  # Amarelo (0xFFFF00)
            65280,  # Verde (0x00FF00)
            16711680,  # Vermelho (0xFF0000)
        ]

        # Testa se a cor retornada está na lista de cores possíveis
        cor_decimal = get_random_color()
        self.assertIn(cor_decimal, cores_decimais)

    def test_get_random_color_hex_format(self):
        # Testa se a cor retornada pode ser formatada como hexadecimal
        cor_decimal = get_random_color()
        cor_hex = f"#{cor_decimal:06X}"
        self.assertTrue(cor_hex.startswith("#"))
        self.assertEqual(len(cor_hex), 7)
