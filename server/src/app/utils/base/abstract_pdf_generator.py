from abc import ABC, abstractmethod


class AbstractPDFGenerator(ABC):

    @staticmethod
    @abstractmethod
    def cot_report_calculation(pdf_filename: str) -> None:
        """
        Generates and returns a PDF file showing how the values in the cot report were
        calculated.
        :param report: A report issued by the CFTC, showing the positions of market participants (Noncommercial).
        :param pdf_filename: Name of the PDF file that will be generated.
        :return: None
        """