import xml.etree.ElementTree as ET


class IEEE_Parser:
    @staticmethod
    def ieee_author_search_parser(xml_file):
        """
        Method to parse the IEEE data of author search
        """
        tree = ET.parse(xml_file)
        root = tree.getroot()

        pubList = []
        authList = []

        for child in root:
            for doc in child:
                if(doc.tag=='title'):
                    pubList.append(doc.text)
                if(doc.tag=='authors'):
                    authList.append(IEEE_Parser.name_seperator(doc.text))


    @staticmethod
    def name_seperator(names):
        """
        Method to parse author name in proper format(i.e. 'von Laszewski, G.' as 'G. von Laszewski') 
        """
        l = names.split(';  ')
        
        nameList = []
        
        for name in l:
            if ',' in name:
                last = name[:name.index(',')]
                first = name[name.index(', ')+2:]
            else:
                last = name[:name.index(' ')]
                first = name[name.index(' ')+1:]
                
            nameList.append(first+' '+last)
            
        return nameList
        
        

        
        