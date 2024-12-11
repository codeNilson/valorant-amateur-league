
# Liga Amadora de Valorant - Site de campeonato de Valorant

Este repositório contém o código-fonte do **lavava.com.br**, um site que organiza um torneio online do jogo Valorant, desenvolvido com Django.
O site é integrado a um bot do Discord para facilitar a administração e interação entre os jogadores, utilizando APIs para comunicação entre os dois sistemas.

Funcionalidades Principais
---------------------------

- Cadastro e autenticação de usuários (com suporte a OAuth2 e autenticação por redes sociais).
- Gerenciamento de torneio para Valorant que envolve escolha dinâmica de equipes:
  - Dois líderes são sorteados antes de cada partida para formar os times.
  - Pontuação e classificações baseadas no desempenho individual dos jogadores.
- Sistema de classificação com cálculo de posições, histórico de partidas e estatísticas globais.
- Integração com um bot do Discord para automação:
  - Sorteio de líderes.
  - Gerenciamento de jogadores e equipes.
  - Registro e sincronização de resultados das partidas.
- Design responsivo, otimizado para desktop e dispositivos móveis.
- Idioma em inglês e pt-BR.
- Configuração em produção com suporte a HTTPS (usando Nginx e Gunicorn).

Tecnologias Utilizadas
----------------------

- **Backend:** Django com Django Rest Framework (DRF) para APIs RESTful. Suporte a localização em inglês e pt_br.
- **Frontend:** HTML5, Javascript, SCSS (gerado com SASS) e Bootstrap.
- **Servidor:** Nginx como proxy reverso, Gunicorn como servidor WSGI.
- **Banco de Dados:** PostgreSQL em produção.
- **Infraestrutura:** Configuração de HTTPS com certificados SSL através do Let's Encrypt.

## Screenshots

![App Screenshot](https://i.imgur.com/aRIf2Ny.png)

## Rodando localmente

1. Clone o projeto

```bash
  git clone https://github.com/AroMight/valorant-amateur-league.git
```

2. Crie e ative um ambiente virtual:

```bash
  python -m venv venv source venv/bin/activate # No Windows, use venv\Scripts\activate
```

3. Instale as dependências

```bash
  pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

```bash
  - Crie um arquivo `.env` na raiz do projeto e preencha com as configurações necessárias (veja `.env.example`).
```

5. Aplique as migrações

```bash
  python manage.py migrate
```

6. Aplique as fixtures para o app gamedata

```bash
  python manage.py loaddata gamedata/fixtures/gamedata_fixtures.json
```

7. Inicie o servidor

```bash
  python manage.py runserver
```
