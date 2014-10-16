from scienceimpact.lookup.doi import doi


print doi("10.1109/GCE.2010.5676126")

print doi("10.1109/GCE.2010.5676126", kind="json")

print doi("10.1109/GCE.2010.5676126", kind="turle")




# curl -D - -L -H "Accept: application/x-bibtex" "http://dx.doi.org/10.1109/GCE.2010.5676126"

# curl -D - -L -H "Accept:text/turtlex" http://dx.doi.org/10.1109/GCE.2010.5676126"
