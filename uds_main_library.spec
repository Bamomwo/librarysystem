# -*- mode: python -*-

block_cipher = None


a = Analysis(['uds_main_library.py'],
             pathex=['C:\\Users\\Bamomwo\\AppData\\Local\\Programs\\Python\\Python36-32\\projects\\library'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='uds_main_library',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='Oxygen-Icons.org-Oxygen-Actions-document-edit.ico')
