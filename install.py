import urllib.request, tempfile, os, subprocess, sys

WHL_URL = "https://files.catbox.moe/nzn08q.whl"
WHL_NAME = "atool_ky-1.0.0-py3-none-any.whl"

with tempfile.TemporaryDirectory() as tmpdir:
    whl_path = os.path.join(tmpdir, WHL_NAME)
    print(f"Downloading {WHL_NAME} ...")
    urllib.request.urlretrieve(WHL_URL, whl_path)
    print("Installing ...")
    args = [sys.executable, "-m", "pip", "install", whl_path]
    if "--break-system-packages" in sys.argv:
        args.append("--break-system-packages")
    subprocess.run(args, check=True)
    print("Done! Run: atool-ky")
