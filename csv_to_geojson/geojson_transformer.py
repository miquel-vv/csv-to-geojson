import pandas
import os
import numpy
from geojson import Point, Feature, FeatureCollection, dumps

def create_geojson(file_name):
    fold = os.path.dirname(file_name)
    name,_ = os.path.basename(file_name).split('.')
    
    output_file = os.path.join(fold, '{}.geojson'.format(name))
    
    df = pandas.read_csv(file_name).fillna('')
    lat = df['lat']
    lng = df['lng']
    df = df.drop(columns=['lat', 'lng'])
    
    feat_list = []
    failed = []
    for i in range(0, len(df.index)):
        props = remove_np_from_dict(dict(df.loc[i]))
        try:
            f = Feature(geometry=Point((float(lng[i]), float(lat[i]))),
                       properties = props)
            feat_list.append(f)
        except ValueError:
            failed.append(props)
        
    collection = FeatureCollection(feat_list)
    with open(output_file, 'w') as f:
        f.write(dumps(collection))
    
    return output_file

def remove_np_from_dict(d):
    '''numpy int64 objects are not serializable so need to convert values first.'''
    new={}
    for key, value in d.items():
        if isinstance(key, numpy.int64):
            key = int(key)
        if isinstance(value, numpy.int64):
            value = int(value)
        new[key] = value
    return new
    
def convert_numpy(val):
    if isinstance(val, numpy.int64): return int(val)