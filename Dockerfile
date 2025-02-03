# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primeiro
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar todo o projeto
COPY . .

# Definir o PYTHONPATH
ENV PYTHONPATH=/app

# Expor a porta
EXPOSE 7071

# Comando para rodar a aplicação
CMD ["uvicorn", "function_app:app", "--host", "0.0.0.0", "--port", "7071"]