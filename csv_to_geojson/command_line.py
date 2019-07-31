import os
from geojson_transformer import create_geojson

def main():
    import sys
    if len(sys.argv) > 2:
        raise TypeError("Only the csv filename should be passed as argument. {} arguments were given.".format(len(sys.argv)-1))
    
    file_name = sys.argv[1]
    if not os.path.exists(file_name): 
        raise TypeError("{} was not found".format(file_name))
    
    if not os.path.isfile(file_name):
        raise TypeError("{} is not a file".format(file_name))
    
    print("Starting converison...")
    output = create_geojson(file_name)
    print("Geojson created at {}".format(output))

if __name__ == "__main__":
    main()