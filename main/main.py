from load_data.LoadOrcIdData import LoadOrcIdData 
from load_data.LoadIeeeData import LoadIeeeData
def start():
    LoadOrcIdData.start_load()
    LoadIeeeData.start_load()

if __name__ == '__main__': start()