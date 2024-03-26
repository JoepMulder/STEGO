from utils import *
import hydra
from omegaconf import DictConfig
import os
import wget


@hydra.main(config_path="configs", config_name="eval_config.yml")
def my_app(cfg: DictConfig) -> None:
    pytorch_data_dir = cfg.pytorch_data_dir
    dataset_names = ["cocostuff"]#["potsdam", "cityscapes", "cocostuff", "potsdamraw"]
    url_base = "https://upnow-prod.ff45e40d1a1c8f7e7de4e976d0c9e555.r2.cloudflarestorage.com/zkezvcRggVQB5lzXFKyOYgAP6N22/ab390096-dd36-4bc0-bb0a-7f2f3ff720c1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=cdd12e35bbd220303957dc5603a4cc8e%2F20240326%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20240326T125131Z&X-Amz-Expires=43200&X-Amz-Signature=5198d13086ec7898ecfbd430807e2e73934ef19b1e74ed471eb0def33996b601&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3D%22cocostuff.zip%22"

    os.makedirs(pytorch_data_dir, exist_ok=True)
    for dataset_name in dataset_names:
        if (not os.path.exists(join(pytorch_data_dir, dataset_name))) or \
                (not os.path.exists(join(pytorch_data_dir, dataset_name + ".zip"))):
            print(f"\n Downloading {dataset_name} from {url_base}")
            wget.download(url_base, join(pytorch_data_dir, dataset_name + ".zip"))
        else:
            print("\n Found {}, skipping download".format(dataset_name))


if __name__ == "__main__":
    prep_args()
    my_app()
