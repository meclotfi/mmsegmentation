# Copyright (c) OpenMMLab. All rights reserved.

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class Lamp(CustomDataset):
    """Chase_db1 dataset.

    In segmentation map annotation for Chase_db1, 0 stands for background,
    which is included in 2 categories. ``reduce_zero_label`` is fixed to False.
    The ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '_1stHO.png'.
    """

    CLASSES = ('background', 'lamp','window','lampoff')

    PALETTE = [[120, 120, 120], [6, 230, 230],[6, 230, 0],[6, 0, 230]]

    def __init__(self, **kwargs):
        super(Lamp, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='.png',
            reduce_zero_label=True,
            **kwargs)
        assert self.file_client.exists(self.img_dir)