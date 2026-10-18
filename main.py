from src.cnnClassifier import logger
from src.cnnClassifier.pipelines.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.components import prepare_base_model
from pathlib import Path
STAGE_NAME ="data ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    obj = DataIngestionTrainingPipeline()
    obj.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "prepare base model"
try:
    logger.info(f"****************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
