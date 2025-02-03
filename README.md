# World Time API 🌍⏰

## 📋 Descrição do Projeto

API simples para consulta de horários internacionais, utilizando a World Time API para obter informações precisas de diferentes fusos horários.

### 🌐 Localidades Disponíveis
- 🇧🇷 Brasil (São Paulo)
- 🇺🇸 Estados Unidos (Nova York)
- 🇬🇧 Reino Unido (Londres)
- 🇨🇳 China (Shanghai)

## 🚀 Tecnologias Utilizadas

- Python 3.11
- FastAPI
- httpx
- Docker
- Azure DevOps


## 🔧 Pré-requisitos

- Python 3.11+
- Docker (opcional)
- pip

## 📦 Instalação

### Método 1: Instalação Local

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd world-time-api
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Método 2: Usando Docker

```bash
# Construir a imagem
docker build -t world-time-api .

# Executar o container
docker-compose up --build
```

## 🔍 Executando a Aplicação

### Localmente
```bash
uvicorn src.function_app:app --reload
```

### Docker
```bash
docker-compose up
```

A API estará disponível em `http://localhost:7071`

## 📡 Endpoint Disponível

### `GET /api/world-time`

#### Exemplo de Resposta:
```json
{
    "Brazil": {
        "timezone": "America/Sao_Paulo",
        "datetime": "2024-02-03T10:30:45.123456-03:00"
    },
    "USA": {
        "timezone": "America/New_York",
        "datetime": "2024-02-03T07:30:45.123456-05:00"
    },
    ...
}
```


## 🔒 Segurança

- Tratamento de erros implementado
- Validação de resposta da API externa
- Logging de erros

## 🚢 Deploy no Azure DevOps

### Pré-requisitos
- Conta no Azure DevOps
- Azure Container Registry (ACR) configurado

### Configuração
1. Crie um grupo de variáveis no Azure DevOps
2. Configure service connection para o ACR
3. Ajuste o `azure-pipelines.yml`

### Pipeline de CI/CD
A pipeline no `azure-pipelines.yml` realiza:
- Build da imagem Docker
- Push da imagem para ACR
- Tags de versão automáticas

## ✒️ Autores
* **Rafael Wessling Meurer** - *Desenvolvimento Inicial* - [rafaelwmeurer](https://github.com/rafaelwmeurer)

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes