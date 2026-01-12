build:
# 	git describe --tags --abbrev=0 | tail -n 1 | xargs -I % uv version %
# 	rm -rf dist/
# 	rm -rf build/
	sphinx-build -vvv --write-all --fresh-env src build

# create-dev:
# 	pre-commit install
# 	pre-commit autoupdate
# 	uv sync
# 	uv build

# convert-cv-to-pdf:
# 	flatpak run org.libreoffice.LibreOffice \
# 		--convert-to pdf \
# 		--outdir src/_static \
# 		src/_static/NMSynovic_CV.docx

# convert-resume-to-pdf:
# 	flatpak run org.libreoffice.LibreOffice \
# 		--convert-to pdf \
# 		--outdir src/_static \
# 		src/_static/NMSynovic_Resume.docx

serve:
	sphinx-autobuild src build
