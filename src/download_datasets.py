import os
import requests
from os.path import join
import hydra
from omegaconf import DictConfig
from utils import prep_args

@hydra.main(config_path="configs", config_name="eval_config.yml")
def my_app(cfg: DictConfig) -> None:
    pytorch_data_dir = cfg.pytorch_data_dir
    dataset_names = [
        "potsdam",
        "cityscapes",
        "cocostuff",
        "potsdamraw",
        "voc"
    ]
    url_base = "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/"

    os.makedirs(pytorch_data_dir, exist_ok=True)
    for dataset_name in dataset_names:
        dataset_file_path = join(pytorch_data_dir, dataset_name + ".tar")
        if not os.path.exists(dataset_file_path):
            print("\n Downloading {}".format(dataset_name))
            url = url_base + dataset_name + ".tar"
            response = requests.get(url, stream=True)
            with open(dataset_file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        else:
            print("\n Found {}, skipping download".format(dataset_name))

if __name__ == "__main__":
    prep_args()
    my_app()

