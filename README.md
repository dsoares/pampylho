# Pampylho: yet another Python wrapper for PAM

My own Python wrapper for PAM, based on these projects:

- [gnosek/python-pam](https://github.com/gnosek/python-pam)
- [simplepam](https://github.com/leonnnn/python3-simplepam)
- [minrk/pamela](https://github.com/minrk/pamela)

This is just a fork from project
[minrk/pamela](https://github.com/minrk/pamela), with a minor modification.

## Why?

I need this minor modification for my
[JupyterHub](https://github.com/jupyter/jupyterhub) environment, which
uses the [pam-mount](http://pam-mount.sourceforge.net/) PAM module.

After some more testing, I'll open a pull request to the
main [minrk/pamela](https://github.com/minrk/pamela) project.


## Use it

Install:

    pip install git+https://github.com/dsoares/pampylho.git


## The name

**Pampilho** is a pastry from Santarém, Portugal. It's a thinly rolled
sponge cake filled with egg yolk cream called *“Ovos-moles (soft
eggs)”* (see
[pampilho](https://eatingtheworld.wordpress.com/2012/12/07/portuguese-pastry-post-doc-pampilhos-de-santarem/)).
