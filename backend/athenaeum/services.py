"""
Service layer, for scrapper (work in progress)
"""
from dataclasses import dataclass
from drf_service_layer.services import Service

@dataclass
class ScrapperDTO:
    """ Scrapper data transfer object """
    book_name: str

class ScrapperService(Service):
    """ Scrapper class """
    dto: ScrapperDTO

    def scrapper(self):
        """ Scrapper logic (to be implemented) """
        book = self.dto.book_name
        pass
        # logic
