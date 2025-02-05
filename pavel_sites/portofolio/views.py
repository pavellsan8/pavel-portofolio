from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def homepage(request):
    logger.error("Homepage view was called") 
    try:
        return render(request, 'homepage.html')
    except Exception as e:
        logger.error(f"Error rendering homepage: {str(e)}")
    
def porto_details(request):
    return render(request, 'portfolio-details.html')