from scienceimpact.lookup.doi import doi2bibtex


print doi2bibtex("10.1109/GCE.2010.5676126")

print doi2bibtex("10.1109/GCE.2010.5676126", kind="json")

print doi2bibtex("10.1109/GCE.2010.5676126", kind="turle")




# curl -D - -L -H "Accept: application/x-bibtex" "http://dx.doi.org/10.1109/GCE.2010.5676126"

# curl -D - -L -H "Accept:text/turtlex" http://dx.doi.org/10.1109/GCE.2010.5676126"
