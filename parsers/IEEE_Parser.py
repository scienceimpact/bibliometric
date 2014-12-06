import xml.etree.ElementTree as ET

class IEEE_Parser:
    @staticmethod
    def ieee_author_search_parser(xml_file):
        """
        Method to parse the IEEE data of author search
        """
        tree = ET.parse(xml_file)
        
        print tree.getroot().tag
        