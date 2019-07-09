from lanenet_model import lanenet_cluster
import numpy as np
import glog as log

def minmax_scale(input_arr):
    min_val = np.min(input_arr)
    max_val = np.max(input_arr)
    output_arr = (input_arr - min_val) * 255.0 / (max_val - min_val)
    return output_arr

def typeof(variate):
    type=None
    if isinstance(variate,int):
        type = "int"
    elif isinstance(variate,str):
        type = "str"
    elif isinstance(variate,float):
        type = "float"
    elif isinstance(variate,list):
        type = "list"
    elif isinstance(variate,tuple):
        type = "tuple"
    elif isinstance(variate,dict):
        type = "dict"
    elif isinstance(variate,set):
        type = "set"
    else:
        type = "other"
    log.info(type)
    return type

def test_merge_model(binary_seg_image, instance_seg_image, gt_image):
    cluster = lanenet_cluster.LaneNetCluster()    
    mask = np.random.randn(binary_seg_image[0].shape[0], binary_seg_image[0].shape[1]) > 0.5
    bi = binary_seg_image[0] * mask
    mask_image, lane_coordinate, cluster_index, labels = cluster.get_lane_mask(binary_seg_ret=bi,
                                           instance_seg_ret=instance_seg_image[0], gt_image=gt_image)
    for i in range(4):
        instance_seg_image[0][:, :, i] = minmax_scale(instance_seg_image[0][:, :, i])

    embedding_image = np.array(instance_seg_image[0], np.uint8)
    predict_binary = binary_seg_image[0] * 255
    predict_lanenet = mask_image
    predict_instance = embedding_image

    lanes_pts = []
    for i in cluster_index:
        idx = np.where(labels == i)
        coord = lane_coordinate[idx]
        lanes_pts.append(coord)

    print(lanes_pts.shape)
    print(typeof(lanes_pts)
          
    return lanes_pts

def add(a,b,c):
    return 1,2,3

    

