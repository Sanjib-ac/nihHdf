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
        self.data = None

    def get_file_info(self):
        with h5py.File(self.file, 'r') as f:
            # print(list(f.items()))
            print(f.keys())
            print("*" * 60)
            for i, file_keys in enumerate(f.keys()):
                print(f'{i + 1}: {file_keys}')
                group = f[file_keys]
                print(f'Shape:{group.shape}\n')
                print(f'data:{list(group)}')
            f.close()

    def read_file(self):
        pass

    def close(self):
        pass


def read_hdf(file):
    hdf_file = nih_ads_hdf(file)
    hdf_file.get_file_info()


if __name__ == '__main__':
    # file_name = 'Calibration__2024_02_02_155817__C4.h5'
    file_name = 'ML23320104-PAVE_D14_WT_A33_B63_TWT_5ms_.5hz__A1.h5'
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, 'files', file_name)
    read_hdf(file_path)
