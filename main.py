from ChestCancerClassification import logger
from ChestCancerClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChestCancerClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ChestCancerClassification.pipeline.stage_03_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try: 
    logger.info(f"*******************")
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
