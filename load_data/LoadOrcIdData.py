from lookup.ORCID import ORCID

from parsers.ORCID_Parser import ORCID_Parser

class LoadOrcIdData:
    @staticmethod
    def start_load():
        """
        Method to retrieve author data from ORCID and load into neo4j
        """
        out_file = "../data/orcid_author_get.xml"
        fout = open(out_file, "w")
        print >> fout, ORCID.orcid_author_get("0000-0001-9558-179X", kind="xml").encode('utf-8')
        fout.close()
        ORCID_Parser.orcid_author_get_parser(out_file)
