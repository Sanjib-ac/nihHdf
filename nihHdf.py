import os
import h5py
import numpy as np

__autor__ = 'Sanjib Sarkar'
__email__ = 'sanjib.sarkar@acquiredata.com'
__status__ = 'Prototype'
__date__ = 'FEB 2024'
__version__ = 'V1.0.0'


class nih_ads_hdf:
    def __init__(self, filename: str):
        self.file = filename
        self.f_obj = None
        self.data = None
        self.get_file_info()

    def get_file_info(self):
        self.f_obj = h5py.File(self.file, 'r')
        print(self.f_obj.keys())
        print("*" * 60, end='\n\n')
        self.close()

        # with h5py.File(self.file, 'r') as self.f_obj:
        #     # print(list(self.f_obj.items()))
        #     print(self.f_obj.keys())
        #     print("*" * 60)

    def read_file(self):
        self.f_obj = h5py.File(self.file, 'r')
        for i, file_keys in enumerate(self.f_obj.keys()):
            print(f'{i + 1}: {file_keys}')
            group = self.f_obj[file_keys]
            print(f'Shape:{group.shape}')
            print(f'data:{list(group)}\n\n')
        self.close()

    def close(self):
        self.f_obj.close()


def read_hdf(file):
    hdf_file = nih_ads_hdf(file)
    hdf_file.read_file()


if __name__ == '__main__':
    # file_name = 'Calibration__2024_02_02_155817__C4.h5'
    file_name = 'ML23320104-PAVE_D14_WT_A33_B63_TWT_5ms_.5hz__A1.h5'
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, 'files', file_name)
    read_hdf(file_path)
