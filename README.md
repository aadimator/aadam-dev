# aadam-dev

My personal website and blog

## Saving Environments

To make your environment reproducible, you need to create a `environment.yml` file that enumerates all of the packages in use.

```sh
conda env export > environment.yml
```

## Restoring Environments

To reproduce the environment on another machine you just pass the `environment.yml` file as an argument to `conda env create`:

```sh
conda env create --prefix env -f environment.yml
```
