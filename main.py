from src.cnnClassifier import logger
from src.cnnClassifier.pipelines.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline
)
from src.cnnClassifier.pipelines.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline
)
from src.cnnClassifier.pipelines.stage_03_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"
    )

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_base_model_pipeline.main()

    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"
    )

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    model_trainer = ModelTrainingPipeline()
    model_trainer.main()

    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"
    )

except Exception as e:
    logger.exception(e)
    raise e
