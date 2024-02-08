# mercury

## 项目结构

```plantuml
mercury
    ├─common  # 通用模块
    │
    ├─core    # 核心模块
    │
    ├─domain  # DTO
    │
    ├─entity  # PO
    │
    ├─mapper  # 数据访问模块
    │
    ├─model   # VO
    │
    ├─service # 业务模块
    │
    ├─web     # web 模块
    │
    └─app.py  # 项目入口
```

## 项目环境

### python

- [python3.12](https://docs.python.org/3.12/)

```shell
conda create -y -n mercury python=3.12
```

### 必要依赖

- [Flask](https://flask.palletsprojects.com/)

```shell
conda activate mercury
pip install Flask
```

### 开发依赖

- [pytest](https://docs.pytest.org/)
- [pylint](https://pylint.readthedocs.io/)

```shell
conda activate mercury
pip install pytest pylint
```
