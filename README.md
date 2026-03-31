# QuPath Zindy catalog

This is a custom QuPath catalog maintained by [@zindy](https://github.com/zindy) containing (somewhat) useful extensions developed over the years.

## Extensions in this catalog

This catalog includes the following extensions:

### QuPath XGBoost extension
XGBoost object classifier for QuPath.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-xgboost
- **QuPath compatibility**: v0.7.0+
- **Discussion**: https://forum.image.sc/t/xgboost-extension-for-object-classification-qupath-0-7/119571

### QuPath NDPA extension
Extension to import and export Hamamatsu annotations between NDP.View and QuPath.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-ndpa
- **QuPath compatibility**: v0.7.0+
- **Discussion**: https://forum.image.sc/t/qupath-extension-ndpa-import-export-ndpa-annotations-from-qupath-now-as-an-extension/111858

### QuPath MLD extension
An extension to import Visiopharm MLD annotations into QuPath.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-mld
- **QuPath compatibility**: v0.7.0+
- **Discussion**: https://forum.image.sc/t/qupath-extension-for-importing-visiopharm-mld-files-into-qupath-both-rois-labels/118475

### QuPath Project Metadata editor extension
A QuPath extension for viewing and editing project metadata, extracted from QuPath core to allow independent development and release.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-project-metadata-editor
- **QuPath compatibility**: v0.7.0+

### QuPath Filename Regex extension
Filename regex parser inspired by CellProfiler.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-fireparser
- **QuPath compatibility**: v0.7.0+
- **Discussion**: https://forum.image.sc/t/qupath-metadata/80733/6

### QuPath OCR extension
QuPath extension for optical character recognition (OCR) on slide labels via Tess4J / Tesseract.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-ocr
- **QuPath compatibility**: v0.7.0+
- **Discussion**: https://forum.image.sc/t/how-to-read-tissue-slides-label-using-tesseract/114820/4
  
### QuPath BentoFX extension (experimental)
This extension converts QuPath's dialogs and frames into dockable panels. It is very much a proof of concept: Not everything works as expected, so use it at your own risk but I would love to hear back from you if you encounter any issues!

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-bentofx
- **QuPath compatibility**: v0.7.0+
- **Discussion**: https://forum.image.sc/t/qupath-gui-with-dockable-panels-experimental-proof-of-concept/115582

### QuPath JInput extension (experimental)
This extension adds joysticks and spacemouse navigation to QuPath via JInput. It was originally written by @petebankhead.

- **Latest version**: v0.1.0
- **Repository**: https://github.com/zindy/qupath-extension-jinput
- **QuPath compatibility**: v0.7.0+

## Installation

To use this catalog in QuPath:

1. Open QuPath
2. Go to **Extensions → Manage extensions**
3. Click **Manage extension catalogs**
4. Enter the catalog URL: `https://github.com/zindy/qupath-catalog-zindy`
5. Browse and install the extensions you need or want to try.

## About QuPath catalogs

QuPath uses [catalogs](https://github.com/qupath/extension-catalog-model) to easily install, manage, and delete QuPath extensions. 

To create your own custom catalog, follow the instructions at https://github.com/qupath/extension-catalog-model.
