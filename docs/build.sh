sphinx-multiversion "docs/source" "docs/build/html"
touch docs/build/html/.nojekyll
cp "docs/source/_template/docsite-index-redirect.html" "build/html/index.html"
ln -srf "docs/build/html/$(git tag -l --sort=creatordate |tail -1)" "docs/build/html/latest"  # auto-link the latest tag