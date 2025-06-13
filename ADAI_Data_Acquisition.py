import logging
import azure.functions as func
import requests
import pandas as pd
import io
import os

from azure.storage.blob import BlobServiceClient
from datetime import datetime

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 2 * * TUE",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def ADAI_Data_Acquisition(myTimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function started.')

    # Configuração do logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Variaveis que se alteram por conjunto de dados
    url = "https://inradar.com.br/api/v1/member_history"
    params = {"limit": 50, "offset": 0}
    name_file = "member_history"
    data_formatada = datetime.today().strftime('%Y%m%d')

    ACCOUNT_NAME = os.environ.get(ACCOUNT_NAME)
    ACCOUNT_KEY = os.environ.get(ACCOUNT_KEY) 
    CONTAINER_NAME = "raw"
    BLOB_NAME = f"{name_file}/{name_file}_{data_formatada}.csv"

    # Construir a connection string
    connection_string = (
        f"DefaultEndpointsProtocol=https;"
        f"AccountName={ACCOUNT_NAME};"
        f"AccountKey={ACCOUNT_KEY};"
        f"EndpointSuffix=core.windows.net"
    )

    # Cabeçalhos de autenticação
    headers = {
        "Authorization": "ApiKey yurifillippo:9d20cd67a03a19a2bbcf7cac0ea11b2409e11bc7",
        "Content-Type": "application/json;charset=UTF-8",
        "Channel": "control_panel",
        "Origin": "https://admin.inchurch.com.br",
        "Referer": "https://admin.inchurch.com.br/",
        "Accept": "application/json, text/plain, /"
    }

    todos_size = []

    while True:
        logger.info(f"Linhas de dados coletadas: {params['offset']}")
        response = requests.get(url, headers=headers, params=params)

        try:
            data = response.json()
        except Exception as e:
            logger.error("Erro ao converter JSON:", e)
            logger.error("Resposta crua:", response.text)
            break

        data = data.get("objects", [])  # Ponto-chave da resposta

        if not data:
            logger.info("Nenhum dado retornado. Fim da coleta.")
            break

        todos_size.extend(data)
        params["offset"] += params["limit"]

    # Se dados foram coletados
    if todos_size:
        # Converte todos os dados em DataFrame
        df = pd.json_normalize(todos_size)

        print(f"Quantidade de dados: {df.shape[0]}")

        logger.info("Colunas disponíveis:")
        print(df.columns.tolist())

        # Salvar tudo
        buffer = io.BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)

        # Conectar ao Azure Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string)
        blob_client = blob_service_client.get_blob_client(
            container=CONTAINER_NAME, blob=BLOB_NAME)

        # Enviar o arquivo para o blob
        blob_client.upload_blob(buffer, overwrite=True)

        logger.info(f"Arquivo completo salvo como '{name_file}.csv'")
    else:
        logger.info("Nenhum dado coletado da API.")

    logging.info('Python timer trigger function executed.')

