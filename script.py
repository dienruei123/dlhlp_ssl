# import s3prl.hub as hub
# import torch

# model_0 = getattr(hub, 'fbank')()  # use classic FBANK
# model_1 = getattr(hub, 'modified_cpc')()  # build the CPC model with pre-trained weights
# model_2 = getattr(hub, 'tera')()  # build the TERA model with pre-trained weights
# model_3 = getattr(hub, 'wav2vec2')()  # build the Wav2Vec 2.0 model with pre-trained weights

# device = 'cuda'  # or cpu
# model_3 = model_3.to(device)
# wavs = [torch.randn(160000, dtype=torch.float).to(device) for _ in range(16)]
# with torch.no_grad():
#     reps = model_3(wavs)["hidden_states"]

import os
# os.chdir("/work/u8449362")

datasets = [
    "https://www.openslr.org/resources/12/dev-clean.tar.gz",
    "https://www.openslr.org/resources/12/dev-other.tar.gz",
    "https://www.openslr.org/resources/12/test-clean.tar.gz",
    "https://www.openslr.org/resources/12/test-other.tar.gz",
    "https://www.openslr.org/resources/12/train-clean-100.tar.gz",
    "https://www.openslr.org/resources/12/train-clean-360.tar.gz",
    "https://www.openslr.org/resources/12/train-other-500.tar.gz",
]

if __name__ == "__main__":
    os.chdir("/work/u8449362")
    # os.system("pip install -r requirements/all.txt")
    # os.system("pip install -r requirements/dev.txt")
    # os.system("pip install -r requirements/install.txt")
    # os.system("pip install s3prl")
    
    # for dataset in datasets:
    #     os.system(f"wget {dataset} -O {dataset.split('/')[-1]}")
    #     os.system(f"tar -xvf ./{dataset.split('/')[-1]} -C ./LibriSpeech")
    #     os.system(f"rm -rf ./{dataset.split('/')[-1]}")
    # os.chdir("./s3prl/s3prl")
    # os.system("python3 preprocess/generate_len_for_bucket.py -i ../../LibriSpeech/")

    # os.chdir("/work/u8449362/s3prl")

    os.chdir("./s3prl/s3prl") 
    os.system("python3 run_downstream.py -m train -n asr_test -u fbank -d asr")