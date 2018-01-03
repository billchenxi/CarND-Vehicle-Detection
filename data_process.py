import glob
import pickle

def data_process(train_r=0.7, valid_r=0.2, test_r=0.1):
    '''
    data_process(): function to use vehicle and non-vehicle images from a combination of the GTI vehicle image database, the KITTI vision benchmark suite, and examples extracted from the project video itself. 
        Input:
            * train_r: training ratio
            * valid_r: validation ratio
            * test_r: test ratio
    '''
    cars0 = glob.glob('./vehicles/GTI_Far/*.png')
    cars1 = glob.glob('./vehicles/GTI_MiddleClose/*.png')
    cars2 = glob.glob('./vehicles/GTI_Left/*.png')
    cars3 = glob.glob('./vehicles/GTI_Right/*.png')
    cars4 = glob.glob('./vehicles/KITTI_extracted/*.png')
    
    notcars1 = glob.glob('./non-vehicles/Extras/*.png')
    notcars1 += glob.glob('./non-vehicles/GTI/*.png'

    
    
    pickle_file = 'data.p'
    print('Saving data to pickle file...')