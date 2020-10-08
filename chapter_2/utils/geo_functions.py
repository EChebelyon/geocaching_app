import ogr
import osr 

def open_vector_file(file_path):
    """
    Open a vector compatible with OGR, gets the first layer and returns the OGR data source

    :param str file_path: The full path to the file
    :return: The OGR datasource
    """

    datasource = ogr.Open(file_path)
    layer = datasource.GetLayerByIndex(0)
    print(f"Opening {file_path} ")
    print(f"Number of features: {layer.GetFeatureCount()}")
    return datasource

def transform_geometries(datasource, src_epsg, dst_epsg):
    """
    Transform the coordinates of all geometries in the first layer
    """

    src_srs = osr.SpatialReference()
    src_srs.ImportFromEPSG(src_epsg)
    dst_srs = osr.SpatialReference()
    dst_srs.ImportFromEPSG(dst_epsg)
    transformation = osr.CoordinateTransformation(src_srs, dst_srs)
    layer = datasource.GetLayerByIndex(0)

    geoms = []
    layer.ResetReading()
    for feature in layer:
        geom = feature.GetGeometryRef().Clone()
        geom.Transform(transformation)
        geoms.append(geom)
    
    return geoms

if __name__ == '__main__':
    open_vector_file('/Users/echebelyon/Documents/GitHub/geocaching_app/data/geocaching_test.gpx')
