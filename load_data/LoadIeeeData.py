from lookup.IEEE import IEEE

from parsers.IEEE_Parser import IEEE_Parser

class LoadIeeeData:
    @staticmethod
    def start_load():
        """
        Method to retrieve publication data from IEEE and load into neo4j
        """
        out_file = "../data/ieee_author_search.xml"
        fout = open(out_file, "w")
        print >> fout,IEEE.ieee_author_search("Gregor von Laszewski", kind="xml").encode('utf-8')
        fout.close()
        IEEE_Parser.ieee_author_search_parser(out_file)
