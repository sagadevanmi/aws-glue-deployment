import sys
import logging
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from utils.data_processor import DataProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize Glue context
        sc = SparkContext()
        glueContext = GlueContext(sc)
        spark = glueContext.spark_session
        
        logger.info("Initialized Glue context successfully")
        
        # Initialize data processor
        processor = DataProcessor(spark)
        
        # Process data
        processor.process_data()
        
        logger.info("Data processing completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main() 