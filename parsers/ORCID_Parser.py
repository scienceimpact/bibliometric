import xml.etree.ElementTree as ET

class ORCID_Parser:
    @staticmethod
    def orcid_author_get_parser(xml_file):
        """
        Method to parse the ORCID profile of an author
        """
        tree = ET.parse(xml_file)
        
        print tree.getroot().tag
        
