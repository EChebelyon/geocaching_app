import ogr

def open_vector_file(file_path):
    """
    Open a vector compatible with OGR, gets the first layer and returns the OGR data source

    :param str file_path: The full path to the file
    :return: The OGR datasource
    """

    datasource = ogr.Open(file_path)
    layer = datasource.GetLayerByIndex(0)
    print(f"Opening {file_path} ")
    print(f"Number of features: {layer.GetFeaureCount()}")
    return datasource

if __name__ == '__main__':
    open_vector_file('/Users/echebelyon/Documents/GitHub/geocaching_app/data/geocaching_test.gpx')
