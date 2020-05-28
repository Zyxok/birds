import os

SPECIES = ['Agelaius phoeniceus', 'Anas platyrhynchos', 'Ardea alba', 'Ardea herodias', 'Branta canadensis',
           'Buteo jamaicensis', 'Calidris alpina', 'Haliaeetus leucocephalus', 'Larus argentatus', 'Pandion haliaetus',
           'Passer domesticus', 'Sturnus vulgaris', 'Turdus migratorius']


class Path:
    RESOURCES = "resources"
    DATA_CONDENSED = os.path.join(RESOURCES,"data_condensed.csv")
    FRAMES = os.path.join(RESOURCES,"frames")


SHUFFLE_SEED = 69

IMAGE_SIZE = (360, 585)

