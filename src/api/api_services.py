from PIL import Image
from io import BytesIO
import io
import logging
logger = logging.getLogger('root')

class api_services:

    def welcome(self):
        logger.info("Welcome to outliers app")
        return "Welcome to  outlier detection!"    
    
    def return_image(self, data):
        try:
            logger.info("Data analyzed")
            return()
        except Exception as err:
            logger.exception(err)
            return("Problem analyzing data")




            

