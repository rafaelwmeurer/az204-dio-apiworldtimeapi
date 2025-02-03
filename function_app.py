import httpx
import logging
from fastapi import FastAPI, HTTPException
from typing import Dict

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

async def get_world_time(timezone: str) -> Dict[str, str]:
    """
    Consulta a API World Time para obter informações de horário de um timezone específico.
    
    Args:
        timezone (str): Timezone a ser consultado
    
    Returns:
        Dict[str, str]: Dicionário com informações de local e horário
    """
    try:
        # Timeout configurado para 10 segundos
        async with httpx.AsyncClient(timeout=10.0) as client:
            url = f"https://worldtimeapi.org/api/timezone/{timezone}"
            logger.info(f"Fazendo requisição para: {url}")
            
            # Adicionar headers para identificação
            headers = {
                "User-Agent": "WorldTimeAPIClient/1.0",
                "Accept": "application/json"
            }
            
            response = await client.get(url, headers=headers)
            
            # Log do status da resposta
            logger.info(f"Status da resposta: {response.status_code}")
            
            # Verificar explicitamente o status da resposta
            if response.status_code != 200:
                logger.error(f"Erro na requisição: {response.text}")
                raise HTTPException(
                    status_code=response.status_code, 
                    detail=f"Erro ao consultar API de horário. Status: {response.status_code}"
                )
            
            # Parse do JSON
            data = response.json()
            
            return {
                "timezone": timezone,
                "datetime": data.get('datetime', 'N/A')
            }
    except httpx.RequestError as exc:
        # Log de erro de conexão
        logger.error(f"Erro de conexão ao consultar {timezone}: {exc}")
        raise HTTPException(
            status_code=500, 
            detail=f"Erro de conexão ao consultar horário para {timezone}. Detalhes: {str(exc)}"
        )
    except Exception as exc:
        # Log de qualquer outro erro
        logger.error(f"Erro inesperado ao consultar {timezone}: {exc}")
        raise HTTPException(
            status_code=500, 
            detail=f"Erro inesperado ao consultar horário para {timezone}. Detalhes: {str(exc)}"
        )

@app.get("/api/world-time")
async def get_world_times():
    """
    Endpoint para obter horários de diferentes localidades.
    
    Returns:
        Dict[str, Dict[str, str]]: Horários de Brazil, EUA, Inglaterra e China
    """
    timezones = {
        "Brazil": "America/Sao_Paulo",
        "USA": "America/New_York", 
        "UK": "Europe/London",
        "China": "Asia/Shanghai"
    }
    
    world_times = {}
    for country, timezone in timezones.items():
        try:
            world_times[country] = await get_world_time(timezone)
        except HTTPException as exc:
            # Em caso de falha para um timezone, registra o erro mas continua
            logger.warning(f"Falha ao obter horário para {country}: {exc.detail}")
            world_times[country] = {
                "timezone": timezone,
                "error": exc.detail
            }
    
    return world_times

# Adicionar tratamento de exceções não capturadas
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Erro não tratado: {exc}")
    return {"detail": "Erro interno no servidor"}