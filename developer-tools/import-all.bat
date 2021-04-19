echo off

cd ../game/libs

git clone https://github.com/python/typeshed.git
pip download PyQt5
pip download QtGui
pip download PyQtWebEngine
cd ../../