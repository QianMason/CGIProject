# -*- mode: python -*-

block_cipher = None

adddata = [


a = Analysis(['windowsautoprimer.py'],
             pathex=['C:\\Users\\mqian\\Desktop\\CGIProject\\autoprimercode\\windowsversion'],
             binaries=[],
             datas=[],
             hiddenimports=['tkinter', 'Tkinter'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='windowsautoprimer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='windowsautoprimer')
