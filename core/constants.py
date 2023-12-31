CHECKPOINT_PATH = "sam_vit_l_0b3195.pth"
MODEL_TYPE = "vit_l"
# THESE ARE SUBJECT TO CHANGE AT ANY TIME, YOU PESKY MINERS YOU
POSSIBLE_VALUES_TO_TEST_EACH_HOTKEY = range(1, 4)
WEIGHTS_FOR_NUMBER_OF_TIMES_TO_TEST_EACH_HOTKEY = [50, 10, 10]  # , 10, 10, 5, 4, 3, 2, 1]

# DEFAULT SIZE IS 5GB
MINER_CACHE_SIZE = 5 * (1024**3)


LARGEST_SEED = 4294967295
DEFAULT_CFG_SCALE = 7
DEFAULT_HEIGHT = 1024
DEFAULT_WIDTH = 1024
DEFAULT_SAMPLES = 1
DEFAULT_STEPS = 30
DEFAULT_STYLE_PRESET = None
DEFAULT_IMAGE_STRENGTH = 0.20
DEFAULT_INIT_IMAGE_MODE = "IMAGE_STRENGTH"