from cx_Freeze import setup, Executable

includefiles = ['ffmpeg.exe', 'api/download_logic/사용방법.txt', 'api/download_logic/user_query.txt']

buildOptions = dict(packages = ['os'], excludes = [], include_files = includefiles)

exe = [Executable("api/download_logic/HIGHLIGHTING.py")]

setup(
    author = "Team HIGHLIGHTING",
    options = dict(build_exe = buildOptions),
    executables = exe
)