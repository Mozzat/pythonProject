# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py','home.py','SQLManager.py','util.py'],
    pathex=[],
    binaries=[],
    datas=[('image/打工人.gif', 'image'),('image/bg.png', 'image'), (robot.ico, '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='桃桃子',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='robot.ico',
)
