from os import getenv, path
import re

app_name = 'ScreenTranslator'

target_name = app_name
qt_version = '5.15.2'

# qtx11extras is Linux-only, remove for Windows builds
qt_modules_common = ['qtbase', 'qttools', 'icu', 'qttranslations',
                     'qtwebengine', 'qtwebchannel', 'qtdeclarative', 
                     'qtlocation', 'qtserialport']
qt_modules_windows = ['opengl32sw', 'd3dcompiler_47']
qt_modules_linux = ['qtx11extras']

os_name = getenv('OS', 'linux')
if os_name in ['win32', 'win64']:
    qt_modules = qt_modules_common + qt_modules_windows
else:
    qt_modules = qt_modules_common + qt_modules_linux

script_dir = path.dirname(path.abspath(__file__))
qt_dir = path.join(script_dir, 'qt')
ssl_dir = path.join(script_dir, 'ssl')

build_dir = path.join(script_dir, 'build')
dependencies_dir = path.join(script_dir, 'deps')
pro_file = path.abspath(path.dirname(__file__) +
                        '/../../screen-translator.pro')
test_pro_file = path.abspath(path.dirname(__file__) +
                             '/../../tests/tests.pro')
bin_name = 'screen-translator'
app_version = 'testing'
with open(pro_file, 'r') as f:
    match = re.search(r'VER=(.*)', f.read())
    if match:
        app_version = match.group(1)
ts_files_dir = path.abspath(path.dirname(__file__) + '/../../translations')

app_version += {'linux': '', 'macos': '-experimental',
                'win32': '', 'win64': ''}[os_name]
bitness = '32' if os_name == 'win32' else '64'
msvc_version = getenv('MSVC_VERSION', 'C:/Program Files (x86)/Microsoft Visual Studio/2022/BuildTools')

build_type = 'release' # 'debug'
