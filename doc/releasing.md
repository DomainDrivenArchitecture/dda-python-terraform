## Release

```
adjust version number in setup.py to release version number.
git commit -am "release"
git tag -am "release" release-[release version no]
git push --follow-tags
increase version no in setup.py
git commit -am "version bump"
git push
pip3 install --upgrade --user dda-python-terraform
```