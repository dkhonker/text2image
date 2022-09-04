# TextToImage
基于[diffuse_my_lyrics](https://github.com/MichaelisTrofficus/diffuse_my_lyrics)，模型为[table Diffusion v1-4 Model](https://huggingface.co/CompVis/stable-diffusion-v1-4)。

由于diffuse_my_lyrics原代码中的pytorch的autocast的应用存在问题，故重写了原代码中的这一部分。

另外，Stable Diffusion对中文效果不是很好，故添加了一个翻译功能。

## 使用前准备

默认使用CUDA，故需要一台有GPU的电脑。

代码中调用了[translators](https://github.com/UlionTse/translators)包用来翻译，故需执行以下代码。

```
pip install translators
```

**注意：** 会下载大约4G的模型文件，请确保空间充足。

## 如何使用

 见`demo.ipynb`

参数

- **model_id** - 模型ID. 默认 `CompVis/stable-diffusion-v1-4`
- **revision** - 模型 revision. 默认`fp16`
- **torch_dtype** - Pytorch数据类型. 默认 `torch.float16`
- **prompt** - 这里其实是给文字另外加的文字。可以加入一些画的种类的名字，来更好的生成图像。比如, `digital art`, `HQ`, 等等。默认 `digital art`
- **num_inference_steps** - The number of steps. 默认 `50`
- **zh2en** - 是否开启翻译. 默认 `True`
- **use_auth_token** - Hugging Face的authentication token。**需要自己填写。**

另外，如果缺乏灵感，可以参考https://lexica.art/

## 效果

`戴着墨镜的马在沙漠狂奔`

<p align="center"><img src="image/0.png?raw=true" alt="Comparison"></p>

`乘电车跨过大海`

<p align="center"><img src="image/1.png?raw=true" alt="Comparison"></p>

## To Do

本来想搞[《耗时50小时，让AI生成《悔过诗》的MV》](https://www.bilibili.com/video/BV1GG4y1e7Mf)这样的视频，奈何遇到了许多问题。

期望将来能实现end-to-end 生成这样的视频。也有几个问题要面对，如对于中国风的歌词如何生成更配的场景（是否能对歌词进行进一步的精炼提取），如何使每一句生成的不相关的场景连贯起来。
