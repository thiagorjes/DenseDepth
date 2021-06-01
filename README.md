
## [Estimativa de Profundidade de Alta Qualidade utilizando Camera Monocular via "Transfer Learning"](https://arxiv.org/abs/1812.11941)

A versão mais recente, porém instável [AdaBins](https://github.com/shariqfarooq123/AdaBins).

## Modelos Pré-Treinados
* [NYU Depth V2](https://s3-eu-west-1.amazonaws.com/densedepth/nyu.h5) (165 MB)
* [KITTI](https://s3-eu-west-1.amazonaws.com/densedepth/kitti.h5) (165 MB)

## Datasets
* [NYU Depth V2 (50K)](https://tinyurl.com/nyu-data-zip) (4.1 GB): Não precisa extrair esse arquivo.
* [KITTI](http://www.cvlibs.net/datasets/kitti/): Copiar o "raw data" para a pasta '../kitti'. Esse metodo espera por "dense input depth maps", então precisa calcular um "depth [inpainting method](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)" nos dados do Lidar. 
Para os experimentos, foi utilizado o script [Python](https://gist.github.com/ialhashim/be6235489a9c43c6d240e8331836586a) que reimplemento o código disponibilizado com o "NYU Depth V2 toolbox".

## Preparando o Ambiente
* Para utilizar é necessário ter o CUDA_10.0 (e Cudnn compatível) , Python 3.5 (ou superior), pip e virtualenv (para evitar problemas)
* Execute o comando e todas as dependências serão instaladas (processo já testado):
```
./instalar_dependencias.sh 1
```
O parametro 1 é para instalar CUDA e CUNN corretamente, se você já possuir o CUDA 10.0 e Cudnn compatível instalados então rode o seguinte comando:
```
./instalar_dependencias.sh
```





## Treinar (Precisa de uma Titan V)
```
   source venv/bin/activate
   python3 train.py --data nyu --gpus 1 --bs 4
   deactivate
```


## Avaliar
* Baixe, mas não extraia o arquivo do [link](https://s3-eu-west-1.amazonaws.com/densedepth/nyu_test.zip) (1.4 GB). Então execute:
```
   source venv/bin/activate
   python evaluate.py
   deactivate
```

## Visualizar imagens lado a lado - original/profundidade
* Rode o seguinte comando para utilizar um vídeo e gerar imagens lado a lado comparando o frame original e a profundidade estimada:
```
python test_video.py --model nyu.h5 --input test_video.MOV
```
Obs.: test_video.MOV é algum vídeo de sua escolha.

## Referência aos autores
Corresponding paper to cite:
```
@article{Alhashim2018,
  author    = {Ibraheem Alhashim and Peter Wonka},
  title     = {High Quality Monocular Depth Estimation via Transfer Learning},
  journal   = {arXiv e-prints},
  volume    = {abs/1812.11941},
  year      = {2018},
  url       = {https://arxiv.org/abs/1812.11941},
  eid       = {arXiv:1812.11941},
  eprint    = {1812.11941}
}
```
